# test_statistic_read_write/_exceptions.py

class FriendlyException(Exception):
    """
    Base class for errors that must stop the program.
    """
    def __init__(self, user_message: str):
        super().__init__(user_message)
        self.user_message = user_message


class InputFileNotFound(FriendlyException):
    """Raised when the input file does not exist."""
    pass


class OutputFolderError(FriendlyException):
    """Raised when the output folder cannot be created or there is no access."""
    pass


class InvalidTopX(FriendlyException):
    """Raised when the top_x value is invalid."""
    pass


class EmptyFileError(FriendlyException):
    """Raised when the input CSV file is empty."""
    pass


class InvalidHeaderColumns(FriendlyException):
    """Raised when the CSV header does not have exactly 3 columns."""
    pass


class InvalidHeaderFormat(FriendlyException):
    """Raised when the CSV header format does not match the expected format."""
    pass


class NoDataLinesError(FriendlyException):
    """Raised when the CSV file has no data lines after the header."""
    pass


class NoValidLinesError(FriendlyException):
    """Raised when no valid data lines are found in the CSV after parsing and validation."""
    pass


class CSVExportError(FriendlyException):
    """Raised when there is a general error during CSV export."""
    pass


class InvalidSortingKey(FriendlyException):
    """Raised when an invalid sorting key is provided for CSV export."""
    pass