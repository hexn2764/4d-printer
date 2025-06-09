# Test Specification: D-T-LOG-SLU-001

**Test ID:** D-T-LOG-SLU-001

**Test Name:** Logger - Set Log Folder Updates Handler

**Source:** Developer

**Module:** Logger

**Category:** Set Log Folder Updates

**Related Requirements:**

*   D-21
*   D-23
*   D-24

**Purpose:**
This test verifies that if a `FileHandler` already exists when `set_log_folder` is called, the existing handler is properly removed and closed before a new `FileHandler` is created and added for the new log folder.

**Preconditions:**

*   1) An instance of the `Logger` class is created.
*   2) The `logging.FileHandler` class is mocked.

**Test Data:**

*   `log_folder1`: A temporary directory created using `tmp_path`.
*   `log_folder2`: Another temporary directory created using `tmp_path`.

**Test Steps:**

1.  Create an instance of the `Logger` class.
2.  Create two temporary directories, `log_folder1` and `log_folder2`.
3.  Call `set_log_folder` with `log_folder1`.
4.  Reset the mocks for `FileHandler` and `addHandler`.
5.  Call `set_log_folder` with `log_folder2`.

**Expected Results:**

*   1) The first call to `set_log_folder` should create a `FileHandler` for `log_folder1`.
*   2) The second call to `set_log_folder` should remove and close the existing `FileHandler`.
*   3) The second call to `set_log_folder` should create a new `FileHandler` for `log_folder2`.

**Assertions:**

*   (First call) `mock_file_handler_cls.assert_called_once_with(str(log_folder1 / "test_statistic_read_wrte.log"))`: Asserts that `FileHandler` was called with the correct log file path for the first folder.
*   (First call) `mock_logging['mock_logger'].addHandler.assert_called()`: Asserts that `addHandler` was called for the first folder.
*   (Second call) `mock_file_handler_cls.assert_called_once_with(str(log_folder2 / "test_statistic_read_wrte.log"))`: Asserts that `FileHandler` was called with the correct log file path for the second folder.
*   (Second call) `mock_logging['mock_logger'].addHandler.assert_called()`: Asserts that `addHandler` was called for the second folder.

**Postconditions:**

*   The `Logger` instance has a `FileHandler` configured to write to a log file within the second log folder (`log_folder2`).
*   The `FileHandler` associated with the first log folder (`log_folder1`) has been removed and closed.

**Test Code:** `test_logger.py::test_set_log_folder_updates_handler`

**Status:** Pass

**Notes:**

*   This test ensures that the `Logger` class correctly manages the `FileHandler` when the log folder is changed.
*   The use of `reset_mock()` is crucial to isolate the interactions between the two calls to `set_log_folder`.
