# Test Specification: D-T-AN-GTX-003

**Test ID:** D-T-AN-GTX-003

**Test Name:** Analyser - Get Top X Entries X Larger Than Data Size

**Source:** Developer

**Module:** Analyser

**Category:** Get Top X

**Related Requirements:**

*   D-14
*   D-21

**Purpose:**
This test verifies that the `_get_top_x_entries` method of the `Analyser` class correctly handles the case where the provided `top_x` value is larger than the number of entries in the `Data` object. It ensures that all entries are returned and that they are sorted by duration in descending order.

**Preconditions:**

*   1) An instance of the `Analyser` class has been created (using the `analyser` fixture).
*   2) A `Data` object containing sample data has been created (using the `sample_data` fixture).

**Test Data:**

The test uses the `sample_data` fixture, which provides a `Data` object with the following entries:

```python
[
{"Requirement": "R1", "Test Case": "TC1", "Duration": 10.5, "Status": "Passed"},
{"Requirement": "R2", "Test Case": "TC2", "Duration": 5.2, "Status": "Failed"},
{"Requirement": "R3", "Test Case": "TC3", "Duration": 15.8, "Status": "Passed"},
{"Requirement": "R4", "Test Case": "TC4", "Duration": 2.1, "Status": "Failed"}
]
```

**Test Steps:**

1.  Call the `_get_top_x_entries` method of the `Analyser` instance, passing the `sample_data` object and `top_x = 10` as input.
2.  Store the returned value in a variable named `top_x_entries`.

**Expected Results:**

*   1) The `_get_top_x_entries` method should return a list of tuples, where each tuple contains an ID and a dictionary representing an entry from the `sample_data`.
*   2) The returned list `top_x_entries` should contain all 4 entries from the `sample_data` object.
*   3) The entries in `top_x_entries` should be sorted by "Duration" in descending order.

**Assertions:**

*   `assert len(top_x_entries) == 4`: Verifies that the returned list contains all 4 entries.
*   `assert top_x_entries[0][1]["Duration"] == 15.8`: Verifies that the "Duration" of the first entry is 15.8 (the longest).
*   `assert top_x_entries[1][1]["Duration"] == 10.5`: Verifies that the "Duration" of the second entry is 10.5.
*   `assert top_x_entries[2][1]["Duration"] == 5.2`: Verifies that the "Duration" of the third entry is 5.2.
*   `assert top_x_entries[3][1]["Duration"] == 2.1`: Verifies that the "Duration" of the fourth entry is 2.1 (the shortest).

**Postconditions:**

*   The state of the `Analyser` instance and the `sample_data` object are not modified by this test.

**Test Code:** `test_analyser.py::test_get_top_x_entries_x_larger_than_data_size`

**Status:** Pass

**Notes:**

*   This test relies on the `pytest` framework and uses the `analyser` and `sample_data` fixtures.
*   The test verifies that the `_get_top_x_entries` method correctly handles the edge case where `top_x` is larger than the number of entries in the input `Data` object.
