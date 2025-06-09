# Test Specification: D-T-PRI-GWE-001

**Test ID:** D-T-PRI-GWE-001

**Test Name:** Printer - Get Width Empty data

**Source:** Developer

**Module:** Printer

**Category:** Get Width Empty data

**Related Requirements:**

*   D-18
*   D-21

**Purpose:**
This test verifies that the `get_width` method of the `Printer` class correctly calculates column widths when the input data list (`top_entries`) is empty. In this case, the widths should be based solely on the header lengths plus padding.

**Preconditions:**

*   1) A `Printer` instance is created.

**Test Data:**

*   `headers`: A list of column headers.
    ```python
    headers = ["ID", "Requirement", "Test Case", "Duration (sec)", "Status"]
    ```
*   `top_entries`: An empty list.

**Test Steps:**

1.  Call the `get_width` method with an empty `top_entries` list and the `headers` data.

**Expected Results:**

*   1) The method should return a list of integers, where each integer represents the calculated width for the corresponding column.
*   2) Each calculated width should be equal to the length of the corresponding header plus a fixed padding.

**Assertions:**

*   `assert widths == [len(header) + padding for header in headers]`: Asserts that the calculated widths are correct for each column, based on header lengths and padding.

**Postconditions:**

*   The `get_width` method has been tested with an empty data list.
*   The calculated column widths have been verified to be correct.

**Test Code:** `test_printer.py::test_get_width_empty_data`

**Status:** Pass

**Notes:**

*   This test checks the edge case where the input data list is empty.
*   It ensures that the `get_width` method can handle this scenario gracefully and still produce correct results based on the headers.
