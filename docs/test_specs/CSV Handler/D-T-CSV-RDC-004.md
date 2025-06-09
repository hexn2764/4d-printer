# Test Specification: D-T-CSV-RDC-004

**Test ID:** D-T-CSV-RDC-004

**Test Name:** CSV Handler - Read CSV Invalid Header Columns

**Source:** Developer

**Module:** CSV Handler

**Category:** Read CSV

**Related Requirements:**

*   D-1
*   D-3
*   D-21
*   D-22

**Purpose:**
This test verifies that the `CSVHandler.read_csv()` method correctly raises an `InvalidHeaderColumns` exception when the input CSV file has a header row with an incorrect number of columns (not equal to 3).

**Preconditions:**

*   1) The `builtins.open` function is mocked using `mocker.mock_open` to simulate reading from a file with the specified `csv_content`.
*   2) The `os.path.isfile` function is mocked to always return `True`.

**Test Data:**

*   `csv_content`: A string representing the content of a CSV file with an invalid header:
    ```csv
    Test case;Duration
    ```

**Test Steps:**

1.  Create a mock file object using `mocker.mock_open` with the `csv_content`.
2.  Patch `builtins.open` to return the mock file object.
3.  Patch `os.path.isfile` to always return `True`.
4.  Create an instance of `CSVHandler` with a dummy file path ("dummy.csv").
5.  Call `csv_handler.read_csv()` within a `pytest.raises(InvalidHeaderColumns)` context.

**Expected Results:**

*   1) The `csv_handler.read_csv()` method should raise an `InvalidHeaderColumns` exception.

**Assertions:**

*   `with pytest.raises(InvalidHeaderColumns):`: Asserts that an `InvalidHeaderColumns` exception is raised.

**Postconditions:**

*   No files are created or modified on the file system.

**Test Code:** `test_csv_handler.py::test_read_csv_invalid_header_columns`

**Status:** Pass

**Notes:**

*   This test relies on the `pytest` framework and the `pytest-mock` plugin (`mocker` fixture).
*   The test uses a mocked file object to isolate the `read_csv` method from the actual file system.
*   The test assumes that `InvalidHeaderColumns` is a custom exception defined in the `_exceptions.py` file.
