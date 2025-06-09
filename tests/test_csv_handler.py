# tests/test_csv_handler.py

import pytest
from unittest.mock import patch
from test_statistic_read_write._csv_handler import CSVHandler
from test_statistic_read_write._data import Data
from test_statistic_read_write._exceptions import *

@pytest.fixture
def mock_logger(mocker):
    """Fixture to mock the Logger class."""
    return mocker.patch('test_statistic_read_write._csv_handler.Logger').return_value

@pytest.fixture
def sample_data():
    """Fixture to create a sample Data object."""
    data = Data()
    data.add_entry(1, {"Requirement": "R1", "Test Case": "TC1", "Duration": 10.5, "Status": "Passed"})
    data.add_entry(2, {"Requirement": "R2", "Test Case": "TC2", "Duration": 5.2, "Status": "Failed"})
    return data

def test_export_csv_valid(mocker, sample_data):
    """
    Test-ID: D-T-CSV-EXC-001
    Tests exporting data to CSV with valid data and sorting.

    This test verifies that the export_csv method correctly formats and
    exports data to a CSV file, sorted by the specified key. It uses a
    mocked file object to capture the written content without interacting
    with the actual file system.

    Args:
        mocker (pytest_mock.plugin.MockerFixture): Fixture for mocking objects.
        sample_data (Data): Fixture providing sample data for the test.
    """
    mock_open = mocker.mock_open()
    mocker.patch("builtins.open", mock_open)

    csv_handler = CSVHandler("dummy.csv")
    csv_handler.export_csv(sample_data, "/fake/export/folder", "Duration")

    # Retrieve the mock file handle to see what was "written"
    file_handle = mock_open.return_value
    # Collect all write calls
    write_calls = file_handle.write.call_args_list
    # Reconstruct the written content from all write() calls
    written_content = "".join(call.args[0] for call in write_calls)

    lines = written_content.splitlines()
    assert len(lines) == 3
    assert lines[0] == "Requirement;Test Case;Duration;Status"
    assert lines[1] == "R2;TC2;5.2;Failed"
    assert lines[2] == "R1;TC1;10.5;Passed"

    # Check the name of the file that would have been opened
    mock_open.assert_called_once_with(
        "/fake/export/folder/dummy_sorted_by_Duration.csv", 
        mode="w", 
        encoding="utf-8"
    )

def test_export_csv_file_write_error(sample_data, mocker):
    """
    Test-ID: D-T-CSV-EXC-003
    Verifies that a CSVExportError is raised when a file write error occurs.

    This test simulates an IOError during the file writing process in the
    export_csv method. It checks that the expected CSVExportError is raised
    in this scenario.

    Args:
        sample_data (Data): Fixture providing sample data for the test.
        mocker (pytest_mock.plugin.MockerFixture): Fixture for mocking objects.
    """
    csv_handler = CSVHandler("dummy.csv")

    # Simulate an error during file writing
    mock_open = mocker.mock_open()
    mock_open.side_effect = IOError("Mocked file write error")

    with pytest.raises(CSVExportError):
        with patch("builtins.open", mock_open):
            csv_handler.export_csv(sample_data, "/fake/export/folder", "Duration")

def test_log_review_lines(capsys, mock_logger):
    """
    Test-ID: D-T-CSV-LRV-001
    Verifies that the `_log_review_lines` method logs a warning and prints skipped lines to the console.

    Args:
        capsys (pytest.fixture): Fixture for capturing stdout and stderr.
        mock_logger (pytest.fixture): Fixture providing a mocked Logger instance.
    """

    csv_handler = CSVHandler("dummy.csv")  
    data = Data()
    data.review_lines = [
        (10, "Reason A"),
        (12, "Reason B"),
    ]

    csv_handler._log_review_lines(data)

    mock_logger.log_warning.assert_called_once_with(
        "2 lines were skipped. Detailed reasons: [(10, 'Reason A'), (12, 'Reason B')]"
    )

    captured = capsys.readouterr()
    assert "2 lines were skipped." in captured.out
    assert "  - Line 10 skipped: Reason A" in captured.out
    assert "  - Line 12 skipped: Reason B" in captured.out

def test_read_csv_valid_file(mocker):
    """
    Test-ID: D-T-CSV-RDC-001
    Verifies successful reading and parsing of a valid CSV file.

    This test checks that the read_csv method correctly reads a CSV file
    with valid header and data lines, parses the data, and populates the
    Data object accordingly. It uses a mocked file object to simulate the
    CSV content.

    Args:
        mocker (pytest_mock.plugin.MockerFixture): Fixture for mocking objects.
    """
    csv_content = (
        "Test case;Duration;Status\n"
        "R1\\TC1;10.5 sec;Passed\n"
        "R2\\TC2;5.2 min;Failed\n"
    )

    mock_open = mocker.mock_open(read_data=csv_content)
    mocker.patch("builtins.open", mock_open)
    mocker.patch("test_statistic_read_write.cli.os.path.isfile", return_value=True)

    csv_handler = CSVHandler("dummy.csv")
    data = csv_handler.read_csv()

    assert data.get_size() == 2
    assert data.data[1]["Requirement"] == "R1"
    assert data.data[1]["Test Case"] == "TC1"
    assert data.data[1]["Duration"] == 10.5
    assert data.data[1]["Status"] == "Passed"
    assert data.data[2]["Requirement"] == "R2"
    assert data.data[2]["Test Case"] == "TC2"
    assert data.data[2]["Duration"] == 312.0 # 5.2 min => 5.2 * 60 = 312.0
    assert data.data[2]["Status"] == "Failed"     

def test_read_csv_file_not_found():
    """
    Test-ID: D-T-CSV-RDC-002
    Verifies that an InputFileNotFound exception is raised for a non-existent file.

    This test checks that when the read_csv method is called with a
    non-existent file path, the expected InputFileNotFound exception is raised.

    """
    csv_handler = CSVHandler("nonexistent_file.csv")
    with pytest.raises(InputFileNotFound):
        csv_handler.read_csv()

def test_read_csv_empty_file(mocker):
    """
    Test-ID: D-T-CSV-RDC-003
    Verifies that an EmptyFileError is raised when reading an empty CSV file.

    This test checks that the read_csv method correctly raises an EmptyFileError
    when the input CSV file is empty. It uses a mocked file object to
    simulate an empty file.

    Args:
        mocker (pytest_mock.plugin.MockerFixture): Fixture for mocking objects.
    """
    csv_content = ""

    mock_open = mocker.mock_open(read_data=csv_content)
    mocker.patch("builtins.open", mock_open)
    mocker.patch("test_statistic_read_write.cli.os.path.isfile", return_value=True)

    csv_handler = CSVHandler("dummy.csv")
    with pytest.raises(EmptyFileError):
        csv_handler.read_csv()

def test_read_csv_invalid_header_columns(mocker):
    """
    Test-ID: D-T-CSV-RDC-004
    Verifies that an InvalidHeaderColumns exception is raised for an invalid header.

    This test checks that the read_csv method correctly raises an
    InvalidHeaderColumns exception when the input CSV file has a header
    with an incorrect number of columns. It uses a mocked file object to
    simulate the CSV content.

    Args:
        mocker (pytest_mock.plugin.MockerFixture): Fixture for mocking objects.
    """
    csv_content = "Test case;Duration\n"

    mock_open = mocker.mock_open(read_data=csv_content)
    mocker.patch("builtins.open", mock_open)
    mocker.patch("test_statistic_read_write.cli.os.path.isfile", return_value=True)

    csv_handler = CSVHandler("dummy.csv")

    with pytest.raises(InvalidHeaderColumns):
        csv_handler.read_csv()

def test_read_csv_invalid_header_format(mocker):
    """
    Test-ID: D-T-CSV-RDC-005
    Verifies that an InvalidHeaderFormat exception is raised for an invalid header format.

    This test checks that the read_csv method correctly raises an
    InvalidHeaderFormat exception when the input CSV file has a header
    with incorrect column names. It uses a mocked file object to
    simulate the CSV content.

    Args:
        mocker (pytest_mock.plugin.MockerFixture): Fixture for mocking objects.
    """
    csv_content = "Test;Duration;Status\n"  # Incorrect header name

    mock_open = mocker.mock_open(read_data=csv_content)
    mocker.patch("builtins.open", mock_open)
    mocker.patch("test_statistic_read_write.cli.os.path.isfile", return_value=True)

    csv_handler = CSVHandler("dummy.csv")

    with pytest.raises(InvalidHeaderFormat):
        csv_handler.read_csv()

def test_read_csv_no_data_lines(mocker):
    """
    Test-ID: D-T-CSV-RDC-006
    Verifies that a NoDataLinesError is raised for a CSV with no data lines.

    This test checks that the read_csv method correctly raises a NoDataLinesError
    when the input CSV file contains only a header row and no data lines.
    It uses a mocked file object to simulate the CSV content.

    Args:
        mocker (pytest_mock.plugin.MockerFixture): Fixture for mocking objects.
    """
    csv_content = "Test case;Duration;Status\n"
    mock_open = mocker.mock_open(read_data=csv_content)
    mocker.patch("builtins.open", mock_open)
    mocker.patch("test_statistic_read_write.cli.os.path.isfile", return_value=True)

    csv_handler = CSVHandler("dummy.csv")
    with pytest.raises(NoDataLinesError):
        csv_handler.read_csv()

def test_read_csv_no_valid_lines(mocker):
    """
    Test-ID: D-T-CSV-RDC-007
    Verifies that a NoValidLinesError is raised for a CSV with no valid lines.

    This test checks that the read_csv method correctly raises a NoValidLinesError
    when the input CSV file contains a valid header but all data lines
    are invalid (due to parsing errors in test case, duration, or status).
    It uses a mocked file object to simulate the CSV content.

    Args:
        mocker (pytest_mock.plugin.MockerFixture): Fixture for mocking objects.
    """
    csv_content = (
        "Test case;Duration;Status\n"
        "R1TC1;invalid;Passed\n"    # Invalid test case and duration
        "R2TC2;10.5 sec;Invalid\n"  # Invalid test case
    )

    mock_open = mocker.mock_open(read_data=csv_content)
    mocker.patch("builtins.open", mock_open)
    mocker.patch("test_statistic_read_write.cli.os.path.isfile", return_value=True)

    csv_handler = CSVHandler("dummy.csv")
    with pytest.raises(NoValidLinesError):
        csv_handler.read_csv()

def test_read_csv_skip_lines_with_incorrect_number_of_columns(mocker):
    """
    Test-ID: D-T-CSV-RDC-008
    Verifies that lines with incorrect column count are skipped and logged.

    This test checks that the read_csv method correctly skips lines with
    an incorrect number of columns and records them in the review_lines
    list of the Data object. It uses a mocked file object to simulate the
    CSV content.

    Args:
        mocker (pytest_mock.plugin.MockerFixture): Fixture for mocking objects.
    """
    csv_content = (
        "Test case;Duration;Status\n"
        "R1\\TC1;10.5 sec;Passed\n"
        "R2\\TC2;5.2 min\n"         # Incorrect number of columns
        "R3\\TC3;2 min;Failed\n"
    )
    mock_open = mocker.mock_open(read_data=csv_content)
    mocker.patch("builtins.open", mock_open)
    mocker.patch("test_statistic_read_write.cli.os.path.isfile", return_value=True)

    csv_handler = CSVHandler("dummy.csv")
    data = csv_handler.read_csv()

    assert data.get_size() == 2
    assert len(data.review_lines) == 1
    assert data.review_lines[0][0] == 3
    assert data.review_lines[0][1] == "2 columns instead of 3"

def test_read_csv_skip_lines_with_empty_fields(mocker):
    """
    Test-ID: D-T-CSV-RDC-009
    Verifies that lines with empty fields are skipped and logged.

    This test checks that the read_csv method correctly skips lines with
    empty fields and records them in the review_lines list of the Data
    object. It uses a mocked file object to simulate the CSV content.

    Args:
        mocker (pytest_mock.plugin.MockerFixture): Fixture for mocking objects.
    """
    csv_content = (
        "Test case;Duration;Status\n"
        "R1\\TC1;10.5 sec;Passed\n"
        "R2\\TC2;;Failed\n"         # Empty duration
        "R3\\TC3;2 min;Failed\n"
    )

    mock_open = mocker.mock_open(read_data=csv_content)
    mocker.patch("builtins.open", mock_open)
    mocker.patch("test_statistic_read_write.cli.os.path.isfile", return_value=True)

    csv_handler = CSVHandler("dummy.csv")
    data = csv_handler.read_csv()

    assert data.get_size() == 2
    assert len(data.review_lines) == 1
    assert data.review_lines[0][0] == 3
    assert data.review_lines[0][1] == "Empty field"

def test_read_csv_skip_lines_with_parse_errors(mocker):
    """
    Test-ID: D-T-CSV-RDC-010
    Verifies that lines with parsing errors are skipped and logged.

    This test checks that the read_csv method correctly skips lines with
    parsing errors (invalid test case, duration, or status format) and
    records them in the review_lines list of the Data object. It uses a
    mocked file object to simulate the CSV content.

    Args:
        mocker (pytest_mock.plugin.MockerFixture): Fixture for mocking objects.
    """
    csv_content = (
        "Test case;Duration;Status\n"
        "R1\\TC1;10.5 sec;Passed\n"
        "R2TC2;5.2 min;Failed\n"    # Invalid test case format
        "R3\\TC3;invalid;Failed\n"  # Invalid duration
        "R5\\TC5;1 min;Passed\n"
    )

    mock_open = mocker.mock_open(read_data=csv_content)
    mocker.patch("builtins.open", mock_open)
    mocker.patch("test_statistic_read_write.cli.os.path.isfile", return_value=True)

    csv_handler = CSVHandler("dummy.csv")
    data = csv_handler.read_csv()

    assert data.get_size() == 2
    assert len(data.review_lines) == 2
    assert data.review_lines[0][0] == 3
    assert data.review_lines[0][1] == "Test case parse error. Invalid value: 'R2TC2'"
    assert data.review_lines[1][0] == 4
    assert data.review_lines[1][1] == "Duration parse error. Invalid value: 'invalid'"

def test_read_csv_status_parser_returns_none(mock_logger, mocker):
    """
    Test-ID: D-T-CSV-RDC-011
    Verifies that a line is skipped and logged if StatusParser returns None.

    This test checks that if the StatusParser.parse method returns None
    for a specific status value, the corresponding line is skipped during
    CSV reading, a warning message is logged, and the line information is
    recorded in the review_lines list of the Data object.

    Args:
        mock_logger: A mock of the Logger object.
        mocker (pytest_mock.plugin.MockerFixture): Fixture for mocking objects.
    """

    csv_content = (
        "Test case;Duration;Status\n"
        "R1\\TC1;10.5 sec;GoodStatus\n"
        "R1\\TC2;5.2 min;BadStatus\n"
    )
    mock_open = mocker.mock_open(read_data=csv_content)
    csv_handler = CSVHandler("dummy.csv")  

    mocker.patch.object(csv_handler.parsers.get("Status"), 'parse', side_effect=lambda x: None if x == "BadStatus" else x.strip())
    mocker.patch.object(csv_handler.parsers.get("Test Case"), 'parse', return_value={"Requirement": "R1", "Test Case": "TC1"})
    mocker.patch.object(csv_handler.parsers.get("Duration"), 'parse', return_value=10.5)

    mocker.patch("builtins.open", mock_open)  # Status that triggers None return
    mocker.patch("test_statistic_read_write.cli.os.path.isfile", return_value=True)

    data = csv_handler.read_csv()

    # 1. Check that the warning was logged for the correct line
    mock_logger.log_warning.assert_any_call('CSVHandler: Status parsing error at line 3, skipping.')
    mock_logger.log_warning.assert_any_call('1 lines were skipped. Detailed reasons: [(3, "Status parse error. Invalid value: \'BadStatus\'")]')
    
    # 2. Check that the correct line was added to review_lines
    assert len(data.review_lines) == 1
    assert data.review_lines[0][0] == 3  # Line number 3
    assert data.review_lines[0][1] == "Status parse error. Invalid value: 'BadStatus'"

    # 3. Check that only the line with "GoodStatus" was added
    assert data.get_size() == 1
    assert data.data[1]["Status"] == "GoodStatus"  