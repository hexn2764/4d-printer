# Test Specification: D-T-ORC-RFE-001

**Test ID:** D-T-ORC-RFE-001

**Test Name:** Orchestrator - Run Friendly Exception at Read

**Source:** Developer

**Module:** Orchestrator

**Category:** Run Friendly Exception at Read

**Related Requirements:**

*   D-21
*   D-22

**Purpose:**
This test verifies that if a `FriendlyException` is raised during the `read_csv` operation, the `run` method of `TestStatisticReadWrite` catches it, logs an error message, prints an error message to the console, and exits with a status code of 1. It also verifies that subsequent operations like `analyze`, `display_results`, and `export_csv` are not executed.

**Preconditions:**

*   1) Mocks are set up for `Logger`, `CSVHandler`, `Analyser`, and `Printer`.
*   2) An instance of `TestStatisticReadWrite` is created.

**Test Data:**

*   N/A (Exception is mocked)

**Test Steps:**

1.  Create an instance of `TestStatisticReadWrite`.
2.  Set up `mock_csv_handler.read_csv` to raise a `FriendlyException`.
3.  Mock `sys.exit`.
4.  Call the `run` method.

**Expected Results:**

*   1) `read_csv` should raise a `FriendlyException`.
*   2) The `run` method should catch the exception.
*   3) An error message should be logged.
*   4) An error message should be printed to the console.
*   5) `sys.exit` should be called with a status code of 1.
*   6) `analyze`, `display_results`, and `export_csv` should not be called.

**Assertions:**

*   `mock_exit.assert_called_once_with(1)`: Asserts that `sys.exit(1)` was called.
*   `mock_analyser.analyze.assert_not_called()`: Asserts that `analyze` was not called.
*   `mock_printer.display_results.assert_not_called()`: Asserts that `display_results` was not called.
*   `mock_csv_handler.export_csv.assert_not_called()`: Asserts that `export_csv` was not called.
*   `assert "Error in processing. Mocked read error. Exiting." in captured.out`: Asserts that the error message is printed.
*   `mock_logger.log_error.assert_called_once_with(...)`: Asserts that the error message is logged.

**Postconditions:**

*   The program has exited with a status code of 1.
*   An error message has been logged and printed to the console.
*   No further processing (analysis, display, export) has occurred.

**Test Code:** `test_test_statistic_read_write.py::test_run_friendly_exception_at_read`

**Status:** Pass

**Notes:**

*   This test focuses on error handling when a `FriendlyException` occurs during the `read_csv` operation.
*   `mocker` is used to mock `sys.exit` to prevent the test runner from exiting.
*   `capsys` is used to capture and verify the error message printed to the console.
