# Test Specification: D-T-LOG-SLF-001

**Test ID:** D-T-LOG-SLF-001

**Test Name:** Logger - Set Log Folder

**Source:** Developer

**Module:** Logger

**Category:** Set Log Folder

**Related Requirements:**

*   D-21
*   D-23
*   D-24

**Purpose:**
This test verifies that the `set_log_folder` method correctly sets the log folder and creates a `FileHandler` that writes to the expected log file within that folder.

**Preconditions:**

*   1) An instance of the `Logger` class is created.
*   2) The `logging.FileHandler` class is mocked to prevent actual file creation during the test.

**Test Data:**

*   `log_folder`: A temporary directory created using the `tmp_path` fixture.

**Test Steps:**

1.  Create an instance of the `Logger` class.
2.  Create a temporary directory `log_folder` using `tmp_path`.
3.  Call the `set_log_folder` method with the path to `log_folder`.

**Expected Results:**

*   1) `logging.FileHandler` should be called with the path to the log file within `log_folder`.
*   2) The `addHandler` method of the `Logger` instance should be called, indicating that the `FileHandler` was added.

**Assertions:**

*   `mock_file_handler_cls.assert_called_once_with(str(log_folder / "test_statistic_read_wrte.log"))`: Asserts that `FileHandler` was called with the correct log file path.
*   `mock_logging['mock_logger'].addHandler.assert_called()`: Asserts that `addHandler` was called on the `Logger` instance.

**Postconditions:**

*   The `Logger` instance has a `FileHandler` configured to write to a log file within the specified `log_folder`.

**Test Code:** `test_logger.py::test_set_log_folder`

**Status:** Pass

**Notes:**

*   The test uses mocks to prevent actual file I/O and to verify interactions with the `logging` module.
*   `tmp_path` is a built-in pytest fixture that provides a unique temporary directory for each test run.
