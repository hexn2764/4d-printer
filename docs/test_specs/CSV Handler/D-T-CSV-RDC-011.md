# Test Specification: D-T-CSV-RDC-011

**Test ID:** D-T-CSV-RDC-011

**Test Name:** CSV Handler - Read CSV Status Parser Returns None

**Source:** Developer

**Module:** CSV Handler

**Category:** Read CSV

**Related Requirements:**

*   D-1
*   D-3
*   D-4
*   D-21

**Purpose:**
This test verifies that the `CSVHandler.read_csv()` method correctly handles the case where the `StatusParser.parse()` method returns `None` for a particular line in the input CSV file. It checks that the line is skipped, a warning message is logged, and information about the skipped line is recorded in the `review_lines` list of the `Data` object.

**Preconditions:**

*   1) The `builtins.open` function is mocked using `mocker.mock_open` to simulate reading from a file with the specified `csv_content`.
*   2) The `os.path.isfile` function is mocked to always return `True`.
*   3) The `csv_handler.parsers.get("Status")` is mocked to return `None` when its `parse` method is called with "BadStatus" and returns the stripped input otherwise.
*   4) The `csv_handler.parsers.get("Test Case")` is mocked to return a valid dictionary `{"Requirement": "R1", "Test Case": "TC1"}` when its `parse` method is called.
*   5) The `csv_handler.parsers.get("Duration")` is mocked to return a valid duration `10.5` when its `parse` method is called.
*   6) The `Logger` object is mocked to capture log messages (using `mock_logger` fixture).

**Test Data:**

*   `csv_content`: A string representing the content of a CSV file:
    ```csv
    Test case;Duration;Status
    R1\\TC1;10.5 sec;GoodStatus
    R1\\TC2;5.2 min;BadStatus
    ```

**Test Steps:**

1.  Create a mock file object using `mocker.mock_open` with the `csv_content`.
2.  Create an instance of `CSVHandler` with a dummy file path ("dummy.csv").
3.  Patch the `parse` methods of `csv_handler.parsers` as described in the Preconditions.
4.  Patch `builtins.open` to return the mock file object.
5.  Patch `os.path.isfile` to always return `True`.
6.  Call `csv_handler.read_csv()`.

**Expected Results:**

*   1) The `mock_logger.log_warning` method should be called at least once. One of the calls should contain the message: "CSVHandler: Status parsing error at line 3, skipping."
*   2) The `mock_logger.log_warning` method should be called with a message that contains the text: "1 lines were skipped. Detailed reasons: \[(3, \"Status parse error. Invalid value: 'BadStatus'\")]"
*   3) The `Data` object returned by `read_csv()` should have a `review_lines` list containing one entry.
*   4) The entry in `review_lines` should indicate that line 3 was skipped due to a status parsing error with the invalid value 'BadStatus'.
*   5) The `Data` object should contain 1 entry with status "GoodStatus".

**Assertions:**

*   `mock_logger.log_warning.assert_any_call('CSVHandler: Status parsing error at line 3, skipping.')`: Asserts that a warning message was logged for line 3.
*   `mock_logger.log_warning.assert_any_call('1 lines were skipped. Detailed reasons: [(3, "Status parse error. Invalid value: \'BadStatus\'")]')` : Asserts the summary warning message for skipped lines was logged.
*   `assert len(data.review_lines) == 1`: Asserts that the `review_lines` list contains one entry.
*   `assert data.review_lines[0][0] == 3`: Asserts that the line number of the skipped line is 3.
*   `assert data.review_lines[0][1] == "Status parse error. Invalid value: 'BadStatus'"`: Asserts that the reason for skipping the line, including the specific error and invalid value, is recorded correctly.
*   `assert data.get_size() == 1`: Asserts that the `Data` object contains one entry.
*   `assert data.data[1]["Status"] == "GoodStatus"`: Asserts that the status of the valid entry is "GoodStatus".

**Postconditions:**

*   The `Data` object contains the valid data from the mocked CSV file.
*   Information about the skipped line (where `StatusParser` returned `None`) is recorded in `review_lines`.
*   Warning messages have been logged indicating the skipped line and a summary.

**Test Code:** `test_csv_handler.py::test_read_csv_status_parser_returns_none`

**Status:** Pass

**Notes:**

*   This test relies on the `pytest` framework, the `pytest-mock` plugin (`mocker` fixture), and a mocked `Logger` object.
*   The test uses a mocked file object and mocks the parser methods to isolate the `read_csv` method from the actual file system and parser implementations.
*   The test assumes that `StatusParser`, `TestCaseParser`, and `DurationParser` are classes with a `parse` method.
*   Note: currently, `StatusParser` parses everything and cannot return `None`. This test is made for the coverage.
