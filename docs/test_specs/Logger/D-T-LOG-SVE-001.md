# Test Specification: D-T-LOG-SVE-001

**Test ID:** D-T-LOG-SVE-001

**Test Name:** Logger - Set Verbose Enabled

**Source:** Developer

**Module:** Logger

**Category:** Set Verbose Enabled

**Related Requirements:**

*   D-21
*   D-23
*   D-26

**Purpose:**
This test verifies that the `set_verbose` method, when called with `True`, correctly sets the console logging level to `logging.INFO`.

**Preconditions:**

*   1) An instance of the `Logger` class is created.

**Test Data:**

*   N/A

**Test Steps:**

1.  Create an instance of the `Logger` class.
2.  Call the `set_verbose` method with `True` to enable verbose mode.

**Expected Results:**

*   1) The `setLevel` method of the `StreamHandler` should be called with `logging.INFO`.

**Assertions:**

*   `mock_logging['stream_handler'].setLevel.assert_called_with(logging.INFO)`: Asserts that the console logging level was set to `INFO`.

**Postconditions:**

*   The console logging level is set to `INFO`.

**Test Code:** `test_logger.py::test_set_verbose_enabled`

**Status:** Pass

**Notes:**

*   This test verifies the functionality of enabling verbose logging.
