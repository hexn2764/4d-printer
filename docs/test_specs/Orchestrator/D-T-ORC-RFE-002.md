# Test Specification: D-T-ORC-RFE-002

**Test ID:** D-T-ORC-RFE-002

**Test Name:** Orchestrator - Run Friendly Exception at Export

**Source:** Developer

**Module:** Orchestrator

**Category:** Run Friendly Exception at Export

**Related Requirements:**

*   D-21
*   D-22

**Purpose:**
This test verifies that if a `FriendlyException` is raised during the `export_csv` operation, the `run` method of `TestStatisticReadWrite` catches it, logs an error message, prints an error message to the console, and exits with a status code of 1. It also verifies that `read_csv`, `analyze`, and `display_results` are executed before the exception.

**Preconditions:**

*   1) Mocks are set up for `Logger`, `CSVHandler`, `Analyser`, and `Printer`.
*   2) An instance of `TestStatisticReadWrite` is created.

**Test Data:**

*   N/A (Exception is mocked)

**Test Steps:**

1.  Create an instance of `TestStatisticReadWrite`.
2.  Set up `mock_csv_handler.export_csv` to raise a `FriendlyException`.
3.  Mock `sys.exit`.
4.  Call the `run` method.

**Expected Results:**

*   1) `read_csv` should be called successfully.
*   2) `analyze` should be called successfully.
*   3) `display_results` should be called successfully.
*   4) `export_csv` should raise a `FriendlyException`.
*   5) The `run` method should catch the exception.
*   6) An error message should be logged.
*   7) An error message should be printed to the console.
*   8) `sys.exit` should be called with a status code of 1.

**Assertions:**

*   `mock_exit.assert_called_once_with(1)`: Asserts that `sys.exit(1)` was called.
*   `mock_csv_handler.read_csv.assert_called_once()`: Asserts that `read_csv` was called.
*   `mock_analyser.analyze.assert_called_once()`: Asserts that `analyze` was called.
*   `mock_printer.display_results.assert_called_once()`: Asserts that `display_results` was called.
*   `assert "Error in processing. Mocked export failure Exiting." in captured.out`: Asserts that the error message is printed.
*   `mock_logger.log_error.assert_called_once()`: Asserts that the error message is logged.

**Postconditions:**

*   The program has exited with a status code of 1.
*   An error message has been logged and printed to the console.
*   `read_csv`, `analyze`, and `display_results` have been executed.

**Test Code:** `test_test_statistic_read_write.py::test_run_friendly_exception_at_export`

**Status:** Pass

**Notes:**

*   This test focuses on error handling when a `FriendlyException` occurs during the `export_csv` operation.
*   `mocker` is used to mock `sys.exit` to prevent the test runner from exiting.
*   `capsys` is used to capture and verify the error message printed to the console.
