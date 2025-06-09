# Test Specification: D-T-LOG-SVD-001

**Test ID:** D-T-LOG-SVD-001

**Test Name:** Logger - Set Verbose Disabled

**Source:** Developer

**Module:** Logger

**Category:** Set Verbose Disabled

**Related Requirements:**

*   D-21
*   D-23
*   D-26

**Purpose:**
This test verifies that the `set_verbose` method, when called with `False`, correctly sets the console logging level to `logging.CRITICAL`.

**Preconditions:**

*   1) An instance of the `Logger` class is created.

**Test Data:**

*   N/A

**Test Steps:**

1.  Create an instance of the `Logger` class.
2.  Call the `set_verbose` method with `False` to disable verbose mode.

**Expected Results:**

*   1) The `setLevel` method of the `StreamHandler` should be called with `logging.CRITICAL`.

**Assertions:**

*   `mock_logging['stream_handler'].setLevel.assert_called_with(logging.CRITICAL)`: Asserts that the console logging level was set to `CRITICAL`.

**Postconditions:**

*   The console logging level is set to `CRITICAL`.

**Test Code:** `test_logger.py::test_set_verbose_disabled`

**Status:** Pass

**Notes:**

*   This test verifies the functionality of disabling verbose logging.
