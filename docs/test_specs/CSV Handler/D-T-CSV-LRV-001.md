# Test Specification: D-T-CSV-LRV-001

**Test ID:** D-T-CSV-LRV-001

**Test Name:** CSV Handler - Log Review Lines

**Source:** Developer

**Module:** CSV Handler

**Category:** Logging

**Related Requirements:**

*   D-8
*   D-21
*   D-23

**Purpose:**
This test verifies that the `CSVHandler._log_review_lines` method correctly logs a warning message with the number of skipped lines and their reasons to the logger and prints detailed information about the skipped lines to the console.

**Preconditions:**

*   1) A `CSVHandler` object is instantiated with a dummy CSV file path.
*   2) A `Data` object is instantiated.
*   3) The `Data` object's `review_lines` attribute is populated with a list of tuples, where each tuple represents a skipped line and its reason: `[(10, "Reason A"), (12, "Reason B")]`.
*   4) The `Logger` object is mocked to track its method invocations.

**Test Data:**

*   `review_lines`: `[(10, "Reason A"), (12, "Reason B")]`

**Test Steps:**

1.  Create a `CSVHandler` object with a dummy CSV file path.
2.  Create a `Data` object.
3.  Populate the `data.review_lines` with the test data.
4.  Call the `_log_review_lines` method of the `CSVHandler` object, passing the `Data` object as an argument.
5.  Capture stdout and stderr using `capsys`.

**Expected Results:**

*   1) The `Logger.log_warning` method should be called exactly once.
*   2) The argument passed to `Logger.log_warning` should be "2 lines were skipped. Detailed reasons: `[(10, 'Reason A'), (12, 'Reason B')]`".
*   3) Stdout should contain the string "2 lines were skipped.".
*   4) Stdout should contain the string "  - Line 10 skipped: Reason A".
*   5) Stdout should contain the string "  - Line 12 skipped: Reason B".

**Assertions:**

*   `mock_logger.log_warning.assert_called_once_with("2 lines were skipped. Detailed reasons: [(10, 'Reason A'), (12, 'Reason B')]")`: Asserts that `Logger.log_warning` was called once with the expected message.
*   `assert "2 lines were skipped." in captured.out`: Asserts that the summary message is printed to stdout.
*   `assert "  - Line 10 skipped: Reason A" in captured.out`: Asserts that the detailed reason for the first skipped line is printed to stdout.
*   `assert "  - Line 12 skipped: Reason B" in captured.out`: Asserts that the detailed reason for the second skipped line is printed to stdout.

**Postconditions:**

*   A warning message with the number of skipped lines and their reasons has been logged.
*   Detailed information about the skipped lines has been printed to the console.

**Test Code:** `test_csv_handler.py::test_log_review_lines`

**Status:** Pass

**Notes:**

*   This test relies on the `pytest` framework, the `pytest-mock` plugin (`mocker` fixture), and a mocked `Logger` object (provided as a fixture).
*   The test isolates the `_log_review_lines` method by using a dummy CSV file path and directly manipulating the `Data` object.
*   The test verifies both the logging behavior and the console output.