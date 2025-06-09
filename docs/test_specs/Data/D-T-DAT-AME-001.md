# Test Specification: D-T-DAT-AME-001

**Test ID:** D-T-DAT-AME-001

**Test Name:** Data - Add Multiple Entries Sorted

**Source:** Developer

**Module:** Data

**Category:** Data Insertion

**Related Requirements:**

*   D-4
*   D-9
*   D-21

**Purpose:**
This test verifies that the `Data.add_entry()` method correctly maintains the sorted order of entries in the `sorted_values`, and `sorted_ids` lists when multiple entries are added in a non-sequential order.

**Preconditions:**

*   1) An instance of the `Data` class is created.

**Test Data:**

*   Four entries with the following data:
    *   Entry 1:
        *   ID: 2
        *   Requirement: "REQ-B"
        *   Test Case: "TC2"
        *   Duration: 10.0
        *   Status: "Failed"
    *   Entry 2:
        *   ID: 1
        *   Requirement: "REQ-A"
        *   Test Case: "TC1"
        *   Duration: 5.0
        *   Status: "Passed"
    *   Entry 3:
        *   ID: 3
        *   Requirement: "REQ-C"
        *   Test Case: "TC3"
        *   Duration: 2.5
        *   Status: "Passed"
    *   Entry 4:
        *   ID: 4
        *   Requirement: "REQ-D"
        *   Test Case: "TC4"
        *   Duration: 4.0
        *   Status: "Passed"

**Test Steps:**

1.  Create an instance of the `Data` class.
2.  Add Entry 1 (ID 2) using `data.add_entry()`.
3.  Add Entry 2 (ID 1) using `data.add_entry()`.
4.  Add Entry 3 (ID 3) using `data.add_entry()`.
5.  Add Entry 4 (ID 4) using `data.add_entry()`.

**Expected Results:**

*   1) The `Data` object should contain 4 entries.
*   2) For "Requirement", data.sorted_values stores sort key tuples. The second element of each tuple should correspond to `["REQ-A", "REQ-B", "REQ-C", "REQ-D"]`.
*   3) `data.sorted_ids` for "Requirement" should be `[1, 2, 3, 4]`.
*   4) `data.sorted_values` for "Test Case" should be `["TC1", "TC2", "TC3", "TC4"]`
*   5) `data.sorted_ids` for "Test Case" should be `[1, 2, 3, 4]`
*   6) `data.sorted_values` for "Duration" should be `[2.5, 4.0, 5.0, 10.0]`.
*   7) `data.sorted_ids` for "Duration" should be `[3, 4, 1, 2]`.
*   8) `data.sorted_values` for "Status" should be `["Failed", "Passed", "Passed", "Passed"]`.
*   9) `data.sorted_ids` for "Status" should be `[2, 1, 3, 4]`.

**Assertions:**

*   `assert data.get_size() == 4, "Should have 4 entries now."`: Asserts that the `Data` object contains 4 entries.
*   `assert [t[1] for t in data.sorted_values.get("Requirement")] == ["REQ-A", "REQ-B", "REQ-C", "REQ-D"]`
*   `assert data.sorted_ids.get("Requirement") == [1, 2, 3, 4]`: Asserts the content of `sorted_ids` for "Requirement".
*   `assert data.sorted_values.get("Test Case") == ["TC1", "TC2", "TC3", "TC4"]`: Asserts the content of `sorted_values` for "Test Case".
*   `assert data.sorted_ids.get("Test Case") == [1, 2, 3, 4]`: Asserts the content of `sorted_ids` for "Test Case".
*   `assert data.sorted_values.get("Duration") == [2.5, 4.0, 5.0, 10.0]`: Asserts the content of `sorted_values` for "Duration".
*   `assert data.sorted_ids.get("Duration") == [3, 4, 1, 2]`: Asserts the content of `sorted_ids` for "Duration".
*   `assert data.sorted_values.get("Status") == ["Failed", "Passed", "Passed", "Passed"]`: Asserts the content of `sorted_values` for "Status".
*   `assert data.sorted_ids.get("Status") == [2, 1, 3, 4]`: Asserts the content of `sorted_ids` for "Status".

**Postconditions:**

*   The `Data` object contains four entries in the correct order.
*   The `sorted_values`, and `sorted_ids` lists are updated to reflect the insertion order and maintain the correct sorting.

**Test Code:** `test_data.py::test_add_multiple_entries_sorted`

**Status:** Pass

**Notes:**

*   This test focuses on verifying that the internal sorting logic of the `Data` class works correctly when entries are added out of order.
*   The test uses specific data to check both alphabetical and numerical sorting for different fields.
*    It also verifies that adding values with the same status keeps the order of insertion (left insert)
*  The "Requirement" field is sorted using a custom sort key (tuple); the test extracts the string component of the sort key for comparison.