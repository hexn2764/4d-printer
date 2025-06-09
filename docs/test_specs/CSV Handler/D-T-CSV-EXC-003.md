# Test Specification: D-T-CSV-EXC-003

**Test ID:** D-T-CSV-EXC-003

**Test Name:** CSV Handler - Export CSV File Write Error

**Source:** Developer

**Module:** CSV Handler

**Category:** Export CSV

**Related Requirements:**

*   D-19
*   D-20
*   D-21
*   D-22

**Purpose:**
This test verifies that the `CSVHandler.export_csv()` method correctly raises a `CSVExportError` exception when an error occurs during the file writing process.

**Preconditions:**

*   1) A `Data` object named `sample_data` is available (provided as a fixture).

**Test Data:**

*   `sample_data`: A `Data` object (the content is not relevant for this test, but it should be in a valid state for export).
*   `export_folder`: "/fake/export/folder" (a string representing a fake folder path).
*   `sort_key`: "Duration" (a string representing the sorting key, although not directly relevant to the error scenario).

**Test Steps:**

1.  Create an instance of `CSVHandler` with a dummy file path ("dummy.csv").
2.  Create a mock file object using `mocker.mock_open` and set its `side_effect` to `IOError("Mocked file write error")` to simulate a file write error.
3.  Patch `builtins.open` with the mock file object using `with patch(...)`.
4.  Call `csv_handler.export_csv()` with `sample_data`, `export_folder`, and `sort_key` within a `pytest.raises(CSVExportError)` context.

**Expected Results:**

*   1) The `csv_handler.export_csv()` method should raise a `CSVExportError` exception.

**Assertions:**

*   `with pytest.raises(CSVExportError):`: Asserts that a `CSVExportError` exception is raised.

**Postconditions:**

*   No actual files are created or modified on the file system.

**Test Code:** `test_csv_handler.py::test_export_csv_file_write_error`

**Status:** Pass

**Notes:**

*   This test relies on the `pytest` framework, the `pytest-mock` plugin (`mocker` fixture), a `sample_data` fixture.
*   The test uses a mocked file object with a side effect to simulate a file write error, isolating the test from the actual file system.
*   The test verifies the correct handling of a file system error during CSV export by checking for the expected exception.
