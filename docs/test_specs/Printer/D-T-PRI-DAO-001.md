# Test Specification: D-T-PRI-DAO-001

**Test ID:** D-T-PRI-DAO-001

**Test Name:** Printer - Do Advanced Output

**Source:** Developer

**Module:** Printer

**Category:** Do Advanced Output

**Related Requirements:**

*   D-21
*   D-27

**Purpose:**
This test verifies that the `do_advanced_output` method of the `Printer` class correctly generates a formatted table output, including a header row, a separator row, and data rows, with appropriate spacing and alignment.

**Preconditions:**

*   1) A `Printer` instance is created.
*   2) The `capsys` fixture is available to capture output.

**Test Data:**

*   `top_entries`: A list of tuples, where each tuple represents an entry and contains an ID and a dictionary of attributes (Requirement, Test Case, Duration, Status).
    ```python
    top_entries = [
        (1, {"Requirement": "REQ-A", "Test Case": "TC-Alpha", "Duration": 2.345, "Status": "Passed"}),
        (2, {"Requirement": "XYZ",    "Test Case": "TC-LongName", "Duration": 123.456, "Status": "Skipped"}),
    ]
    ```

**Test Steps:**

1.  Call the `do_advanced_output` method with the `top_entries` data.
2.  Capture the output using `capsys.readouterr()`.
3.  Extract the header row and separator row from the captured output.
4.  Check data lines for correct format using regex.

**Expected Results:**

*   1) The output should contain a header row with the correct column names ("ID", "Requirement", "Test Case", "Duration (sec)", "Status").
*   2) The header row should have appropriate spacing between columns.
*   3) The output should contain a separator row with dashes ("-") aligned with the header columns.
*   4) The output should contain data rows, one for each entry in `top_entries`.
*   5) The data rows should be formatted according to a specific pattern (e.g., right-aligned numbers, left-aligned text).
*   6) The output lines should be correctly formatted according to the defined pattern.

**Assertions:**

*   `assert expected_header in header_line`: Asserts that the header row is present and has the correct format.
*   `assert "-"*(len(expected_header)) in out`: Asserts that the separator row is present and has the correct length.
*   `assert match is not None`: Asserts, using regex, that each data row is formatted according to the expected pattern.

**Postconditions:**

*   The `do_advanced_output` method has been tested with sample data.
*   The output generated by `do_advanced_output` has been verified to be correctly formatted.

**Test Code:** `test_printer.py::test_do_advanced_output`

**Status:** Pass

**Notes:**

*   This test directly tests the `do_advanced_output` method, which is responsible for generating the formatted table output.
*   The test uses `capsys` to capture the output and then performs various checks on the captured output to ensure its correctness.
*   Regex is used to make the test more flexible with regards to spacing and alignment.
