# tests/test_test_statistic_read_write.py

import pytest
import os
from unittest.mock import patch, MagicMock

from test_statistic_read_write.test_statistic_read_write import TestStatisticReadWrite
from test_statistic_read_write._exceptions import *


@pytest.fixture
def mock_logger(mocker):
    """
    Fixture to patch the Logger in TestStatisticReadWrite so we can
    check calls to log_error, log_warning, etc.
    """
    return mocker.patch('test_statistic_read_write.test_statistic_read_write.Logger', autospec=True).return_value

@pytest.fixture
def mock_csv_handler(mocker):
    """
    Patch the CSVHandler so we can simulate read_csv and export_csv behavior.
    """
    # The instance
    instance = mocker.patch('test_statistic_read_write.test_statistic_read_write.CSVHandler', autospec=True).return_value
    instance.read_csv = MagicMock()
    instance.export_csv = MagicMock()
    return instance

@pytest.fixture
def mock_analyser(mocker):
    """
    Patch the Analyser so we can intercept .analyze(...) calls.
    """
    instance = mocker.patch('test_statistic_read_write.test_statistic_read_write.Analyser', autospec=True).return_value
    instance.analyze = MagicMock(return_value={
        "total_duration": 999.999,
        "top_x_entries": []
    })
    return instance

@pytest.fixture
def mock_printer(mocker):
    """
    Patch the Printer so we can intercept .display_results(...) calls.
    """
    instance = mocker.patch('test_statistic_read_write.test_statistic_read_write.Printer', autospec=True).return_value
    instance.display_results = MagicMock()
    return instance

@pytest.fixture
def mock_makedirs(mocker):
    """Fixture to mock out os.makedirs calls in TestStatisticReadWrite."""
    return mocker.patch("test_statistic_read_write.test_statistic_read_write.os.makedirs")

@pytest.fixture
def mock_path_exists(mocker):
    """Fixture to mock out os.path.exists calls in TestStatisticReadWrite."""
    return mocker.patch("test_statistic_read_write.test_statistic_read_write.os.path.exists", return_value=True)

@pytest.fixture
def mock_is_file(mocker):
    """Fixture to mock out os.path.isfile calls in TestStatisticReadWrite."""
    return  mocker.patch("test_statistic_read_write.test_statistic_read_write.os.path.isfile", return_value=True)

def test_log_folder_creation_fails(mocker, mock_logger):
    """
    Test-ID: D-T-ORC-LFC-001
    Verifies that an OutputFolderError is raised when log folder creation fails during TestStatisticReadWrite initialization.

    This test mocks `os.makedirs` to simulate an `OSError`, ensuring that the
    `TestStatisticReadWrite` class correctly handles failures in creating the log directory.
    It checks that the expected exception is raised and that the error message is properly logged.

    Args:
        mocker (pytest_mock.plugin.MockerFixture): Fixture for mocking objects.
        mock_logger (pytest.fixture): Fixture providing a mocked Logger instance.
    """

    def path_exists_mock(path):
        if path == "output":
            return True
        else:
            return False
        
    def makedirs_mock(path):
        if os.path.basename(path) == "logdir": # here already changed to abspath by main!
            raise OSError("No permission")

    mocker.patch("test_statistic_read_write.test_statistic_read_write.os.path.isfile", return_value=True)
    mocker.patch("test_statistic_read_write.test_statistic_read_write.os.path.exists", side_effect=path_exists_mock)
    mocker.patch('test_statistic_read_write.test_statistic_read_write.os.makedirs', side_effect=makedirs_mock)

    with pytest.raises(OutputFolderError) as exc_info:
        TestStatisticReadWrite("input.csv", "output", log_folder="logdir", verbose=False)

    assert "Cannot create log folder 'logdir'" in str(exc_info.value)

def test_output_folder_creation_fails(mocker):
    """
    Test-ID: D-T-ORC-OFC-001
    Verifies that an OutputFolderError is raised when output folder creation fails during TestStatisticReadWrite initialization.

    This test mocks `os.makedirs` to simulate an `OSError`, ensuring that the
    `TestStatisticReadWrite` class correctly handles failures in creating the output directory.
    It checks that the expected exception is raised and that the error message is properly logged.

    Args:
        mocker (pytest_mock.plugin.MockerFixture): Fixture for mocking objects.
    """
    mocker.patch("test_statistic_read_write.test_statistic_read_write.os.path.isfile", return_value=True)
    mocker.patch('test_statistic_read_write.test_statistic_read_write.os.path.exists', return_value=False)
    mock_makedirs = mocker.patch('test_statistic_read_write.test_statistic_read_write.os.makedirs', side_effect=OSError("Mocked: No permission to create folder"))
    mock_logger = mocker.patch('test_statistic_read_write.test_statistic_read_write.Logger', autospec=True).return_value

    with pytest.raises(OutputFolderError) as exc_info:
        TestStatisticReadWrite("input.csv", "nonexistent_output", log_folder=None, verbose=False)

    assert "Cannot create output folder" in str(exc_info.value)
    assert "Mocked: No permission to create folder" in str(exc_info.value)
    mock_logger.log_error.assert_called_once_with("TestStatisticReadWrite: Could not create output folder 'nonexistent_output': Mocked: No permission to create folder")


def test_run_friendly_exception_at_read(mock_is_file, mock_makedirs, mock_logger, mock_csv_handler, mock_analyser, mock_printer, mocker, capsys):
    """
    Test-ID: D-T-ORC-RFE-001
    Verifies that the `run` method handles `FriendlyException` during `read_csv`, logs/prints an error, and exits with 1.

    Args:
        mock_is_file (pytest.fixture): Fixture providing a mocked `os.path.isfile`.
        mock_makedirs (pytest.fixture): Fixture providing a mocked `os.makedirs`.
        mock_logger (pytest.fixture): Fixture providing a mocked Logger instance.
        mock_csv_handler (pytest.fixture): Fixture providing a mocked CSVHandler instance.
        mock_analyser (pytest.fixture): Fixture providing a mocked Analyser instance.
        mock_printer (pytest.fixture): Fixture providing a mocked Printer instance.
        mocker (pytest_mock.plugin.MockerFixture): Fixture for mocking utilities.
        capsys (pytest.fixture): Fixture for capturing stdout and stderr.
    """
    orchestrator = TestStatisticReadWrite("in.csv", "out_dir", 3)

    # Assume that the file does not exist, is empty, etc.
    mock_csv_handler.read_csv.side_effect = FriendlyException("Mocked read error")

    # Check the exit
    mock_exit = mocker.patch("sys.exit")
    orchestrator.run()
    mock_exit.assert_called_once_with(1)

    # analyze not called, etc.
    mock_analyser.analyze.assert_not_called()
    mock_printer.display_results.assert_not_called()
    mock_csv_handler.export_csv.assert_not_called()

    captured = capsys.readouterr()
    assert "Error in processing. Mocked read error. Exiting." in captured.out
    mock_logger.log_error.assert_called_once_with("Error in processing. Mocked read error. Exiting.")


def test_run_friendly_exception_at_export(mock_is_file, mock_makedirs, mock_logger, mock_csv_handler, mock_analyser, mock_printer, mocker, capsys):
    """
    Test-ID: D-T-ORC-RFE-002
    Verifies that the `run` method handles `FriendlyException` during `export_csv`, logs/prints an error, and exits with 1.

    Args:
        mock_is_file (pytest.fixture): Fixture providing a mocked `os.path.isfile`.
        mock_makedirs (pytest.fixture): Fixture providing a mocked `os.makedirs`.
        mock_logger (pytest.fixture): Fixture providing a mocked Logger instance.
        mock_csv_handler (pytest.fixture): Fixture providing a mocked CSVHandler instance.
        mock_analyser (pytest.fixture): Fixture providing a mocked Analyser instance.
        mock_printer (pytest.fixture): Fixture providing a mocked Printer instance.
        mocker (pytest_mock.plugin.MockerFixture): Fixture for mocking utilities.
        capsys (pytest.fixture): Fixture for capturing stdout and stderr.
    """
    orchestrator = TestStatisticReadWrite("in2.csv", "out_dir2", 5)
  
    mock_csv_handler.export_csv.side_effect = FriendlyException("Mocked export failure")

    mock_exit = mocker.patch("sys.exit")
    orchestrator.run()
    mock_exit.assert_called_once_with(1)

    mock_csv_handler.read_csv.assert_called_once()
    mock_analyser.analyze.assert_called_once()
    mock_printer.display_results.assert_called_once()

    captured = capsys.readouterr()
    assert "Error in processing. Mocked export failure. Exiting." in captured.out
    mock_logger.log_error.assert_called_once()

def test_run_unexpected_exception(mock_is_file, mock_makedirs, mock_logger, mock_csv_handler, mock_analyser, mock_printer, mocker, capsys):
    """
    Test-ID: D-T-ORC-RUE-001
    Verifies that the `run` method allows unhandled exceptions (not `FriendlyException`) to propagate.

    Args:
        mock_is_file (pytest.fixture): Fixture providing a mocked `os.path.isfile`.
        mock_makedirs (pytest.fixture): Fixture providing a mocked `os.makedirs`.
        mock_logger (pytest.fixture): Fixture providing a mocked Logger instance.
        mock_csv_handler (pytest.fixture): Fixture providing a mocked CSVHandler instance.
        mock_analyser (pytest.fixture): Fixture providing a mocked Analyser instance.
        mock_printer (pytest.fixture): Fixture providing a mocked Printer instance.
        mocker (pytest_mock.plugin.MockerFixture): Fixture for mocking utilities.
        capsys (pytest.fixture): Fixture for capturing stdout and stderr.
    """
    orchestrator = TestStatisticReadWrite("in3.csv", "out3", 7)
    mock_csv_handler.read_csv.side_effect = ValueError("Some unexpected error")

    # Because the code only catches FriendlyException, a ValueError is not handled => it will bubble up
    with pytest.raises(ValueError, match="Some unexpected error"):
        orchestrator.run()

    # Confirm no logging of "Error in processing."
    mock_logger.log_error.assert_not_called()
    # The rest not called
    mock_analyser.analyze.assert_not_called()
    mock_printer.display_results.assert_not_called()
    mock_csv_handler.export_csv.assert_not_called()

def test_set_sort_key(mocker, mock_makedirs):
    """
    Test-ID: D-T-ORC-SSK-001
    Verifies that the `set_sort_key` method correctly updates the `sort_key` attribute of the TestStatisticReadWrite class.

    Args:
        mocker (pytest_mock.plugin.MockerFixture): Fixture for mocking objects.
        mock_makedirs (pytest.fixture): Fixture providing a mocked `os.makedirs`.
    """
    mocker.patch("test_statistic_read_write.test_statistic_read_write.os.path.isfile", return_value=True)
    orchestrator = TestStatisticReadWrite("some.csv", "out", 10)
    assert orchestrator.sort_key == "Duration"
    orchestrator.sort_key = "Status"
    assert orchestrator.sort_key == "Status"
