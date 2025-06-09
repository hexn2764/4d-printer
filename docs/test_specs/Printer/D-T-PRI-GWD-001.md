# Test Specification: D-T-PRI-GWD-001

**Test ID:** D-T-PRI-GWD-001

**Test Name:** Printer - Get Width

**Source:** Developer

**Module:** Printer

**Category:** Get Width

**Related Requirements:**

*   D-18
*   D-21

**Purpose:**
This test verifies that the `get_width` method of the `Printer` class correctly calculates the required width for each column in a table, based on the header lengths and the maximum length of the data in each column, plus additional padding.

**Preconditions:**

*   1) A `Printer` instance is created.

**Test Data:**

*   `headers`: A list of column headers.
    ```python
    headers = ["ID", "Requirement", "Test Case", "Duration (sec)", "Status"]
    ```
*   `top_entries`: A list of tuples, where each tuple represents an entry and contains an ID and a dictionary of attributes.
    ```python
    top_entries = [
        (1, {"Requirement": "ABC",  "Test Case": "X",    "Duration": 15.1234, "Status": "Pass"}),
        (2, {"Requirement": "LongReq", "Test Case": "XXY", "Duration": 999.5,  "Status": "FailedTest"})
    ]
    ```

**Test Steps:**

1.  Call the `get_width` method with the `top_entries` and `headers` data.

**Expected Results:**

*   1) The method should return a list of integers, where each integer represents the calculated width for the corresponding column.
*   2) Each calculated width should be equal to 1) the maximum of the header length and 2) the maximum data length in that column, plus a fixed padding. So, `max(<header_length>, <data_length>) + padding`.

**Assertions:**

*   `assert widths[0] == len("ID") + pad_length`: Asserts that the width of the first column ("ID") is calculated correctly.
*   `assert widths[1] == len("Requirement") + pad_length`: Asserts that the width of the second column ("Requirement") is calculated correctly.
*   `assert widths[2] == len("Test Case") + pad_length`: Asserts that the width of the third column ("Test Case") is calculated correctly.
*   `assert widths[3] == len("Duration (sec)") + pad_length`: Asserts that the width of the fourth column ("Duration (sec)") is calculated correctly.
*   `assert widths[4] == len("FailedTest") + pad_length`: Asserts that the width of the fifth column ("Status") is calculated correctly.

**Postconditions:**

*   The `get_width` method has been tested with sample data.
*   The calculated column widths have been verified to be correct.

**Test Code:** `test_printer.py::test_get_width`

**Status:** Pass

**Notes:**

*   This test checks the basic functionality of the `get_width` method, which is crucial for proper table formatting.
