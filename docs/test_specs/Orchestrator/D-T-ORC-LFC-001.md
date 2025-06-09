# Test Specification: D-T-ORC-LFC-001

**Test ID:** D-T-ORC-LFC-001

**Test Name:** Orchestrator - Log Folder Creation Failure

**Source:** Developer

**Module:** Orchestrator

**Category:** Initialization

**Related Requirements:**

*   D-21
*   D-22
*   D-24

**Purpose:**
This test verifies that the `TestStatisticReadWrite` class correctly handles failures in creating the specified log directory during initialization. It checks that an `OutputFolderError` is raised and that the error message is properly logged.

**Preconditions:**

*   1) The `os.path.isfile` function is mocked to return `True`.
*   2) The `os.path.exists` function is mocked to return `True` if path equals to "output" and `False` otherwise.
*   3) The `os.makedirs` function is mocked to raise an `OSError` when called with a path where the last component is "logdir" (simulating a permission error or similar issue).

**Test Data:**

*   `csv_path`: "input.csv" (dummy path, not actually used in this test due to mocking)
*   `output_folder`: "output" (dummy path, checked only for existence)
*   `log_folder`: "logdir" (path that will trigger the mocked `OSError`)
*   `verbose`: False

**Test Steps:**

1.  Patch `os.path.isfile` to always return `True`.
2.  Patch `os.path.exists` to return `True` for "output" and False otherwise.
3.  Patch `os.makedirs` to raise an `OSError` when called with a path ending in "logdir".
4.  Execute `TestStatisticReadWrite` initialization within a `pytest.raises(OutputFolderError)` context, passing the test data.

**Expected Results:**

*   1) The `TestStatisticReadWrite` initialization should raise an `OutputFolderError` exception.
*   2) The exception message should contain the string "Cannot create log folder 'logdir'".

**Assertions:**

*   `with pytest.raises(OutputFolderError) as exc_info:`: Asserts that an `OutputFolderError` exception is raised.
*   `assert "Cannot create log folder 'logdir'" in str(exc_info.value)`: Asserts that the exception message contains the expected error message.

**Postconditions:**

*   No folders or files are created.

**Test Code:** `test_test_statistic_read_write.py::test_log_folder_creation_fails`

**Status:** Pass

**Notes:**

*   This test relies on the `pytest` framework and the `pytest-mock` plugin (`mocker` fixture).
*   The test isolates the log folder creation logic by mocking `os.path.isfile`, `os.path.exists`, and `os.makedirs`.
*   The test uses a specific path ("logdir") to trigger the mocked error, simulating a scenario where the log folder cannot be created.
*   It assumes the constructor of `TestStatisticReadWrite` calls `os.makedirs` for creating the logging folder.
