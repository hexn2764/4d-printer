# Test Specification: D-T-DAT-INI-001

**Test ID:** D-T-DAT-INI-001

**Test Name:** Data - Initial State

**Source:** Developer

**Module:** Data

**Category:** Initialization

**Related Requirements:**

*   D-21

**Purpose:**
This test verifies that a newly created `Data` object is initialized to the correct empty state. It checks that all internal data structures are empty, including the `data` dictionary, the `sorted_ids`, the `sorted_values`, `review_lines`, and `status_collections`.

**Preconditions:**

*   1) An instance of the `Data` class is created.

**Test Data:**

*   None

**Test Steps:**

1.  Create an instance of the `Data` class.

**Expected Results:**

*   1) `data.get_size()` should return 0.
*   2) `data.data` should be an empty dictionary.
*   3) All `sorted_ids` for "Requirement", "Test Case", "Duration", and "Status" should be empty.
*   4) All `sorted_values` for "Requirement", "Test Case", "Duration", and "Status" should be empty.
*   5) `data.review_lines` should be an empty list.
*   6) `data.status_collections` should be an empty dictionary.

**Assertions:**

*   `assert data.get_size() == 0, "New Data object should have size 0."`: Asserts that the size of the `Data` object is 0.
*   `assert data.data == {}, "data dictionary should be empty initially."`: Asserts that the `data` dictionary is empty.
*   `assert data.sorted_ids.get("Requirement") == [], "requirement_sorted should be empty initially."`: Asserts that `sorted_ids` for "Requirement" is empty.
*   `assert data.sorted_ids.get("Test Case") == [], "test_case_sorted should be empty initially."`: Asserts that `sorted_ids` for "Test Case" is empty.
*   `assert data.sorted_ids.get("Duration") == [], "duration_sorted should be empty initially."`: Asserts that `sorted_ids` for "Duration" is empty.
*   `assert data.sorted_ids.get("Status") == [], "status_sorted should be empty initially."`: Asserts that `sorted_ids` for "Status" is empty.
*   `assert data.sorted_values.get("Requirement") == [], "requirement_values should be empty initially."`: Asserts that `sorted_values` for "Requirement" is empty.
*   `assert data.sorted_values.get("Test Case") == [], "test_case_values should be empty initially."`: Asserts that `sorted_values` for "Test Case" is empty.
*   `assert data.sorted_values.get("Duration") == [], "duration_values should be empty initially."`: Asserts that `sorted_values` for "Duration" is empty.
*   `assert data.sorted_values.get("Status") == [], "status_values should be empty initially."`: Asserts that `sorted_values` for "Status" is empty.
*   `assert data.review_lines == [], "review_lines should be empty initially."`: Asserts that `review_lines` is empty.
*   `assert data.status_collections == {}, "status_collections should be empty initially."`: Asserts that `status_collections` is empty.

**Postconditions:**

*   A `Data` object exists in its initial, empty state.

**Test Code:** `test_data.py::test_initial_state`

**Status:** Pass

**Notes:**

*   This test focuses on verifying the correct initialization of a new `Data` object.
*   It ensures that all internal data structures are properly initialized to their empty states.
