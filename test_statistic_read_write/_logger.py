# test_statistic_read_write/_logger.py

import logging
import os

class Logger:
    """
    Singleton logger class for the test_statistic_read_write application.

    Provides methods for:
    - Setting the log folder (adds a FileHandler).
    - Setting verbose mode (adjusts console logging level).
    - Logging messages at different levels (info, error, warning).
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._initialize_logger()
        return cls._instance

    def _initialize_logger(self):
        """Initializes the logger with default settings."""
        self.logger = logging.getLogger("TestStatisticReadWrite")
        self.logger.setLevel(logging.DEBUG)

        # By default, no file handler (corresponds to a call without -L log folder option set)
        self.fh = None
        # By default, console handler at CRITICAL level (correponds to "no verbose")
        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.CRITICAL)

        # Set format
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.ch.setFormatter(formatter)

        if not self.logger.hasHandlers():
            self.logger.addHandler(self.ch)

    def set_log_folder(self, folder: str):
        """
        Attaches a FileHandler to write logs to the specified folder.
        Called if the -L option is set.

        Args:
            folder (str): The path to the folder where the log file should be created.
        """
        if self.fh:
            # if the log folder changes during execution
            self.logger.removeHandler(self.fh)
            self.fh.close()

        log_path = os.path.join(folder, "test_statistic_read_wrte.log")
        self.fh = logging.FileHandler(log_path)
        # DEBUG level, can be adjusted
        self.fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.fh.setFormatter(formatter)
        self.logger.addHandler(self.fh)

    def set_verbose(self, enabled: bool):
        """
        If enabled, sets console logging to INFO. If disabled, sets console logging to CRITICAL.

        Args:
            enabled (bool): Whether to enable verbose console logging.
        """
        if enabled:
            self.ch.setLevel(logging.INFO)
        else:
            self.ch.setLevel(logging.CRITICAL)

    def log_info(self, message: str):
        """Logs a message at the INFO level."""
        self.logger.info(message)

    def log_error(self, message: str):
        """Logs a message at the ERROR level."""
        self.logger.error(message)

    def log_warning(self, message: str):
        """Logs a message at the WARNING level."""
        self.logger.warning(message)

