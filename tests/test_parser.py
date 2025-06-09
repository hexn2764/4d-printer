# tests/test_parser.py

import pytest
from unittest.mock import MagicMock
from test_statistic_read_write._parser import TestCaseParser, DurationParser, StatusParser

@pytest.fixture
def mock_logger(mocker):
    """Fixture to mock the Logger class."""
    mock_logger = MagicMock()
    mocker.patch('test_statistic_read_write._parser.Logger', return_value=mock_logger)
    return mock_logger

@pytest.fixture
def test_case_parser(mock_logger):
    """Fixture to create a TestCaseParser instance."""
    return TestCaseParser()

@pytest.fixture
def duration_parser(mock_logger):
    """Fixture to create a DurationParser instance."""
    return DurationParser()

@pytest.fixture
def status_parser(mock_logger):
    """Fixture to create a StatusParser instance."""
    return StatusParser()

@pytest.mark.parametrize("input_str, expected, log_message", [
    # Single Time Unit - Valid
    ("5 sec", 5.0, None),
    ("5.4 sec", 5.4, None),
    ("15 ms", 0.015, None),
    ("75 ns", 7.5e-08, None),
    ("1 hr", 3600.0, None),
    ("1.5 hour", 5400.0, None),

    # Multiple Time Units - Valid
    ("2 min 48 sec", 168.0, None),
    ("1 hour 2 min 28 sec", 3748.0, None),
    ("3 hr 45 min 15 sec", 13515.0, None),
    ("1 hr 60 min", 7200.0, None),

    # Case Insensitivity & Extra Spaces - Valid
    ("5 SEC", 5.0, None),
    ("  5   sec  ", 5.0, None),
    ("5 sEc", 5.0, None),

    # Invalid Inputs
    ("", None, "DurationParser: Time format incorrect: ''"),
    ("   ", None, "DurationParser: Time format incorrect: '   '"),
    ("5", None, "DurationParser: Time format incorrect: '5'"),
    ("5 seconds", None, "DurationParser: Unknown unit 'seconds' in '5 seconds'."),
    ("5sec", None, "DurationParser: Time format incorrect: '5sec'"),
    ("5 sec some text", None, "DurationParser: Unrecognized components in '5 sec some text': 'sometext'"),
    ("0 min 0 sec", None, "DurationParser: Total duration is zero for '0 min 0 sec'."),
    ("50 cent", None, "DurationParser: Unknown unit 'cent' in '50 cent'."),
    ("5 sec 5 sec", None, "DurationParser: Unit 'sec' used multiple times in '5 sec 5 sec'."),
    ("-0 sec", None, "DurationParser: Total duration is zero for '-0 sec'."),
    ("five sec", None, "DurationParser: Time format incorrect: 'five sec'"),
    ("5 days", None, "DurationParser: Unknown unit 'days' in '5 days'."),
    ("5 sec extra", None, "DurationParser: Unrecognized components in '5 sec extra': 'extra'"),
    ("-5 sec", None, "DurationParser: Negative value '-5.0 sec' in '-5 sec'."),
])
def test_duration_parser_parse(duration_parser, mock_logger, input_str, expected, log_message):
    """
    Test-ID: D-T-PAR-DPV-001
    Parameterized test for the DurationParser.parse method, covering various valid and invalid inputs.

    Args:
        duration_parser (DurationParser): The DurationParser fixture.
        mock_logger (MagicMock): The mocked Logger fixture.
        input_str (str): The input time string to parse.
        expected (float or None): The expected parsed duration in seconds, or None if an error is expected.
        log_message (str or None): The expected error message, or None if no error is expected.
    """
    result = duration_parser.parse(input_str)

    if expected is None:
        assert result is None
        if log_message:
            mock_logger.log_error.assert_called_once_with(log_message)
    else:
        assert result == pytest.approx(expected)

def test_duration_parser_parse_invalid_numeric(duration_parser, mock_logger, mocker):
    """
    Test-ID: D-T-PAR-DPV-002
    Tests parsing an invalid numeric value in a time string using the DurationParser.

    Args:
        duration_parser (DurationParser): The DurationParser fixture.
        mock_logger (MagicMock): The mocked Logger fixture.
        mocker (pytest.mocker): The mocker fixture.
    """
    mocker.patch('builtins.float', side_effect=ValueError("Cannot convert to float"))

    result = duration_parser.parse("5 sec")
    assert result is None
    mock_logger.log_error.assert_called_with("DurationParser: Invalid numeric value '5' in '5 sec'")

def test_status_parser_empty(status_parser):
    """
    Test-ID: D-T-PAR-SPE-001
    Tests parsing an empty status string using the StatusParser.

    Args:
        status_parser (StatusParser): The StatusParser fixture.
    """
    result = status_parser.parse("")
    assert result == ""

def test_status_parser_spaces(status_parser):
    """
    Test-ID: D-T-PAR-SPS-001
    Tests parsing a valid status string with leading/trailing spaces using the StatusParser.

    Args:
        status_parser (StatusParser): The StatusParser fixture.
    """
    result = status_parser.parse("  Passed  ")
    assert result == "Passed"

def test_status_parser_valid(status_parser):
    """
    Test-ID: D-T-PAR-SPV-001
    Tests parsing a valid status string using the StatusParser.

    Args:
        status_parser (StatusParser): The StatusParser fixture.
    """
    result = status_parser.parse("Passed")
    assert result == "Passed"

def test_test_case_parser_empty_part(test_case_parser, mock_logger):
    """
    Test-ID: D-T-PAR-TCE-001
    Tests parsing an invalid test case string (empty part) using the TestCaseParser.

    Args:
        test_case_parser (TestCaseParser): The TestCaseParser fixture.
        mock_logger (MagicMock): The mocked Logger fixture.
    """
    result = test_case_parser.parse("R1\\")
    assert result is None
    mock_logger.log_error.assert_called_once_with("TestCaseParser: One side of the backslash is empty in 'R1\\'.")

def test_test_case_parser_invalid_format(test_case_parser, mock_logger):
    """
    Test-ID: D-T-PAR-TCI-001
    Tests parsing an invalid test case string (missing backslash) using the TestCaseParser.

    Args:
        test_case_parser (TestCaseParser): The TestCaseParser fixture.
        mock_logger (MagicMock): The mocked Logger fixture.
    """
    result = test_case_parser.parse("R1TC1")
    assert result is None
    mock_logger.log_error.assert_called_once_with("TestCaseParser: Expected exactly one backslash in 'R1TC1'.")

def test_test_case_parser_valid(test_case_parser):
    """
    Test-ID: D-T-PAR-TCV-001
    Tests parsing a valid test case string using the TestCaseParser.

    Args:
        test_case_parser (TestCaseParser): The TestCaseParser fixture.
    """
    result = test_case_parser.parse("R1\\TC1")
    assert result == {"Requirement": "R1", "Test Case": "TC1"}

def test_test_case_parser_valid_spaces(test_case_parser):
    """
    Test-ID: D-T-PAR-TCV-002
    Tests parsing a valid test case string with leading/trailing spaces using the TestCaseParser.

    Args:
        test_case_parser (TestCaseParser): The TestCaseParser fixture.
    """
    result = test_case_parser.parse(" R1 \\ TC1 ")
    assert result == {"Requirement": "R1", "Test Case": "TC1"}

