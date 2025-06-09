# Test Specification: D-T-ORC-SSK-001

**Test ID:** D-T-ORC-SSK-001

**Test Name:** Orchestrator - Set Sort Key

**Source:** Developer

**Module:** Orchestrator

**Category:** Set Sort Key

**Related Requirements:**

*   D-21

**Purpose:**
This test verifies that setting the `sort_key` attribute of the `TestStatisticReadWrite` class correctly updates the internal `_sort_key` attribute.

**Preconditions:**

*   1) The `os.path.isfile` function is mocked to return `True`.
*   2) An instance of the `TestStatisticReadWrite` class is created.

**Test Data:**

*   N/A

**Test Steps:**

1.  Patch `os.path.isfile` to always return `True`.
2.  Create an instance of `TestStatisticReadWrite` with dummy values for CSV path, output folder and top_x.
3.  Check the initial value of the `_sort_key` attribute.
4.  Set the `_sort_key` attribute to a new value (e.g., "Status").
5.  Check the updated value of the `_sort_key` attribute.

**Expected Results:**

*   1) The initial value of `_sort_key` should be "Duration".
*   2) After setting the `_sort_key` attribute, its value should be updated to the new value.

**Assertions:**

*   `assert orchestrator.sort_key == "Duration"`: Asserts that the initial `_sort_key` is "Duration".
*   `orchestrator.sort_key = "Status"`: Sets the `_sort_key` attribute to "Status".
*   `assert orchestrator.sort_key == "Status"`: Asserts that the `_sort_key` is updated to "Status".

**Postconditions:**

*   The `_sort_key` attribute of the `TestStatisticReadWrite` instance is updated to the new value.

**Test Code:** `test_test_statistic_read_write.py::test_set_sort_key`

**Status:** Pass

**Notes:**

*   This test focuses on the internal state of the `TestStatisticReadWrite` object.
*   The test mocks `os.path.isfile` as it's called in the constructor, but it doesn't affect this specific test.
*   The test uses dummy values for irrelevant arguments in the `TestStatisticReadWrite` constructor.
