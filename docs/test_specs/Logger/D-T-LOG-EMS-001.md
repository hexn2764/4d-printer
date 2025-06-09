# Test Specification: D-T-LOG-EMS-001

**Test ID:** D-T-LOG-EMS-001

**Test Name:** Logger - Log Empty String

**Source:** Developer

**Module:** Logger

**Category:** Empty String

**Related Requirements:**

*   D-21
*   D-23

**Purpose:**
This test verifies that the `Logger` class correctly handles logging an empty string without raising any exceptions.

**Preconditions:**

*   1) An instance of the `Logger` class is created.

**Test Data:**

*   `message`: "" (an empty string)

**Test Steps:**

1.  Create an instance of the `Logger` class.
2.  Call the `log_info` method with the empty string.
3.  Call the `log_error` method with the empty string.

**Expected Results:**

*   1) The `info` method of the underlying `logging.Logger` object should be called once with the empty string.
*   2) The `error` method of the underlying `logging.Logger` object should be called once with the empty string.
*   3) No exceptions should be raised.

**Assertions:**

*   `mock_logging['mock_logger'].info.assert_called_once_with(message)`: Asserts that `info` was called with the empty string.
*   `mock_logging['mock_logger'].error.assert_called_once_with(message)`: Asserts that `error` was called with the empty string.

**Postconditions:**

*   An empty string has been logged at both INFO and ERROR levels.

**Test Code:** `test_logger.py::test_log_empty_string`

**Status:** Pass

**Notes:**

*   This test verifies that the `Logger` class gracefully handles empty strings, which can be a common edge case.
