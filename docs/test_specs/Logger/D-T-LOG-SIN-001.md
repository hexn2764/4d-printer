# Test Specification: D-T-LOG-SIN-001

**Test ID:** D-T-LOG-SIN-001

**Test Name:** Logger - Singleton Behavior

**Source:** Developer

**Module:** Logger

**Category:** Singleton

**Related Requirements:**

*   D-21
*   D-25

**Purpose:**
This test verifies that the `Logger` class implements the singleton design pattern, ensuring that only one instance of the `Logger` exists throughout the application.

**Preconditions:**

*   1) The `Logger` class is implemented as a singleton.

**Test Data:**

*   N/A

**Test Steps:**

1.  Create an instance of the `Logger` class (`logger1`).
2.  Create another instance of the `Logger` class (`logger2`).

**Expected Results:**

*   1) `logger1` and `logger2` should refer to the same object in memory.

**Assertions:**

*   `assert logger1 is logger2`: Asserts that `logger1` and `logger2` are the same object.

**Postconditions:**

*   Two `Logger` instances have been created, and they are the same object.

**Test Code:** `test_logger.py::test_singleton_behavior`

**Status:** Pass

**Notes:**

*   This test relies on the assumption that the `Logger` class is correctly implemented as a singleton using the `__new__` method.
