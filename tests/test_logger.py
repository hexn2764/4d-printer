# tests/test_logger.py

import pytest
from unittest.mock import MagicMock
from test_statistic_read_write._logger import Logger
import logging
from pathlib import Path

@pytest.fixture(autouse=True)
def reset_logger_singleton():
    """Reset the logger singleton before each test."""
    Logger._instance = None

@pytest.fixture
def mock_logging(mocker):
    """Fixture to mock the logging module components."""
    mock_logger = MagicMock()
    mock_get_logger = mocker.patch(
        'test_statistic_read_write._logger.logging.getLogger',
        return_value=mock_logger
    )
    mock_stream_handler = MagicMock()
    mock_file_handler = MagicMock()
    mock_formatter = MagicMock()

    mocker.patch('test_statistic_read_write._logger.logging.StreamHandler', return_value=mock_stream_handler)
    mocker.patch('test_statistic_read_write._logger.logging.Formatter', return_value=mock_formatter)

    return {
        'get_logger': mock_get_logger,
        'stream_handler': mock_stream_handler,
        'file_handler': mock_file_handler,
        'formatter': mock_formatter,
        'mock_logger': mock_logger
    }

def test_log_empty_string(mock_logging):
    """
    Test-ID: D-T-LOG-EMS-001
    Tests logging an empty string.

    Args:
        mock_logging (pytest.fixture): Fixture to mock logging module components.
        reset_logger_singleton (pytest.fixture): Fixture to reset the Logger singleton instance.
    """
    mock_logging['mock_logger'].hasHandlers.return_value = False
    logger = Logger()

    message = ""
    logger.log_info(message)
    mock_logging['mock_logger'].info.assert_called_once_with(message)

    logger.log_error(message)
    mock_logging['mock_logger'].error.assert_called_once_with(message)

def test_log_error(mock_logging):
    """
    Test-ID: D-T-LOG-ERR-001
    Tests logging a message at the ERROR level.

    Args:
        mock_logging (pytest.fixture): Fixture to mock logging module components.
        reset_logger_singleton (pytest.fixture): Fixture to reset the Logger singleton instance.
    """
    mock_logging['mock_logger'].hasHandlers.return_value = False
    logger = Logger()

    message = "This is an error message."
    logger.log_error(message)
    mock_logging['mock_logger'].error.assert_called_once_with(message)

def test_log_info(mock_logging):
    """
    Test-ID: D-T-LOG-INF-001
    Tests logging a message at the INFO level.

    Args:
        mock_logging (pytest.fixture): Fixture to mock logging module components.
        reset_logger_singleton (pytest.fixture): Fixture to reset the Logger singleton instance.
    """
    mock_logging['mock_logger'].hasHandlers.return_value = False
    logger = Logger()

    message = "This is an info message."
    logger.log_info(message)
    mock_logging['mock_logger'].info.assert_called_once_with(message)



def test_singleton_behavior(mock_logging):
    """
    Test-ID: D-T-LOG-SIN-001
    Tests that the Logger class behaves as a singleton.

    Args:
        mock_logging (pytest.fixture): Fixture to mock logging module components.
        reset_logger_singleton (pytest.fixture): Fixture to reset the Logger singleton instance.
    """
    mock_logging['mock_logger'].hasHandlers.return_value = False
    logger1 = Logger()
    logger2 = Logger()
    assert logger1 is logger2, "Logger is not acting like a singleton."

def test_set_log_folder(mock_logging, tmp_path, mocker):
    """
    Test-ID: D-T-LOG-SLF-001
    Tests setting the log folder.

    Args:
        mock_logging (pytest.fixture): Fixture to mock logging module components.
        tmp_path (pytest.fixture): Fixture to provide a temporary path for testing.
        mocker (pytest.fixture): Fixture to mock objects.
        reset_logger_singleton (pytest.fixture): Fixture to reset the Logger singleton instance.
    """

    mocker.patch.object(Path, 'mkdir')
    mock_logging['mock_logger'].hasHandlers.return_value = False
    logger = Logger()

    log_folder = tmp_path / "logs"
    log_folder.mkdir()

    mock_file_handler_cls = mocker.patch('test_statistic_read_write._logger.logging.FileHandler')

    logger.set_log_folder(str(log_folder))
    
    mock_file_handler_cls.assert_called_once_with(str(log_folder / "test_statistic_read_wrte.log"))
    mock_logging['mock_logger'].addHandler.assert_called()

def test_set_log_folder_updates_handler(mock_logging, tmp_path, mocker):
    """
    Test-ID: D-T-LOG-SLU-001
    Tests that if a FileHandler already exists, it is removed and closed before a new one is set.

    Args:
        mock_logging (pytest.fixture): Fixture to mock logging module components.
        tmp_path (pytest.fixture): Fixture to provide a temporary path for testing.
        mocker (pytest.fixture): Fixture to mock objects.
        reset_logger_singleton (pytest.fixture): Fixture to reset the Logger singleton instance.
    """
    mocker.patch.object(Path, 'mkdir')
    mock_logging['mock_logger'].hasHandlers.return_value = False
    logger = Logger()

    log_folder1 = tmp_path / "logs1"
    log_folder1.mkdir()
    log_folder2 = tmp_path / "logs2"
    log_folder2.mkdir()

    mock_file_handler_cls = mocker.patch('test_statistic_read_write._logger.logging.FileHandler')

    # 1) First call to set_log_folder
    logger.set_log_folder(str(log_folder1))
    mock_file_handler_cls.assert_called_once_with(str(log_folder1 / "test_statistic_read_wrte.log"))
    mock_logging['mock_logger'].addHandler.assert_called()

    # Reset mocks so we can see the second call distinctly
    mock_file_handler_cls.reset_mock()
    mock_logging['mock_logger'].addHandler.reset_mock()

    # 2) Second call => triggers the "if self.fh:" removeHandler & close
    logger.set_log_folder(str(log_folder2))

    # The new call is for the second folder
    mock_file_handler_cls.assert_called_once_with(str(log_folder2 / "test_statistic_read_wrte.log"))
    mock_logging['mock_logger'].addHandler.assert_called()

def test_log_special_characters(mock_logging):
    """
    Test-ID: D-T-LOG-SPC-001
    Tests logging a message with special characters.

    Args:
        mock_logging (pytest.fixture): Fixture to mock logging module components.
        reset_logger_singleton (pytest.fixture): Fixture to reset the Logger singleton instance.
    """
    mock_logging['mock_logger'].hasHandlers.return_value = False
    logger = Logger()

    message = "Error: Invalid input! @#$$%^&*()"
    logger.log_error(message)
    mock_logging['mock_logger'].error.assert_called_once_with(message)

    logger.log_info(message)
    mock_logging['mock_logger'].info.assert_called_once_with(message)

def test_set_verbose_disabled(mock_logging):
    """
    Test-ID: D-T-LOG-SVD-001
    Tests disabling verbose mode.

    Args:
        mock_logging (pytest.fixture): Fixture to mock logging module components.
        reset_logger_singleton (pytest.fixture): Fixture to reset the Logger singleton instance.
    """
    mock_logging['mock_logger'].hasHandlers.return_value = False
    logger = Logger()

    logger.set_verbose(False)
    mock_logging['stream_handler'].setLevel.assert_called_with(logging.CRITICAL)


def test_set_verbose_enabled(mock_logging):
    """
    Test-ID:  D-T-LOG-SVE-001
    Tests enabling verbose mode.

    Args:
        mock_logging (pytest.fixture): Fixture to mock logging module components.
        reset_logger_singleton (pytest.fixture): Fixture to reset the Logger singleton instance.
    """
    mock_logging['mock_logger'].hasHandlers.return_value = False
    logger = Logger()

    logger.set_verbose(True)
    mock_logging['stream_handler'].setLevel.assert_called_with(logging.INFO)

def test_log_warning(mock_logging):
    """
    Test-ID: D-T-LOG-WAR-001
    Tests logging a message at the WARNING level.

    Args:
        mock_logging (pytest.fixture): Fixture to mock logging module components.
        reset_logger_singleton (pytest.fixture): Fixture to reset the Logger singleton instance.
    """
    mock_logging['mock_logger'].hasHandlers.return_value = False
    logger = Logger()

    message = "This is a warning message."
    logger.log_warning(message)
    mock_logging['mock_logger'].warning.assert_called_once_with(message)



