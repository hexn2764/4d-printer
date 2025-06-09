# Test Specification: D-T-CSV-RDC-010

**Test ID:** D-T-CSV-RDC-010

**Test Name:** CSV Handler - Read CSV Skip Lines With Parse Errors

**Source:** Developer

**Module:** CSV Handler

**Category:** Read CSV

**Related Requirements:**

*   D-1
*   D-3
*   D-4
*   D-21

**Purpose:**
This test verifies that the `CSVHandler.read_csv()` method correctly handles lines with parsing errors in the input CSV file. It checks that such lines are skipped during the parsing process, that appropriate information about the skipped lines, including the specific parsing error, is recorded in the `review_lines` list of the `Data` object, and that a warning message is logged for each skipped line.

**Preconditions:**

*   1) The `builtins.open` function is mocked using `mocker.mock_open` to simulate reading from a file with the specified `csv_content`.
*   2) The `os.path.isfile` function is mocked to always return `True`.

**Test Data:**

*   `csv_content`: A string representing the content of a CSV file with lines containing parsing errors:
    ```csv
    Test case;Duration;Status
    R1\\TC1;10.5 sec;Passed
    R2TC2;5.2 min;Failed
    R3\\TC3;invalid;Failed
    R5\\TC5;1 min;Passed
    ```

**Test Steps:**

1.  Create a mock file object using `mocker.mock_open` with the `csv_content`.
2.  Patch `builtins.open` to return the mock file object.
3.  Patch `os.path.isfile` to always return `True`.
4.  Create an instance of `CSVHandler` with a dummy file path ("dummy.csv").
5.  Call `csv_handler.read_csv()`.

**Expected Results:**

*   1) The `Data` object returned by `read_csv()` should contain 2 valid entries.
*   2) The `Data` object's `review_lines` list should contain 2 entries.
*   3) The first entry in `review_lines` should indicate that line 3 was skipped due to a test case parsing error with the invalid value 'R2TC2'.
*   4) The second entry in `review_lines` should indicate that line 4 was skipped due to a duration parsing error with the invalid value 'invalid'.

**Assertions:**

*   `assert data.get_size() == 2`: Asserts that the `Data` object contains 2 valid entries.
*   `assert len(data.review_lines) == 2`: Asserts that the `review_lines` list contains 2 entries.
*   `assert data.review_lines[0][0] == 3`: Asserts that the line number of the first skipped line is 3.
*   `assert data.review_lines[0][1] == "Test case parse error. Invalid value: 'R2TC2'"`: Asserts that the reason for skipping the first line, including the specific error and invalid value, is recorded correctly.
*   `assert data.review_lines[1][0] == 4`: Asserts that the line number of the second skipped line is 4.
*   `assert data.review_lines[1][1] == "Duration parse error. Invalid value: 'invalid'"`: Asserts that the reason for skipping the second line, including the specific error and invalid value, is recorded correctly.

**Postconditions:**

*   The `Data` object is populated with the valid data read from the mocked CSV file.
*   Information about the skipped lines with parsing errors is recorded in `review_lines`.
*   Warning messages are logged for each skipped line.

**Test Code:** `test_csv_handler.py::test_read_csv_skip_lines_with_parse_errors`

**Status:** Pass

**Notes:**

*   This test relies on the `pytest` framework and the `pytest-mock` plugin (`mocker` fixture).
*   The test uses a mocked file object to isolate the `read_csv` method from the actual file system.
*   The test data includes lines with invalid test case and duration values to test the error handling logic.
*   The test assumes that the parsing logic in `TestCaseParser` and `DurationParser` correctly identifies and returns `None` for invalid values, leading to the corresponding error messages being recorded.
