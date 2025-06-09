# Test Specification: D-T-CSV-RDC-002

**Test ID:** D-T-CSV-RDC-002

**Test Name:** CSV Handler - Read CSV File Not Found

**Source:** Developer

**Module:** CSV Handler

**Category:** Read CSV

**Related Requirements:**

*   D-1
*   D-2
*   D-21
*   D-22

**Purpose:**
This test verifies that the `CSVHandler.read_csv()` method correctly raises an `InputFileNotFound` exception when the specified input CSV file does not exist.

**Preconditions:**

*   1) The file "nonexistent_file.csv" does not exist in the file system.

**Test Data:**

*   `csv_path`: "nonexistent_file.csv" (a string representing the path to a non-existent file)

**Test Steps:**

1.  Create an instance of `CSVHandler` with the `csv_path` ("nonexistent_file.csv").
2.  Create an instance of `Data`.
3.  Call `csv_handler.read_csv()` with the `Data` object within a `pytest.raises(InputFileNotFound)` context.

**Expected Results:**

*   1) The `csv_handler.read_csv()` method should raise an `InputFileNotFound` exception.

**Assertions:**

*   `with pytest.raises(InputFileNotFound):`: Asserts that an `InputFileNotFound` exception is raised.

**Postconditions:**

*   No files are created or modified on the file system.

**Test Code:** `test_csv_handler.py::test_read_csv_file_not_found`

**Status:** Pass

**Notes:**

*   This test relies on the `pytest` framework.
*   The test does not use mocking because it intends to test the actual file system interaction and exception handling.
*   The test assumes that `InputFileNotFound` is a custom exception defined in the `_exceptions.py` file.
