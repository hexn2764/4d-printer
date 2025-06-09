# Test Specification: D-T-CLI-LES-001

**Test ID:** D-T-CLI-LES-001

**Test Name:** CLI - Log End Of Session

**Source:** Developer

**Module:** CLI

**Category:** Logging

**Related Requirements:**

*   D-21
*   D-23

**Purpose:**
This test verifies that the `cli.log_end_of_session()` function correctly logs the end-of-session message using the `Logger` object. It checks that the `log_info` method of the logger is called once with the expected message.

**Preconditions:**

*   1) The `Logger` object is mocked to track its `log_info` method invocations.

**Test Data:**

*   None

**Test Steps:**

1.  Call `cli.log_end_of_session()`.

**Expected Results:**

*   1) The `Logger.log_info` method should be called exactly once.
*   2) The argument passed to `Logger.log_info` should be "Execution ended.\n".

**Assertions:**

*   `mock_logger.log_info.assert_called_once_with("Execution ended.\n")`: Asserts that the `log_info` method of the mocked logger was called exactly once with the message "Execution ended.\n".

**Postconditions:**

*   The end-of-session message has been logged.

**Test Code:** `test_cli.py::test_log_end_of_session`

**Status:** Pass

**Notes:**

*   This test relies on the `pytest` framework and a mocked `Logger` object (provided as a fixture).
*   The test assumes that the `cli.log_end_of_session()` function uses the `Logger` object to log the end-of-session message.
*   The test focuses on verifying the correct logging behavior and does not involve any file system interactions.
