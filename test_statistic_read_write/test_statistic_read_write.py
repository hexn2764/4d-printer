# test_statistic_read_write/test_statistic_read_write.py

import sys
from ._logger import Logger
from ._csv_handler import CSVHandler
from ._analyser import Analyser
from ._printer import Printer
from test_statistic_read_write._exceptions import *
import os 

class TestStatisticReadWrite:
    __test__ = False
    """
    High-level orchestrator:

      1. CSVHandler reads CSV.
      2. Analyser computes results, Printer displays them.
      3. CSVHandler exports CSV sorted by a chosen field (internal logic).
    """

    def __init__(self, csv_path: str, output_folder: str, top_x: int = 10, sort_key: str = "Duration", log_folder: str = None, verbose: bool = False):
        """
        Initializes the TestStatisticReadWrite orchestrator.

        Args:
            csv_path (str): Path to the input CSV file.
            output_folder (str): Path to the output folder for the exported CSV.
            top_x (int): Number of top entries to display in the analysis results.
            sort_key (str, optional): The key to sort by for CSV export. Defaults to "Duration".
            log_folder (str, optional): Path to the folder for log files. Defaults to None.
            verbose (bool, optional): If True, enables verbose logging. Defaults to False.
        """
        self.logger = Logger()  

        self.csv_path = csv_path
        self.output_folder = output_folder
        self.top_x = top_x
        self.sort_key = sort_key
        self.log_folder = log_folder
        self.verbose = verbose

        self.csv_handler = CSVHandler(self.csv_path)
        self.analyser = Analyser()
        self.printer = Printer()

    @property
    def csv_path(self) -> str:
        return self._csv_path

    @csv_path.setter
    def csv_path(self, value: str):
        if value is None:
            self.logger.log_error("TestStatisticReadWrite: csv_path cannot be None.")
            raise InputFileNotFound("csv_path cannot be None")
        if not os.path.isfile(value):
            self.logger.log_error(f"TestStatisticReadWrite: Input file does not exist: {value}")
            raise InputFileNotFound(f"Input file not found: {value}")
        self._csv_path = value

    @property
    def output_folder(self) -> str:
        return self._output_folder

    @output_folder.setter
    def output_folder(self, value: str):
        if value is None:
            self.logger.log_error("TestStatisticReadWrite: output_folder cannot be None.")
            raise OutputFolderError("output_folder cannot be None")
        if not os.path.exists(value):
            try:
                os.makedirs(value)
            except Exception as e:
                self.logger.log_error(f"TestStatisticReadWrite: Could not create output folder '{value}': {e}")
                raise OutputFolderError(f"Cannot create output folder '{value}': {e}")
        self._output_folder = value
        self.logger.log_info(f"TestStatisticReadWrite: Output folder set: {value}")

    @property
    def top_x(self) -> int:
        return self._top_x

    @top_x.setter
    def top_x(self, value: int):
        if not isinstance(value, int) or value < 0:
            self.logger.log_error(f"TestStatisticReadWrite: Invalid top_x value: {value}. Must be a non-negative integer.")
            raise InvalidTopX(f"Invalid top_x value: {value}. Must be a non-negative integer.")
        self._top_x = value

    @property
    def sort_key(self) -> str:
        return self._sort_key

    @sort_key.setter
    def sort_key(self, value: str):
        valid_keys = ["Requirement", "Test Case", "Duration", "Status", "none"]
        if value not in valid_keys:
            self.logger.log_error(f"TestStatisticReadWrite: Invalid sort key '{value}'. Must be in {valid_keys}.")
            raise InvalidSortingKey(f"Invalid sort key '{value}'. Must be one of {valid_keys}.")
        self._sort_key = value

    @property
    def log_folder(self) -> str:
        return self._log_folder

    @log_folder.setter
    def log_folder(self, value: str):
        if value is not None:
            if not os.path.exists(value):
                try:
                    os.makedirs(value)
                except Exception as e:
                    self.logger.log_error(f"TestStatisticReadWrite: Could not create log folder '{value}': {e}")
                    raise OutputFolderError(f"Cannot create log folder '{value}': {e}")
            self.logger.set_log_folder(value)
            self.logger.log_info(f"TestStatisticReadWrite: Log folder set: {value}")
        self._log_folder = value

    @property
    def verbose(self) -> bool:
        return self._verbose

    @verbose.setter
    def verbose(self, value: bool):
        self.logger.set_verbose(value)
        self._verbose = value


    def run(self):
        """
        Runs the main processing pipeline:

        1. Reads data from CSV using CSVHandler.
        2. Analyzes the data using Analyser.
        3. Displays results using Printer.
        4. Exports the sorted CSV using CSVHandler.

        Raises:
            FriendlyException: If any error occurs during the processing.
        """
        try:
            # read CSV
            data = self.csv_handler.read_csv()
            # analyze read data
            result = self.analyser.analyze(data, self.top_x)
            # print to console
            self.printer.display_results(result)
            # export CSV
            self.csv_handler.export_csv(data, self.output_folder, sort_key=self.sort_key)

        except FriendlyException as e:
            user_msg = f"Error in processing. {e.user_message}. Exiting."
            print(user_msg)
            self.logger.log_error(user_msg)
            sys.exit(1)

    

    def reset(self):
        self.csv_handler = CSVHandler(self.csv_path)
