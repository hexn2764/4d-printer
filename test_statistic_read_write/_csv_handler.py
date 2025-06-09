# test_statistic_read_write/_csv_handler.py

import os
import time
from ._logger import Logger
from ._parser import TestCaseParser, DurationParser, StatusParser
from ._data import Data
from ._exceptions import *
import uuid

class CSVHandler:
    """
    Responsible for:
    1) Reading a CSV into a Data object.
    2) Exporting a CSV from Data, sorted by a given key.

    No analysis or display logic here.
    """

    def __init__(self, csv_path: str):
        self.logger = Logger()
        self.csv_path = csv_path

        self.parsers = {
            "Test Case": TestCaseParser(),
            "Duration": DurationParser(),
            "Status": StatusParser()
        }


    def read_csv(self):
        """
        Reads and validates CSV line by line, populating a new Data object.

        The method returns the populated Data object after processing the CSV file.
        It performs several validation checks on the input CSV, including file existence,
        format, and content, raising appropriate exceptions if issues are found.

        Parsed data is stored in a Data object, and lines that fail validation are
        recorded for review.

        Note: 
            The parsers used (TestCaseParser, DurationParser, StatusParser) are
            non-destructive. They return None on parsing errors instead of raising
            exceptions, allowing the CSVHandler to continue processing and report
            all errors.

        Raises:
            InputFileNotFound: If the input file cannot be opened.
            EmptyFileError: If the input CSV is empty.
            InvalidHeaderColumns: If the header does not have exactly 3 columns.
            InvalidHeaderFormat: If the header does not match 'Test case;Duration;Status'.
            NoDataLinesError: If no data lines are found after the header.
            NoValidLinesError: If no valid data lines are found in the CSV.

        Returns:
            Data: The populated Data object containing the parsed and validated CSV data.
        """
        data = Data()

        try:
            with open(self.csv_path, mode='r', encoding='utf-8') as f:
                lines = f.readlines()
        except Exception as e:
            self.logger.log_error(f"CSVHandler: Error reading file '{self.csv_path}': {e}")
            raise InputFileNotFound(f"Cannot open file: {e}")

        # Step 2: check if the file is empty
        if not lines:
            self.logger.log_error("CSVHandler: File is empty.")
            raise EmptyFileError("Input CSV is empty")

        # Step 3: validate header
        first_line = lines[0].strip()
        expected_header = ["Test case", "Duration", "Status"]
        header_parts = first_line.split(";")

        # 3-1: check if exactly 3 columns
        if len(header_parts) != 3:
            self.logger.log_error(
                f"CSVHandler: Invalid header. Expected 3 columns, found {len(header_parts)}."
            )
            raise InvalidHeaderColumns("Header must have exactly 3 columns")
        
        # 3-2 check if all columns match
        if header_parts != expected_header:
            self.logger.log_error(
                f"CSVHandler: Header mismatch. Expected {expected_header}, got {header_parts}."
            )
            raise InvalidHeaderFormat("Header does not match 'Test case;Duration;Status'")

        # Step 4: check at least one data line
        if len(lines) == 1:
            self.logger.log_error("CSVHandler: No data lines found after header.")
            raise NoDataLinesError("No data lines found after header.")

        # The loop. Processes each line after the header. Exceptions are not thrown inside the loop, as invalid lines are handled.
        current_id = 1
        for lineno in range(1, len(lines)):
            row_str = lines[lineno].rstrip("\n")
            columns = row_str.split(";")

            # Step 5: check columns
            if len(columns) != 3:
                self.logger.log_warning(
                    f"CSVHandler: Line {lineno+1} has {len(columns)} columns, skipping."
                )
                data.review_lines.append((lineno+1, f"{len(columns)} columns instead of 3"))
                continue

            test_case_str, duration_str, status_str = columns

            # Step 6: check empty fields
            if not test_case_str.strip() or not duration_str.strip() or not status_str.strip():
                self.logger.log_warning(
                    f"CSVHandler: Empty field at line {lineno+1}, skipping."
                )
                data.review_lines.append((lineno+1, "Empty field"))
                continue

            # Step 7a) TestCase
            parsed_tc = self.parsers.get("Test Case").parse(test_case_str)
            if parsed_tc is None:
                self.logger.log_warning(
                    f"CSVHandler: Test Case parsing error at line {lineno+1}, skipping."
                )
                data.review_lines.append((lineno+1, f"Test case parse error. Invalid value: '{test_case_str}'"))
                continue

            # Step 7b) Duration
            parsed_duration = self.parsers.get("Duration").parse(duration_str)
            if parsed_duration is None:
                self.logger.log_warning(
                    f"CSVHandler: Duration parsing error at line {lineno+1}, skipping."
                )
                data.review_lines.append((lineno+1, f"Duration parse error. Invalid value: '{duration_str}'"))
                continue

            # Step 7c) Status
            parsed_status = self.parsers.get("Status").parse(status_str)
            if parsed_status is None: # now not possible, as the Parser performs no validity checks
                self.logger.log_warning(
                    f"CSVHandler: Status parsing error at line {lineno+1}, skipping."
                )
                data.review_lines.append((lineno+1, f"Status parse error. Invalid value: '{status_str}'"))
                continue

            # Build the final entry
            entry = {
                "Requirement": parsed_tc["Requirement"],
                "Test Case": parsed_tc["Test Case"],
                "Duration": parsed_duration,
                "Status": parsed_status
            }
            data.add_entry(current_id, entry)
            current_id += 1

        # Step 8: check if we have any data lines (possible if the file contained a valid header but invalid data lines)
        if data.get_size() == 0:
            self.logger.log_error("CSVHandler: No valid data lines found.")
            raise NoValidLinesError("No valid lines in CSV")

        # Finally, log and notify about skipped lines
        self._log_review_lines(data)

        return data

    def _log_review_lines(self, data):
        """
        Logs a warning message with the number of skipped lines and their reasons.

        Args:
            data (Data): The Data object containing the review_lines information.
        """
        if data.review_lines:
            self.logger.log_warning(
                f"{len(data.review_lines)} lines were skipped. Detailed reasons: {data.review_lines}"
            )

            print(f"{len(data.review_lines)} lines were skipped.")
            for (line_no, reason) in data.review_lines:
                print(f"  - Line {line_no} skipped: {reason}")

    def export_csv(self, data: Data, export_folder: str, sort_key: str = "Duration", timestamp: bool = False):
        """
        Exports the data to a CSV file. The entries will be written in the order defined by the provided sort_key.

        Args:
            data (Data): The data object containing the entries to export.
            export_folder (str): The path to the folder where the exported CSV will be saved.
            sort_key (str): The key that determines the order of entries in the exported CSV.
                            Valid options: 'Requirement', 'Test Case', 'Duration', 'Status', or 'none'.
            timestamp (bool): Whether to include a timestamp in the filename.

        Raises:
            CSVExportError: If there is an error writing the CSV file.
        """
        
        if sort_key == "Requirement":
            sorted_ids = data.sorted_ids["Requirement"]  
        elif sort_key == "Test Case":
            sorted_ids = data.sorted_ids["Test Case"]
        elif sort_key == "Duration":
            sorted_ids = data.sorted_ids["Duration"] 
        elif sort_key == "Status":
            sorted_ids = data.sorted_ids["Status"]
        elif sort_key == "none":
            sorted_ids = list(data.data.keys())

        output_name = self._generate_output_filename(sort_key, timestamp)
        export_file = os.path.join(export_folder, output_name)

        try:
            with open(export_file, mode='w', encoding='utf-8') as f:
                f.write("Requirement;Test Case;Duration;Status\n")
                for cid in sorted_ids:
                    entry = data.data[cid]
                    duration = entry['Duration']
                    if duration < 1e-6:
                        formatted_duration = f"{duration:.9f}".rstrip("0").rstrip(".")
                    elif duration < 60:
                        formatted_duration = f"{duration:.6f}".rstrip("0").rstrip(".")
                    else:
                        formatted_duration = f"{duration:.3f}".rstrip("0").rstrip(".")
                    line = (f"{entry['Requirement']};"
                            f"{entry['Test Case']};"
                            f"{formatted_duration};"
                            f"{entry['Status']}\n")
                    f.write(line)
            self.logger.log_info(f"CSVHandler: Exported CSV to '{export_file}'.")
            print(f"CSV exported successfully to {export_file}")
        
        except Exception as e:
            self.logger.log_error(f"CSVHandler: Failed exporting CSV: {e}")
            raise CSVExportError(f"Failed to write CSV file: {e}")

    def _generate_output_filename(self, sort_key: str, timestamp: bool = False) -> str:
        """
        Generates the output filename based on the base name of the input CSV,
        the sort key, and an optional timestamp.

        Args:
            sort_key (str): The key used for sorting.
            timestamp (bool): Whether to include a timestamp in the filename.

        Returns:
            str: The generated output filename.
        """
        base_name = os.path.splitext(os.path.basename(self.csv_path))[0]
        output_name = base_name + "_"

        if sort_key.lower() != "none":
            output_name += f"sorted_by_{sort_key}"

        if timestamp:
            timestamp_str = time.strftime("%Y%m%d_%H%M%S") + "_" + str(uuid.uuid4())[:6]
            output_name += "_" + timestamp_str

        output_name += ".csv"
        return output_name
    
