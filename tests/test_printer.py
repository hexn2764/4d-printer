# tests/test_printer.py

import pytest
from test_statistic_read_write._printer import Printer
from typing import List, Tuple, Dict, Any
import re

@pytest.fixture
def printer():
    """Returns a new Printer instance for testing."""
    return Printer()

def test_do_advanced_output(printer, capsys):
    """
    Test-ID: D-T-PRI-DAO-001
    Directly tests the `do_advanced_output` method with sample entries.

    Verifies that the method produces a formatted table output with:
        - A header row with correct column names and spacing.
        - A separator row with the correct number of dashes.
        - Data rows with correctly formatted values, according to specified pattern.

    Args:
        printer (Printer): The `Printer` fixture.
        capsys (pytest.fixture): Fixture for capturing stdout and stderr.
    """
    top_entries = [
        (1, {"Requirement": "REQ-A", "Test Case": "TC-Alpha", "Duration": 2.345, "Status": "Passed"}),
        (2, {"Requirement": "XYZ",    "Test Case": "TC-LongName", "Duration": 123.456, "Status": "Skipped"}),
    ]

    printer.do_advanced_output(top_entries)

    captured = capsys.readouterr()
    out = captured.out

    out_lines = out.splitlines()
    header_line = out_lines[0]

    pad = " "
    padding = 5
    fill = pad*padding
    extra_1 = len("TC-LongName") - len("Test Case")
    extra_2 = len("Skipped") - len("Status")
    expected_header = "ID" + fill + "Requirement" + fill + "Test Case" + extra_1*pad + fill + "Duration (sec)" + fill + "Status" + fill + extra_2*pad

    assert expected_header in header_line
    assert "-"*(len(expected_header)) in out
    assert "-"*(len(expected_header) + 1) not in out

    # can be calculated exactly, but we check the regex to abstract from left/right alignment and spacing,
    # as both can be changed during the development
    # first line
    pattern = r"1\.\s+REQ-A\s+TC-Alpha\s+2\.345\s+Passed\s+\n"
    match = re.search(pattern, out)
    assert match is not None, "The line '1. REQ-A TC-Alpha 2.345 Passed' was not found."

    # second line
    pattern = r"2\.\s+XYZ\s+TC-LongName\s+123\.456\s+Skipped\s+\n"
    match = re.search(pattern, out)
    assert match is not None, "The line '2. XYZ TC-LongName 123.456 Skipped' was not found."

def test_do_basic_output(printer, capsys):
    """
    Test-ID: D-T-PRI-DBO-001
    Directly tests the `do_basic_output` method with sample entries.

    Verifies that the method produces a basic, non-tabular output with each entry's information
    (Requirement, Test Case, Duration, Status) on a separate line.

    Args:
        printer (Printer): The `Printer` fixture.
        capsys (pytest.fixture): Fixture for capturing stdout and stderr.
    """
    top_entries = [
        (10, {"Requirement": "R1", "Test Case": "TC1", "Duration": 3.14,  "Status": "Passed"}),
        (11, {"Requirement": "R2", "Test Case": "TC2", "Duration": 99.999,"Status": "Failed"})
    ]

    printer.do_basic_output(top_entries)
    captured = capsys.readouterr()
    out = captured.out

    assert "1. Requirement: R1, Test Case: TC1, Duration: 3.140 sec, Status: Passed" in out
    assert "2. Requirement: R2, Test Case: TC2, Duration: 99.999 sec, Status: Failed" in out

def test_display_results_with_formatting(printer, capsys):
    """
    Test-ID: D-T-PRI-DRF-001
    Tests the `display_results` method with entries and `formatting=True`.

    Verifies that:
        - The output includes the total duration.
        - The output includes a "Top X" entries section header.
        - The output includes a formatted table with a header row, a separator row, and data rows.
        - The output table has the correct columns and spacing.
        - The output table rows are correctly formatted according to the specified pattern.

    Args:
        printer (Printer): The `Printer` fixture.
        capsys (pytest.fixture): Fixture for capturing stdout and stderr.
    """
    analysis = {
        "total_duration": 45.678,
        "top_x_entries": [
            (1, {"Requirement": "REQ-A", "Test Case": "TC1", "Duration": 10.0, "Status": "Passed"}),
            (2, {"Requirement": "REQ-B", "Test Case": "TC2", "Duration": 35.678, "Status": "Failed"})
        ],
        "test_case_counts": (20, 18, 2),  # 20 total, 18 parsed, 2 skipped
        "status_counts": {"Pass": 9, "Fail": 6, "Blocked": 3}, 
    }

    printer.display_results(analysis, formatting=True)
    captured = capsys.readouterr()
    out = captured.out

    assert "\nTotal Duration: 45.678 Seconds.\n" in out
    assert "Total Amount of Cases: 20 (18 Parsed, 2 Skipped)." in out
    assert "Status Counts" in out
    assert "Pass: 9" in out
    assert "Fail: 6" in out
    assert "Blocked: 3" in out

    assert "Top 2 (Longest Tests):\n" in out

    out_lines = out.splitlines()
    header_line = out_lines[9]

    pad = " "
    padding = 5
    fill = pad*padding
    expected_header = "ID" + fill + "Requirement" + fill + "Test Case" + fill + "Duration (sec)" + fill + "Status" + fill

    assert expected_header == header_line
    assert "-"*(len(expected_header)) in out
    assert "-"*(len(expected_header)+1) not in out

    # can be calculated exactly, but we check the regex to abstract from left/right alignment and spacing,
    # as both can be changed during the development
    # first line
    pattern = r"1\.\s+REQ-A\s+TC1\s+10\.000\s+Passed\s+"
    match = re.search(pattern, out)
    assert match is not None, "The line '1. REQ-A TC1 10.000 Passed' was not found."

    # second line
    pattern = r"2\.\s+REQ-B\s+TC2\s+35\.678\s+Failed\s+"
    match = re.search(pattern, out)
    assert match is not None, "The line '2. REQ-B TC2 35.678 Failed' was not found."

def test_display_results_no_entries(printer, capsys):
    """
    Test-ID: D-T-PRI-DRN-001
    Tests the `display_results` method with an empty `top_x_entries` list
    and dummy values for test_case_counts and status_counts.

    Verifies that the method prints the total duration, total test cases,
    status counts, but does not attempt to print a "Top X" entries section
    when there are no entries to display.

    Args:
        printer (Printer): The `Printer` fixture.
        capsys (pytest.fixture): Fixture for capturing stdout and stderr.
    """
    analysis = {
        "total_duration": 12.345,
        "top_x_entries": [],
        "test_case_counts": (15, 12, 3),  # 15 total, 12 parsed, 3 skipped
        "status_counts": {"Pass": 8, "Fail": 4}, 
    }

    printer.display_results(analysis, formatting=True)

    captured = capsys.readouterr()
    out = captured.out

    assert "Total Duration: 12.345 Seconds." in out
    assert "Total Amount of Cases: 15 (12 Parsed, 3 Skipped)." in out
    assert "Status Counts (Parsed Cases Only):" in out
    assert "Pass: 8" in out
    assert "Fail: 4" in out

    assert "Top" not in out

def test_display_results_no_formatting(printer, capsys):
    """
    Test-ID: D-T-PRI-DRN-002
    Tests the `display_results` method with entries and `formatting=False`.

    Verifies that:
        - The output includes the total duration.
        - The output includes a "Top X" entries section header.
        - The output includes the top entries in a basic, non-tabular format.
        - The output includes the total test case counts.
        - The output includes the status counts.

    Args:
        printer (Printer): The `Printer` fixture.
        capsys (pytest.fixture): Fixture for capturing stdout and stderr.
    """
    analysis = {
        "total_duration": 88.999,
        "top_x_entries": [
            (10, {"Requirement": "REQ-X", "Test Case": "TestCaseX", "Duration": 60.5, "Status": "Passed"}),
            (11, {"Requirement": "REQ-Y", "Test Case": "TestCaseY", "Duration": 28.4999, "Status": "Failed"})
        ],
        "test_case_counts": (50, 45, 5),  # 50 total, 45 parsed, 5 skipped
        "status_counts": {"Pass": 25, "Fail": 15, "Blocked": 5},
    }

    printer.display_results(analysis, formatting=False)
    captured = capsys.readouterr()
    out = captured.out

    assert "\nTotal Duration: 88.999 Seconds.\n" in out
    assert "Total Amount of Cases: 50 (45 Parsed, 5 Skipped)." in out
    assert "Status Counts" in out
    assert "Pass: 25" in out
    assert "Fail: 15" in out
    assert "Blocked: 5" in out
    assert "Top 2 (Longest Tests):\n" in out
    assert "1. Requirement: REQ-X, Test Case: TestCaseX, Duration: 60.500 sec, Status: Passed" in out
    assert "2. Requirement: REQ-Y, Test Case: TestCaseY, Duration: 28.500 sec, Status: Failed" in out


def test_get_width(printer):
    """
    Test-ID: D-T-PRI-GWD-001
    Tests the `get_width` method with multiple sample entries.

    Verifies that the method correctly calculates the required width for each column
    based on the header lengths and the maximum length of the data in each column,
    plus additional padding.

    Args:
        printer (Printer): The `Printer` fixture.
    """
    top_entries = [
        (1, {"Requirement": "ABC",  "Test Case": "X",    "Duration": 15.1234, "Status": "Pass"}),
        (2, {"Requirement": "LongReq", "Test Case": "XXY", "Duration": 999.5,  "Status": "FailedTest"})
    ]
    headers = ["ID", "Requirement", "Test Case", "Duration (sec)", "Status"]

    widths = printer.get_width(top_entries, headers)

    pad_length = 5
    assert widths[0] == len("ID") + pad_length, f"ID column wrong length: {widths[0]}"
    assert widths[1] == len("Requirement") + pad_length, f"Requirement column wrong length: {widths[1]}"
    assert widths[2] == len("Test Case") + pad_length, f"TestCase column wrong length: {widths[2]}"
    assert widths[3] == len("Duration (sec)") + pad_length, f"Duration column wrong length: {widths[3]}"
    assert widths[4] == len("FailedTest") + pad_length, f"Status column wrong length: {widths[4]}"

def test_get_width_empty_data(printer):
    """
    Test-ID: D-T-PRI-GWE-001
    Tests the `get_width` method with an empty data list.

    Verifies that the method correctly calculates the column widths based only on header lengths
    when there is no data in the `top_entries` list.

    Args:
        printer (Printer): The `Printer` fixture.
    """
    headers = ["ID", "Requirement", "Test Case", "Duration (sec)", "Status"]
    widths = printer.get_width([], headers)
    padding = 5
    assert widths == [len(header) + padding for header in headers]

def test_get_width_with_longer_data_values(printer):
    """
    Test-ID: D-T-PRI-GWL-001
    Tests the `get_width` method with data values longer than header lengths.

    Verifies that the method correctly calculates the required width for each column when
    the data values are longer than the corresponding header lengths.

    Args:
        printer (Printer): The `Printer` fixture.
    """
    headers = ["ID", "Requirement", "Test Case", "Duration", "Status"]
    top_entries: List[Tuple[int, Dict[str, Any]]] = [
        (1, {"Requirement": "LongerRequirement", "Test Case": "LongerTestCaseName", "Duration": 1234567.89123456789, "Status": "LongerStatus"}),
        (100, {"Requirement": "Short", "Test Case": "TC", "Duration": 1.0, "Status": "S"})
    ]
    widths = printer.get_width(top_entries, headers)
    
    padding = 5
    dot = 1
    precision = 3

    expected_id_width = len("100.") + padding  
    expected_req_width = len("LongerRequirement") + padding 
    expected_tc_width = len("LongerTestCaseName") + padding  
    expected_dur_width = len("1234567") + dot + precision  + padding 
    expected_stat_width = len("LongerStatus") + padding  

    assert widths == [expected_id_width, expected_req_width, expected_tc_width, expected_dur_width, expected_stat_width]

