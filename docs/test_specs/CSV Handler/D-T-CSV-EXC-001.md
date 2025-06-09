# Test Specification: D-T-CSV-EXC-001

**Test ID:** D-T-CSV-EXC-001

**Test Name:** CSV Handler - Export CSV Valid

**Source:** Developer

**Module:** CSV Handler

**Category:** Export

**Related Requirements:**

*   D-19
*   D-20
*   D-21

**Purpose:**
This test verifies that the `CSVHandler.export_csv()` method correctly exports data to a CSV file, including the header row and sorted data rows, when provided with valid data and a valid sorting key. It also ensures that the correct filename is used for the exported file, incorporating the original filename and the sorting key.

**Preconditions:**

*   1) The `builtins.open` function is mocked using `mocker.mock_open` to simulate file writing without actual file system interaction.
*   2) A `Data` object named `sample_data` is available (provided as a fixture), containing at least two entries suitable for export (see Test Data below).
*    The `sample_data` should have pre-calculated sorting order for the 'Duration' key.

**Test Data:**

*   `sample_data`: A `Data` object containing at least the following entries (implied by assertions):
    *   Entry 1:
        *   Requirement: "R1"
        *   Test Case: "TC1"
        *   Duration: 10.5
        *   Status: "Passed"
    *   Entry 2:
        *   Requirement: "R2"
        *   Test Case: "TC2"
        *   Duration: 5.2
        *   Status: "Failed"
*   `export_folder`: "/fake/export/folder" (a string representing a fake folder path for export)
*   `sort_key`: "Duration" (a string representing the sorting key)

**Test Steps:**

1.  Create a mock file object using `mocker.mock_open`.
2.  Patch `builtins.open` to return the mock file object.
3.  Create an instance of `CSVHandler` with a dummy file path ("dummy.csv").
4.  Call `csv_handler.export_csv()` with the `sample_data`, `export_folder`, and `sort_key`.

**Expected Results:**

*   1) The `write` method of the mocked file object should be called multiple times to write the header and data rows.
*   2) The content written to the mocked file should correspond to a valid CSV structure with a header row ("Requirement;Test Case;Duration;Status") and data rows sorted by "Duration" in ascending order.
*   3) The `open` function should be called once with the correct filename, mode, and encoding.

**Assertions:**

*   `assert len(lines) == 3`: Asserts that 3 lines were written (header + 2 data rows).
*   `assert lines[0] == "Requirement;Test Case;Duration;Status"`: Asserts the content of the header row.
*   `assert lines[1] == "R2;TC2;5.2;Failed"`: Asserts the content of the first data row (sorted by Duration).
*   `assert lines[2] == "R1;TC1;10.5;Passed"`: Asserts the content of the second data row (sorted by Duration).
*   `mock_open.assert_called_once_with("/fake/export/folder/dummy_sorted_by_Duration.csv", mode="w", encoding="utf-8")`: Asserts that `open` was called with the correct filename, write mode, and UTF-8 encoding.

**Postconditions:**

*   No actual files are created or modified on the file system.
*   The content that would have been written to the CSV file is captured by the mocked file object.

**Test Code:** `test_csv_handler.py::test_export_csv_valid`

**Status:** Pass

**Notes:**

*   This test relies on the `pytest` framework, the `pytest-mock` plugin (`mocker` fixture), and a `sample_data` fixture that provides a `Data` object.
*   The test uses a mocked file object to isolate the `export_csv` method from the actual file system, making it a unit test.
