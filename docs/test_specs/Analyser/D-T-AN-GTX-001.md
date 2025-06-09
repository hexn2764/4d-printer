# Test Specification: D-T-AN-GTX-001

**Test ID:** D-T-AN-GTX-001

**Test Name:** Analyser - Get Top X Entries

**Source:** Developer

**Module:** Analyser

**Category:** Get Top X

**Related Requirements:**

*   D-14
*   D-21

**Purpose:**
This test verifies that the `_get_top_x_entries` method of the `Analyser` class correctly returns the `top X` entries with the longest durations from a sample dataset when provided with a valid `top_x` value.

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

1.  Call the `_get_top_x_entries` method of the `Analyser` instance, passing the `sample_data` object and `top_x = 2` as input.
2.  Store the returned value in a variable named `top_x_entries`.

**Expected Results:**

*   1) The `_get_top_x_entries` method should return a list of tuples, where each tuple contains an ID and a dictionary representing an entry from the `sample_data`.
*   2) The returned list `top_x_entries` should contain exactly 2 entries.
*   3) The first entry in `top_x_entries` should correspond to the entry with `ID 3`(the longest duration).
*   4) The second entry in `top_x_entries` should correspond to the entry with `ID 1` (the second longest duration).
*   5) The "Duration" value of the first entry should be `15.8`.
*   6) The "Duration" value of the second entry should be `10.5`.

**Assertions:**

*   `assert len(top_x_entries) == 2`: Verifies that the returned list contains 2 entries.
*   `assert top_x_entries[0][0] == 3`: Verifies that the ID of the first entry is 3.
*   `assert top_x_entries[0][1]["Duration"] == 15.8`: Verifies that the "Duration" of the first entry is 15.8.
*   `assert top_x_entries[1][0] == 1`: Verifies that the ID of the second entry is 1.
*   `assert top_x_entries[1][1]["Duration"] == 10.5`: Verifies that the "Duration" of the second entry is 10.5.

**Postconditions:**

*   The state of the `Analyser` instance and the `sample_data` object are not modified by this test.

**Test Code:** `test_analyser.py::test_get_top_x_entries`

**Status:** Pass

**Notes:**

*   The test will fail, if `top_x=0`, because `top_x_entries` will be empty.

*   This test relies on the `pytest` framework and uses the `analyser` and `sample_data` fixtures.
*   The test verifies that the `_get_top_x_entries` method correctly identifies and returns the entries with the longest durations, based on the provided `top_x` value.
