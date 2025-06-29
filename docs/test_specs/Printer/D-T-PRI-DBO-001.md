# Test Specification: D-T-PRI-DBO-001

**Test ID:** D-T-PRI-DBO-001

**Test Name:** Printer - Do Basic Output

**Source:** Developer

**Module:** Printer

**Category:** Do Basic Output

**Related Requirements:**

*   D-21
*   D-27

**Purpose:**
This test verifies that the `do_basic_output` method of the `Printer` class correctly generates a basic, non-tabular output, where each entry's information (Requirement, Test Case, Duration, Status) is printed on a separate line.

**Preconditions:**

*   1) A `Printer` instance is created.
*   2) The `capsys` fixture is available to capture output.

**Test Data:**

*   `top_entries`: A list of tuples, where each tuple represents an entry and contains an ID and a dictionary of attributes (Requirement, Test Case, Duration, Status).
    ```python
    top_entries = [
        (10, {"Requirement": "R1", "Test Case": "TC1", "Duration": 3.14,  "Status": "Passed"}),
        (11, {"Requirement": "R2", "Test Case": "TC2", "Duration": 99.999,"Status": "Failed"})
    ]
    ```

**Test Steps:**

1.  Call the `do_basic_output` method with the `top_entries` data.
2.  Capture the output using `capsys.readouterr()`.

**Expected Results:**

*   1) The output should contain one line for each entry in `top_entries`.
*   2) Each line should be formatted as: "ID. Requirement: <value>, Test Case: <value>, Duration: <value> sec, Status: <value>".

**Assertions:**

*   `assert "1. Requirement: R1, Test Case: TC1, Duration: 3.140 sec, Status: Passed" in out`: Asserts that the output for the first entry is correctly formatted.
*   `assert "2. Requirement: R2, Test Case: TC2, Duration: 99.999 sec, Status: Failed" in out`: Asserts that the output for the second entry is correctly formatted.

**Postconditions:**

*   The `do_basic_output` method has been tested with sample data.
*   The output generated by `do_basic_output` has been verified to be correctly formatted.

**Test Code:** `test_printer.py::test_do_basic_output`

**Status:** Pass

**Notes:**

*   This test directly tests the `do_basic_output` method, which is responsible for generating the basic output format.
*   The test uses `capsys` to capture the output and then performs checks on the captured output.
