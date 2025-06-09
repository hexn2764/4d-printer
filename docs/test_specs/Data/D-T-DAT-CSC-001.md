# Test Specification: D-T-DAT-CSC-001

**Test ID:** D-T-DAT-CSC-001

**Test Name:** Data - Count Statuses

**Source:** Developer

**Module:** Data

**Category:** Status Counts

**Related Requirements:**

*   D-16
*   D-21

**Purpose:**
This test verifies that the `Data` class correctly maintains a collection of test IDs for each status encountered in the added entries and provides correct counts for each status via the `Analyser` class. It ensures that `status_collections` is updated properly when new entries with different statuses are added, and that `Analyser.analyze` calculates status counts accurately.

**Preconditions:**

*   1) An instance of the `Data` class is created.
*   2) An instance of the `Analyser` class is created.

**Test Data:**

*   Multiple entries with the following statuses: "Passed", "Failed", "Blocked".

**Test Steps:**

1.  Create an instance of the `Data` class.
2.  Add multiple entries with different statuses using `data.add_entry()`.
3.  Create an instance of the `Analyser` class.
4.  Call `analyser.analyze()` on the `Data` instance to obtain the analysis results.
5.  Retrieve the `status_counts` from the analysis results.

**Expected Results:**

*   1) The `data.status_collections` attribute should be a dictionary.
*   2) The keys of the dictionary should be the unique statuses encountered ("Passed", "Failed", "Blocked").
*   3) The values of the dictionary should be lists of test IDs corresponding to each status.
*   4) The `status_counts` obtained from `Analyser.analyze` should be a dictionary mapping each status to its count.

**Assertions:**

*   `assert data.status_collections == {"Passed": [1,3], "Failed": [2]}`: Asserts the initial content of `status_collections`.
*   `assert data.status_collections == {"Passed": [1,3], "Failed": [2], "Blocked": [4]}`: Asserts the content of `status_collections` after adding a "Blocked" entry.
*   `assert count == {"Passed": 2, "Failed": 1, "Blocked": 1}`: Asserts that the `status_counts` from `Analyser.analyze` are correct.

**Postconditions:**

*   The `Data` object contains multiple entries with different statuses.
*   The `data.status_collections` attribute correctly maps each status to a list of corresponding test IDs.
*   The `Analyser` class correctly calculates the counts for each status.

**Test Code:** `test_data.py::test_data_counts_statuses`

**Status:** Pass

**Notes:**

*   This test verifies the functionality of maintaining a collection of test IDs for each status and calculating status counts using the `Analyser`.
*   It implicitly tests the interaction between `Data.add_entry()`, `Data.status_collections`, and `Analyser.analyze`.
