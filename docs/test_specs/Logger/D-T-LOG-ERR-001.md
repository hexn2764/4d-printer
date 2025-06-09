# Test Specification: D-T-LOG-ERR-001

**Test ID:** D-T-LOG-ERR-001

**Test Name:** Logger - Log Error

**Source:** Developer

**Module:** Logger

**Category:** Log Error

**Related Requirements:**

*   D-21
*   D-23

**Purpose:**
This test verifies that the `log_error` method of the `Logger` class correctly logs a message at the ERROR level.

**Preconditions:**

*   1) An instance of the `Logger` class is created.

**Test Data:**

*   `message`: "This is an error message."

**Test Steps:**

1.  Create an instance of the `Logger` class.
2.  Call the `log_error` method with the test message.

**Expected Results:**

*   1) The `error` method of the underlying `logging.Logger` object should be called once with the test message.

**Assertions:**

*   `mock_logging['mock_logger'].error.assert_called_once_with(message)`: Asserts that the `error` method was called once with the correct message.

**Postconditions:**

*   An error message has been logged.

**Test Code:** `test_logger.py::test_log_error`

**Status:** Pass

**Notes:**

*   This test uses mocking to verify that the underlying `logging.Logger` object's `error` method is called correctly.
