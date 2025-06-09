
## Test Specification: D-T-AN-AN-002

**Test ID:** D-T-AN-AN-002

**Test Name:** Analyser - Analyze

**Source:** Developer

**Module:** Analyser

**Category:** Analyze

**Related Requirements:**
*   D-21

**Purpose:**
This test verifies that the `analyze` method of the `Analyser` class raises an `InvalidTopX` exception when called with an invalid (negative) `top_x` value.

**Preconditions:**
1. An instance of the `Analyser` class has been created (using the `analyser` fixture).
2. A `Data` object containing sample data has been created (using the `sample_data` fixture).

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
1. Call the `analyze` method of the `Analyser` instance, passing the `sample_data` object and a negative `top_x` value (-5) as input.
2. Capture any raised exception using `pytest.raises`.

**Expected Results:**
1. An `InvalidTopX` exception is raised.
2. The exception message matches the expected string: `"Invalid top_x value: -5. Must be a non-negative integer."`

**Assertions:**
* `with pytest.raises(InvalidTopX) as exc_info`: Verifies that an `InvalidTopX` exception is raised.
* `assert "Invalid top_x value: -5. Must be a non-negative integer." == str(exc_info.value)`: Verifies that the exception message matches the expected value.

**Postconditions:**
* The state of the `Analyser` instance and the `sample_data` object are not modified by this test.

**Test Code:** `test_analyser.py::test_analyze_negative_top_x`

**Status:** Pass

**Notes:**
* This test relies on the `pytest` framework and uses the `analyser` and `sample_data` fixtures.
* The test ensures that the `analyze` method enforces input validation for the `top_x` parameter.
