# Test Specification: D-T-AN-GTX-004

**Test ID:** D-T-AN-GTX-004

**Test Name:** Analyser - Get Zero Top X Entries

**Source:** Developer

**Module:** Analyser

**Category:** Get Top X Entries

**Related Requirements:**

*   D-14
*   D-21

**Purpose:**
This test verifies that the `_get_top_x_entries` method of the `Analyser` class returns an empty list when `top_x` is 0.

**Preconditions:**

*   1) An `Analyser` instance is created.
*   2) A `Data` object with sample data is created.

**Test Data:**

*   `sample_data`: A `Data` object containing sample entries.
*   `top_x`: 0

**Test Steps:**

1.  Call the `_get_top_x_entries` method with `sample_data` and `top_x` set to 0.

**Expected Results:**

*   1) The `_get_top_x_entries` method should return an empty list.

**Assertions:**

*   `assert len(top_x_entries) == 0`: Asserts that the returned list is empty.

**Postconditions:**

*   The `_get_top_x_entries` method has been tested with `top_x` equal to 0.

**Test Code:** `test_analyser.py::test_get_zero_top_x_entries`

**Status:** Pass

**Notes:**

*   This test specifically checks the edge case where `top_x` is 0.