# tests/test_data.py

import pytest
from test_statistic_read_write._data import Data
from test_statistic_read_write._analyser import Analyser

def test_add_entries_with_same_values():
    """
    Test-ID: D-T-DAT-AEW-001
    Verifies that entries with same values are added correctly.

    Tests behavior when multiple entries have the same requirement or same
    duration, ensuring insertion still works with bisect_left but stable
    enough for repeated values. Specifically, it checks that the
    requirement_sorted, duration_sorted, and status_sorted lists maintain
    the correct order when duplicate values are added.

    """
    data = Data()

    data.add_entry(1, {
        "Requirement": "REQ-X",
        "Test Case": "TC-ALPHA",
        "Duration": 10.0,
        "Status": "Passed"
    })
    data.add_entry(2, {
        "Requirement": "REQ-X",
        "Test Case": "TC-BETA",
        "Duration": 10.0,
        "Status": "Failed"
    })

    assert data.get_size() == 2

    # requirement_values
    actual_req_values = [t[1] for t in data.sorted_values.get("Requirement")]
    assert actual_req_values == ["REQ-X", "REQ-X"]
    assert data.sorted_ids.get("Requirement") == [2, 1]  # left insert

    # duration_values
    assert data.sorted_values.get("Duration") == [10.0, 10.0]
    assert data.sorted_ids.get("Duration") == [2, 1]  # left insert

    # status values
    assert data.sorted_values.get("Status") == ["Failed", "Passed"]
    assert data.sorted_ids.get("Status") == [2, 1]  # left insert


def test_add_multiple_entries_sorted():
    """
    Test-ID: D-T-DAT-AME-001
    Verifies that adding multiple entries maintains correct sorting.

    Test adding multiple entries in an order that checks whether
    the insertion maintains ascending sorting for each field.

    """
    data = Data()

    # Insert an entry that should come later in alphabetical sorting for 'Requirement'
    data.add_entry(2, {
        "Requirement": "REQ-B",
        "Test Case": "TC2",
        "Duration": 10.0,
        "Status": "Failed"
    })

    # Insert an entry that should come earlier for 'Requirement'
    data.add_entry(1, {
        "Requirement": "REQ-A",
        "Test Case": "TC1",
        "Duration": 5.0,
        "Status": "Passed"
    })

    data.add_entry(3, {
        "Requirement": "REQ-C",
        "Test Case": "TC3",
        "Duration": 2.5,
        "Status": "Passed"
    })

    data.add_entry(4, {
        "Requirement": "REQ-D",
        "Test Case": "TC4",
        "Duration": 4.0,
        "Status": "Passed"
    })

    # Check final size
    assert data.get_size() == 4, "Should have 4 entries now."

    # Check requirements sorting
    actual_req_values = [t[1] for t in data.sorted_values.get("Requirement")]
    assert actual_req_values == ["REQ-A", "REQ-B", "REQ-C", "REQ-D"]
    assert data.sorted_ids.get("Requirement") == [1, 2, 3, 4]

    # Check test_case_values
    assert data.sorted_values.get("Test Case") == ["TC1", "TC2", "TC3", "TC4"]
    assert data.sorted_ids.get("Test Case") == [1, 2, 3, 4]

    # Check duration sorting
    assert data.sorted_values.get("Duration") == [2.5, 4.0, 5.0, 10.0]
    assert data.sorted_ids.get("Duration") == [3, 4, 1, 2]

    # Check status sorting => 'Failed' < 'Passed' in lexicographical order
    assert data.sorted_values.get("Status") == ["Failed", "Passed", "Passed", "Passed"]
    assert data.sorted_ids.get("Status") == [2, 4, 3, 1]  # left insert, so the last entered value is to the most left


def test_add_single_entry():
    """
    Test-ID: D-T-DAT-ASE-001
    Verifies that adding a single entry updates sorted lists and values correctly.

    Test adding a single entry to verify that all sorted lists and values
    are updated correctly. Specifically, it checks that the size of the
    Data object is correct, the entry is stored under the correct key,
    and all sorted lists (requirement_sorted, test_case_sorted,
    duration_sorted, status_sorted) and value lists (requirement_values,
    test_case_values, duration_values, status_values) contain the expected
    values.
    """
    data = Data()
    key = 1
    entry = {
        "Requirement": "REQ-A",
        "Test Case": "TC1",
        "Duration": 5.0,
        "Status": "Passed"
    }

    data.add_entry(key, entry)

    assert data.get_size() == 1, "Size should be 1 after adding one entry."
    assert data.data[key] == entry, "The data dictionary should store the entry under key=1."

    assert data.sorted_ids.get("Requirement") == [1], "Only one entry in requirement_sorted."
    assert data.sorted_ids.get("Test Case") == [1],    "Only one entry in test_case_sorted."
    assert data.sorted_ids.get("Duration") == [1],     "Only one entry in duration_sorted."
    assert data.sorted_ids.get("Status") == [1],       "Only one entry in status_sorted."

    actual_req_values = [t[1] for t in data.sorted_values.get("Requirement")]
    assert actual_req_values == ["REQ-A"], "requirement_values should match the single 'REQ-A'."

    assert data.sorted_values.get("Test Case") == ["TC1"],     "test_case_values should match the single 'TC1'."
    assert data.sorted_values.get("Duration") == [5.0],        "duration_values should match the single 5.0."
    assert data.sorted_values.get("Status") == ["Passed"],     "status_values should match the single 'Passed'."


def test_data_counts_statuses():
    """
    Test-ID: D-T-DAT-CSC-001
    Verifies that the `Data` class correctly maintains a collection of test IDs for each status.

    This test adds multiple entries with different statuses to a `Data` object
    and then checks that the `status_collections` attribute is correctly
    populated, mapping each status to a list of corresponding test IDs.

    """
    data = Data()

    data.add_entry(1, {
        "Requirement": "REQ-A",
        "Test Case": "TC-ALPHA",
        "Duration": 10.0,
        "Status": "Passed"
    })
    data.add_entry(2, {
        "Requirement": "REQ-B",
        "Test Case": "TC-BETA",
        "Duration": 10.0,
        "Status": "Failed"
    })
    data.add_entry(3, {
        "Requirement": "REQ-C",
        "Test Case": "TC-GAMMA",
        "Duration": 10.0,
        "Status": "Passed"
    })
    
    assert data.status_collections == {"Passed": [1,3], "Failed": [2]}
    
    data.add_entry(4, {
        "Requirement": "REQ-D",
        "Test Case": "TC-DELTA",
        "Duration": 10.0,
        "Status": "Blocked"
    })
    assert data.status_collections == {"Passed": [1,3], "Failed": [2], "Blocked": [4]}

    analyser = Analyser()
    data = analyser.analyze(data, 5)
    count = data.get("status_counts")

    assert count == {"Passed": 2, "Failed": 1, "Blocked": 1}


def test_initial_state():
    """
    Test-ID: D-T-DAT-INI-001
    Verifies that a new Data object is initialized with empty lists and dictionary.

    This test checks that a newly created Data object has a size of 0, an
    empty data dictionary, and empty lists for requirement_sorted,
    test_case_sorted, duration_sorted, status_sorted, requirement_values,
    test_case_values, duration_values, status_values, and review_lines.
    """
    data = Data()
    
    assert data.get_size() == 0, "New Data object should have size 0."
    assert data.data == {}, "data dictionary should be empty initially."
    
    assert data.sorted_ids.get("Requirement") == [], "requirement_sorted should be empty initially."
    assert data.sorted_ids.get("Test Case") == [], "test_case_sorted should be empty initially."
    assert data.sorted_ids.get("Duration") == [], "duration_sorted should be empty initially."
    assert data.sorted_ids.get("Status") == [], "status_sorted should be empty initially."

    assert data.sorted_values.get("Requirement") == [], "requirement_values should be empty initially."
    assert data.sorted_values.get("Test Case") == [], "test_case_values should be empty initially."
    assert data.sorted_values.get("Duration") == [], "duration_values should be empty initially."
    assert data.sorted_values.get("Status") == [], "status_values should be empty initially."

    assert data.review_lines == [], "review_lines should be empty initially."
    assert data.status_collections == {}, "status_collections should be empty initially."


