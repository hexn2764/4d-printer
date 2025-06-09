# Test Specification: D-T-PRI-GWL-001

**Test ID:** D-T-PRI-GWL-001

**Test Name:** Printer - Get Width Longer values

**Source:** Developer

**Module:** Printer

**Category:** Get Width Longer values

**Related Requirements:**

*   D-18
*   D-21

**Purpose:**
This test verifies that the `get_width` method of the `Printer` class correctly calculates column widths when the data values in some columns are longer than the corresponding header lengths.

**Preconditions:**

*   1) A `Printer` instance is created.

**Test Data:**

*   `headers`: A list of column headers.
    ```python
    headers = ["ID", "Requirement", "Test Case", "Duration", "Status"]
    ```
*   `top_entries`: A list of tuples, where each tuple represents an entry and contains an ID and a dictionary of attributes. Some data values are intentionally longer than their corresponding header lengths.
    ```python
    top_entries: List[Tuple[int, Dict[str, Any]]] = [
        (1, {"Requirement": "LongerRequirement", "Test Case": "LongerTestCaseName", "Duration": 1234567.89123456789, "Status": "LongerStatus"}),
        (100, {"Requirement": "Short", "Test Case": "TC", "Duration": 1.0, "Status": "S"})
    ]
    ```

**Test Steps:**

1.  Call the `get_width` method with the `top_entries` and `headers` data.

**Expected Results:**

*   1) The method should return a list of integers, where each integer represents the calculated width for the corresponding column.
*   2) Each calculated width should be equal to the maximum of the header length and the maximum data length in that column, plus a fixed padding. So, `max(<header_length>, <data_length>) + padding`.
*   3) In this specific case, the widths should be determined by the longer data values rather than the header lengths for the "Requirement", "Test Case", "Duration," and "Status" columns.

**Assertions:**

*   `assert widths == [expected_id_width, expected_req_width, expected_tc_width, expected_dur_width, expected_stat_width]`: Asserts that the calculated widths are correct for each column, considering the longer data values and padding.

**Postconditions:**

*   The `get_width` method has been tested with data values longer than header lengths.
*   The calculated column widths have been verified to be correct.

**Test Code:** `test_printer.py::test_get_width_with_longer_data_values`

**Status:** Pass

**Notes:**

*   This test checks the scenario where the data values influence the column widths more than the header lengths.
*   The test uses specific data values that are longer than the default header lengths to trigger this scenario.
*   It uses pre-calculated `expected_..._width` values to compare against the result.
