# Test Specification: D-T-CSV-RDC-001

**Test ID:** D-T-CSV-RDC-001

**Test Name:** CSV Handler - Read CSV Valid File

**Source:** Developer

**Module:** CSV Handler

**Category:** Read CSV

**Related Requirements:**

*   D-1
*   D-3
*   D-4
*   D-21

**Purpose:**
This test verifies that the `CSVHandler.read_csv()` method correctly reads and parses a valid CSV file, populating the `Data` object with the extracted information. It ensures that the method can handle valid test cases, durations, and statuses.

**Preconditions:**

*   1) The `builtins.open` function is mocked using `mocker.mock_open` to simulate reading from a file with the specified `csv_content`.
*   2) The `os.path.isfile` function is mocked to always return `True`.

**Test Data:**

*   `csv_content`: A string representing the content of a valid CSV file:
    ```csv
    Test case;Duration;Status
    R1\\TC1;10.5 sec;Passed
    R2\\TC2;5.2 min;Failed
    ```

**Test Steps:**

1.  Create a mock file object using `mocker.mock_open` with the `csv_content`.
2.  Patch `builtins.open` to return the mock file object.
3.  Patch `os.path.isfile` to always return `True`.
4.  Create an instance of `CSVHandler` with a dummy file path ("dummy.csv").
5.  Call `csv_handler.read_csv()`.

**Expected Results:**

*   1) The `Data` object returned by `read_csv()` should contain 2 entries.
*   2) The first entry (key=1) should have:
        *   Requirement: "R1"
        *   Test Case: "TC1"
        *   Duration: 10.5
        *   Status: "Passed"
*   3) The second entry (key=2) should have:
        *   Requirement: "R2"
        *   Test Case: "TC2"
        *   Duration: 312.0
        *   Status: "Failed"

**Assertions:**

*   `assert data.get_size() == 2`: Asserts that the `Data` object contains 2 entries.
*   `assert data.data[1]["Requirement"] == "R1"`: Asserts the requirement of the first entry.
*   `assert data.data[1]["Test Case"] == "TC1"`: Asserts the test case of the first entry.
*   `assert data.data[1]["Duration"] == 10.5`: Asserts the duration of the first entry.
*   `assert data.data[1]["Status"] == "Passed"`: Asserts the status of the first entry.
*   `assert data.data[2]["Requirement"] == "R2"`: Asserts the requirement of the second entry.
*   `assert data.data[2]["Test Case"] == "TC2"`: Asserts the test case of the second entry.
*   `assert data.data[2]["Duration"] == 312.0`: Asserts the duration of the second entry.
*   `assert data.data[2]["Status"] == "Failed"`: Asserts the status of the second entry.

**Postconditions:**

*   The `Data` object is populated with the data read from the mocked CSV file.

**Test Code:** `test_csv_handler.py::test_read_csv_valid_file`

**Status:** Pass

**Notes:**

*   This test relies on the `pytest` framework and the `pytest-mock` plugin (`mocker` fixture).
*   The test uses a mocked file object to isolate the `read_csv` method from the actual file system.
*   The test data includes valid examples of test cases, durations (in seconds and minutes), and statuses.
*   The calculation of the duration in minutes (5.2 min => 312.0) is implicitly tested.
