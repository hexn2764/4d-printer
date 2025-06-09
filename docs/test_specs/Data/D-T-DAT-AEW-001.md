# Test Specification: D-T-DAT-AEW-001

**Test ID:** D-T-DAT-AEW-001

**Test Name:** Data - Add Entries With Same Values

**Source:** Developer

**Module:** Data

**Category:** Data Insertion

**Related Requirements:**

*   D-4
*   D-9
*   D-21

**Purpose:**
This test verifies that the `Data.add_entry()` method correctly handles the insertion of entries with duplicate values for "Requirement", "Duration", and "Status" fields. It checks that the `sorted_ids` maintains the correct order based on a left-insert behavior when duplicates are encountered and that `sorted_values` contains all values in the correct order..

**Preconditions:**

*   1) An instance of the `Data` class is created.

**Test Data:**

*   Two entries with the following data:
    *   Entry 1:
        *   ID: 1
        *   Requirement: "REQ-X"
        *   Test Case: "TC-ALPHA"
        *   Duration: 10.0
        *   Status: "Passed"
    *   Entry 2:
        *   ID: 2
        *   Requirement: "REQ-X"
        *   Test Case: "TC-BETA"
        *   Duration: 10.0
        *   Status: "Failed"

**Test Steps:**

1.  Create an instance of the `Data` class.
2.  Add the first entry (ID 1) using `data.add_entry()`.
3.  Add the second entry (ID 2) using `data.add_entry()`.

**Expected Results:**

*   1) The `Data` object should contain 2 entries.
*   2) 2) For "Requirement", data.sorted_values stores sort key tuples. The second element of each tuple should correspond to `["REQ-X", "REQ-X"]`.
*   3) `data.sorted_ids` for "Requirement" should be `[2, 1]` (due to left-insert).
*   4) `data.sorted_values` for "Duration" should be `[10.0, 10.0]`.
*   5) `data.sorted_ids` for "Duration" should be `[2, 1]` (due to left-insert).
*   6) `data.sorted_values` for "Status" should be `["Failed", "Passed"]`.
*   7) `data.sorted_ids` for "Status" should be `[2, 1]` (due to left-insert).

**Assertions:**

*   `assert data.get_size() == 2`: Asserts that the `Data` object contains 2 entries.
*   `assert [t[1] for t in data.sorted_values.get("Requirement")] == ["REQ-X", "REQ-X"]`
*   `assert data.sorted_ids.get("Requirement") == [2, 1]`: Asserts the content of `sorted_ids` for "Requirement".
*   `assert data.sorted_values.get("Duration") == [10.0, 10.0]`: Asserts the content of `sorted_values` for "Duration".
*   `assert data.sorted_ids.get("Duration") == [2, 1]`: Asserts the content of `sorted_ids` for "Duration".
*   `assert data.sorted_values.get("Status") == ["Failed", "Passed"]`: Asserts the content of `sorted_values` for "Status".
*   `assert data.sorted_ids.get("Status") == [2, 1]`: Asserts the content of `sorted_ids` for "Status".

**Postconditions:**

*   The `Data` object contains two entries with duplicate "Requirement" and "Duration" values.
*   The `sorted_ids` and `sorted_values` are updated to reflect the insertion order, demonstrating the left-insert behavior for duplicates.

**Test Code:** `test_data.py::test_add_entries_with_same_values`

**Status:** Pass

**Notes:**

*   This test focuses on the internal behavior of the `Data` class, specifically how it maintains sorted lists when duplicate values are added.
*   The test implicitly assumes that `Data.add_entry()` uses a left-insert approach (like `bisect.bisect_left`) when inserting into the sorted lists.
