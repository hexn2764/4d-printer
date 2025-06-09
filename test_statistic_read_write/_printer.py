# test_statistic_read_write/_printer.py

from typing import Dict, Any, List, Tuple


class Printer:
    """
    Displays analysis results on the console (or could be extended for other output).
    """

    def display_results(self, analysis: Dict[str, Any], formatting: bool = True):
        """
        Displays the analysis results either in a formatted table or as plain text.

        Args:
            analysis (Dict[str, Any]): Dictionary containing analysis results.
                                    Expected keys:
                                    - "total_duration": float representing the total duration.
                                    - "top_x_entries": List[Tuple[int, Dict[str, Any]]] representing the top entries.
                                    - "test_case_counts": Tuple[int, int, int] representing the total, valid, and skipped
                                                            test case counts.
                                    - "status_counts": Dict[str, int] representing the counts of each status.
            formatting (bool, optional): If True, displays results in a formatted table.
                                        If False, displays results as plain text. Defaults to True.
        """
        total_duration = analysis.get("total_duration", 0.0)
        top_entries = analysis.get("top_x_entries", [])
        test_case_counts = analysis.get("test_case_counts", (0, 0, 0))
        status_counts = analysis.get("status_counts", {})

        print(f"\nTotal Duration: {total_duration:.3f} Seconds.")

        total, valid, skipped = test_case_counts
        print(f"Total Amount of Cases: {total} ({valid} Parsed, {skipped} Skipped).")

        print("Status Counts (Parsed Cases Only):")
        if status_counts:
            for status, count in status_counts.items():
                print(f"  {status}: {count}")
        else:
            print("  No status data available.")

        num_entries = len(top_entries)
        if num_entries > 0:
            print(f"Top {num_entries} (Longest Tests):\n")
        else:
            return

        if formatting:
            self.do_advanced_output(top_entries)
        else:
            self.do_basic_output(top_entries)

    def do_advanced_output(self, top_entries: List[Tuple[int, Dict[str, Any]]]):
        """
        Displays the top entries in a formatted table with dynamic column widths.

        Args:
            top_entries (List[Tuple[int, Dict[str, Any]]]): List of top entries.
        """

        headers = ["ID", "Requirement", "Test Case", "Duration (sec)", "Status"]

        widths = self.get_width(top_entries, headers)
        # line format
        fmt = (
            f"{{id:>{widths[0]}}}"
            f"{{req:<{widths[1]}}}"
            f"{{tc:<{widths[2]}}}"
            f"{{dur:<{widths[3]}}}"
            f"{{stat:<{widths[4]}}}"
        )

        pad = " "*5  # "padding" spaces

        # Header
        header_line = fmt.format(
            id=headers[0] + pad,
            req=headers[1] + pad,
            tc=headers[2] + pad,
            dur=headers[3] + pad,
            stat=headers[4] + pad
        )
        print(header_line)

        # Separator line
        print("-" * sum(widths))

        # Entries
        for idx, (_, entry) in enumerate(top_entries, start=1):
            requirement = entry.get("Requirement", "")
            test_case = entry.get("Test Case", "")
            duration = f"{entry.get('Duration', 0.0):.3f}"  # Format duration to three decimal places
            status = entry.get("Status", "")

            print(
                fmt.format(
                    id=str(idx) + "." + pad,
                    req=requirement + pad,
                    tc=test_case + pad,
                    dur=duration + pad,
                    stat=status + pad
                )
            )

        # Separator line
        print("-" * sum(widths) + "\n")

    def do_basic_output(self, top_entries: List[Tuple[int, Dict[str, Any]]]):
        """
        Displays the top entries as plain text without any alignment or additional formatting.

        Args:
            top_entries (List[Tuple[int, Dict[str, Any]]]): List of top entries.
        """
        for idx, (_, entry) in enumerate(top_entries, start=1):
            requirement = entry.get("Requirement", "")
            test_case = entry.get("Test Case", "")
            duration = f"{entry.get('Duration', 0.0):.3f}"  # Format duration to three decimal places
            status = entry.get("Status", "")

            print(
                f"{idx}. Requirement: {requirement}, Test Case: {test_case}, "
                f"Duration: {duration} sec, Status: {status}"
            )
        print()  # spacing

    def get_width(
            self,
            top_entries: List[Tuple[int, Dict[str, Any]]],
            headers: List[str]
        ) -> List[int]:
            """
            Determines the maximum width for each column based on the data and headers.

            Args:
                top_entries (List[Tuple[int, Dict[str, Any]]]): List of top entries.
                headers (List[str]): List of header names.

            Returns:
                List[int]: List of widths for each column.

            NOTE: This logic can be integrated into the CSV reading phase to avoid double data iteration.
            """
            padding = 5     # amount of padding symbols
            precision = 3   # amount of precision digits
            dot = 1         # one char for decimal dot

            # The desired width is the maximum of the <header_name_length> and <entry_name_length>, together with padding and precision.
            widths = [
                max(
                    len(header),
                    max(
                        (len(f"{id_}.") for id_, _ in top_entries), # adds the dot after ID
                        default=0
                    ) if header == "ID" else
                    max(
                        (len(str(int(data.get(header, 0)))) + dot + precision for _, data in top_entries), # floors a float and adds a dot and precision
                        default=0
                    ) if header == "Duration" else
                    max(
                        (len(str(data.get(header, ""))) for _, data in top_entries), # Status
                        default=0
                    )
                ) + padding
                for header in headers
            ]

            return widths
    
