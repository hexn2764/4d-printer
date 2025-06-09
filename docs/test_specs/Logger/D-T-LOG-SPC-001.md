# Test Specification: D-T-LOG-SPC-001

**Test ID:** D-T-LOG-SPC-001

**Test Name:** Logger - Log Special Characters

**Source:** Developer

**Module:** Logger

**Category:** Special Characters

**Related Requirements:**

*   D-21
*   D-23

**Purpose:**
This test verifies that the `Logger` class correctly handles logging messages containing special characters without raising any exceptions.

**Preconditions:**

*   1) An instance of the `Logger` class is created.

**Test Data:**

*   `message`: "Error: Invalid input! @#$$%^&*()"

**Test Steps:**

1.  Create an instance of the `Logger` class.
2.  Call the `log_error` method with the message containing special characters.
3.  Call the `log_info` method with the message containing special characters.

**Expected Results:**

*   1) The `error` method of the underlying `logging.Logger` object should be called once with the message.
*   2) The `info` method of the underlying `logging.Logger` object should be called once with the message.
*   3) No exceptions should be raised.

**Assertions:**

*   `mock_logging['mock_logger'].error.assert_called_once_with(message)`: Asserts that `error` was called with the message.
*   `mock_logging['mock_logger'].info.assert_called_once_with(message)`: Asserts that `info` was called with the message.

**Postconditions:**

*   A message containing special characters has been logged at both ERROR and INFO levels.

**Test Code:** `test_logger.py::test_log_special_characters`

**Status:** Pass

**Notes:**

*   This test ensures that the `Logger` can handle various characters that might appear in log messages.
