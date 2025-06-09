# Test Specification: D-T-DAT-ASE-001

**Test ID:** D-T-DAT-ASE-001

**Test Name:** Data - Add Single Entry

**Source:** Developer

**Module:** Data

**Category:** Data Insertion

**Related Requirements:**

*   D-4
*   D-9
*   D-21

**Purpose:**
This test verifies that the `Data.add_entry()` method correctly adds a single entry to the `Data` object and updates all associated `sorted_ids`, and `sorted_values` accordingly.

**Preconditions:**

*   1) An instance of the `Data` class is created.

**Test Data:**

*   `key`: 1 (an integer representing the key for the entry)
*   `entry`: A dictionary representing the entry data:
    ```
    {
        "Requirement": "REQ-A",
        "Test Case": "TC1",
        "Duration": 5.0,
        "Status": "Passed"
    }
    ```

**Test Steps:**

1.  Create an instance of the `Data` class.
2.  Define the `key` and `entry` data.
3.  Call `data.add_entry()` with the `key` and `entry`.

**Expected Results:**

*   1) The `Data` object should contain 1 entry.
*   2) The entry should be stored in `data.data` under the specified key (1).
*   3) All `sorted_ids` for "Requirement", "Test Case", "Duration", and "Status" should contain only the key (1).
*   4) For "Test Case", "Duration", and "Status", `sorted_values` should contain the corresponding values from the added entry. For "Requirement", `sorted_values` stores a sort key tuple whose second element corresponds to the Requirement string ("REQ-A").

**Assertions:**

*   `assert data.get_size() == 1, "Size should be 1 after adding one entry."`: Asserts that the `Data` object contains 1 entry.
*   `assert data.data[key] == entry, "The data dictionary should store the entry under key=1."`: Asserts that the entry is stored correctly.
*   `assert data.sorted_ids.get("Requirement") == [1], "Only one entry in requirement_sorted."`: Asserts the content of `sorted_ids` for "Requirement".
*   `assert data.sorted_ids.get("Test Case") == [1], "Only one entry in test_case_sorted."`: Asserts the content of `sorted_ids` for "Test Case".
*   `assert data.sorted_ids.get("Duration") == [1], "Only one entry in duration_sorted."`: Asserts the content of `sorted_ids` for "Duration".
*   `assert data.sorted_ids.get("Status") == [1], "Only one entry in status_sorted."`: Asserts the content of `sorted_ids` for "Status".
*   `assert [t[1] for t in data.sorted_values.get("Requirement")] == ["REQ-A"]`, "requirement_values should match the single 'REQ-A' (second element of sort key tuple)."
*   `assert data.sorted_values.get("Test Case") == ["TC1"], "test_case_values should match the single 'TC1'."`: Asserts the content of `sorted_values` for "Test Case".
*   `assert data.sorted_values.get("Duration") == [5.0], "duration_values should match the single 5.0."`: Asserts the content of `sorted_values` for "Duration".
*   `assert data.sorted_values.get("Status") == ["Passed"], "status_values should match the single 'Passed'."`: Asserts the content of `sorted_values` for "Status".

**Postconditions:**

*   The `Data` object contains the added entry.
*   All `sorted_ids` and `sorted_values` within the `Data` object are updated to reflect the added entry.

**Test Code:** `test_data.py::test_add_single_entry`

**Status:** Pass

**Notes:**

*   This test focuses on verifying the basic functionality of adding a single entry to the `Data` object.
*   It checks that all internal data structures are updated correctly after the insertion.
*   The "Requirement" field is sorted using a custom sort key (tuple); the test extracts the string component of the sort key for comparison.
