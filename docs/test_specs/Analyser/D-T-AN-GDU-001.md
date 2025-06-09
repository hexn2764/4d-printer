# Test Specification: D-T-AN-GDU-001

**Test ID:** D-T-AN-GDU-001

**Test Name:** Analyser - Get Total Duration

**Source:** Developer

**Module:** Analyser

**Category:** Get Duration

**Related Requirements:**

*   D-13
*   D-21

**Purpose:**
This test verifies that the `_get_total_duration` method of the `Analyser` class correctly calculates the total duration from a sample dataset.

**Preconditions:**

*   1) An instance of the `Analyser` class has been created (using the `analyser` fixture).
*   2) A `Data` object containing sample data has been created (using the `sample_data` fixture).
*   3) At this step in the execution the `Data` array contains positive durations, hence no additional validations are required.

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

1.  Call the `_get_total_duration` method of the `Analyser` instance, passing the `sample_data` object as input.
2.  Store the returned value in a variable named `total_duration`.

**Expected Results:**

*   1) The `_get_total_duration` method should return a float representing the sum of the `"Duration"` values in the `sample_data`.
*   2) The returned `total_duration` should be equal to `33.6`.

**Assertions:**

*   `assert total_duration == 33.6`: Verifies that the calculated total duration matches the expected value `33.6`.

**Postconditions:**

*   The state of the `Analyser` instance and the `sample_data` object are not modified by this test.

**Test Code:** `test_analyser.py::test_get_total_duration`

**Status:** Pass

**Notes:**

*   This test relies on the `pytest` framework and uses the `analyser` and `sample_data` fixtures.
*   The expected value of `33.6` is calculated as the sum of the `"Duration"` values in the `sample_data` fixture.
