# tests/test_analyser.py

import pytest
from test_statistic_read_write._analyser import Analyser
from test_statistic_read_write._data import Data
from test_statistic_read_write._exceptions import InvalidTopX

@pytest.fixture
def analyser():
    """Fixture to create an Analyser instance."""
    return Analyser()

@pytest.fixture
def sample_data():
    """Fixture to create a sample Data object."""
    data = Data()
    data.add_entry(1, {"Requirement": "R1", "Test Case": "TC1", "Duration": 10.5, "Status": "Passed"})
    data.add_entry(2, {"Requirement": "R2", "Test Case": "TC2", "Duration": 5.2, "Status": "Failed"})
    data.add_entry(3, {"Requirement": "R3", "Test Case": "TC3", "Duration": 15.8, "Status": "Passed"})
    data.add_entry(4, {"Requirement": "R4", "Test Case": "TC4", "Duration": 2.1, "Status": "Failed"})
    return data

def test_analyze(analyser, sample_data):
    """
    Test-ID: D-T-AN-AN-001
    Tests the `analyze` method of the `Analyser` class.

    Args:
        analyser (Analyser): The `Analyser` fixture.
        sample_data (Data): The `Data` fixture containing sample data.
    """
    result = analyser.analyze(sample_data, 2)
    assert "total_duration" in result
    assert "top_x_entries" in result
    assert result["total_duration"] == 33.6
    assert len(result["top_x_entries"]) == 2
    assert result["top_x_entries"][0][0] == 3
    assert result["top_x_entries"][0][1]["Duration"] == 15.8
    assert result["top_x_entries"][1][0] == 1
    assert result["top_x_entries"][1][1]["Duration"] == 10.5

def test_analyze_negative_top_x(analyser, sample_data):
    """
    Test-ID: D-T-AN-AN-002
    Tests the `analyze` method of the `Analyser` class with an invalid (negative) top_x value. 
    Verifies that an InvalidTopX exception is raised.

    Args:
        analyser (Analyser): The `Analyser` fixture.
        sample_data (Data): The `Data` fixture containing sample data.
    """
    with pytest.raises(InvalidTopX) as exc_info:
        analyser.analyze(sample_data, -5)

    assert "Invalid top_x value: -5. Must be a non-negative integer." == str(exc_info.value)

def test_get_total_duration(analyser, sample_data):
    """
    Test ID: D-T-AN-GDU-001
    Tests the `_get_total_duration` method of the `Analyser` class.

    Args:
        analyser (Analyser): The `Analyser` fixture.
        sample_data (Data): The `Data` fixture containing sample data.
    """
    total_duration = analyser._get_total_duration(sample_data)
    assert total_duration == 33.6


def test_get_top_x_entries(analyser, sample_data):
    """
    Test-ID: D-T-AN-GTX-001
    Tests the `_get_top_x_entries` method of the `Analyser` class with a valid `top_x` value.

    Args:
        analyser (Analyser): The `Analyser` fixture.
        sample_data (Data): The `Data` fixture containing sample data.
    """
    top_x_entries = analyser._get_top_x_entries(sample_data, 2)
    assert len(top_x_entries) == 2
    assert top_x_entries[0][0] == 3  # ID of the entry with the longest duration
    assert top_x_entries[0][1]["Duration"] == 15.8
    assert top_x_entries[1][0] == 1  # ID of the entry with the second longest duration
    assert top_x_entries[1][1]["Duration"] == 10.5

def test_get_top_x_entries_empty(analyser):
    """
    Test-ID: D-T-AN-GTX-002
    Tests the `_get_top_x_entries` method of the `Analyser` class with an empty `Data` object.

    Args:
        analyser (Analyser): The `Analyser` fixture.
    """
    data = Data()
    top_x_entries = analyser._get_top_x_entries(data, 5)
    assert top_x_entries == []

def test_get_top_x_entries_x_larger_than_data_size(analyser, sample_data):
    """
    Test-ID: D-T-AN-GTX-003
    Tests the `_get_top_x_entries` method of the `Analyser` class with `top_x` larger than the number of entries in the `Data` object.

    Args:
        analyser (Analyser): The `Analyser` fixture.
        sample_data (Data): The `Data` fixture containing sample data.
    """
    top_x_entries = analyser._get_top_x_entries(sample_data, 10)
    assert len(top_x_entries) == 4  # Should return all entries
    # Check if the entries are sorted by duration in descending order
    assert top_x_entries[0][1]["Duration"] == 15.8
    assert top_x_entries[1][1]["Duration"] == 10.5
    assert top_x_entries[2][1]["Duration"] == 5.2
    assert top_x_entries[3][1]["Duration"] == 2.1

def test_get_zero_top_x_entries(analyser, sample_data):
    """
    Test-ID: D-T-AN-GTX-004
    Tests the `_get_top_x_entries` method of the `Analyser` class with `top_x` equal to 0.

    Args:
        analyser (Analyser): The `Analyser` fixture.
        sample_data (Data): The `Data` fixture containing sample data.
    """
    top_x_entries = analyser._get_top_x_entries(sample_data, 0)
    assert len(top_x_entries) == 0
