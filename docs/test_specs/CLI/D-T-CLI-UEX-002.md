# Test Specification: D-T-CLI-UEX-002

**Test ID:** D-T-CLI-UEX-002

**Test Name:** CLI - Unexpected Exception

**Source:** Developer

**Module:** CLI

**Category:** Error Handling

**Related Requirements:**

*   D-21
*   D-22

**Purpose:**
This test verifies that the `cli.main()` function correctly handles unexpected exceptions raised during the execution of the core logic (`TestStatisticReadWrite.run`). It checks that the program exits with a non-zero exit code and prints an appropriate error message.

**Preconditions:**

*   1) The `os.path.isfile` function is mocked to always return `True`.
*   2) The `os.path.exists` function is mocked to always return `True`.
*   3) The `os.makedirs` function is mocked to do nothing.
*   4) The `TestStatisticReadWrite.run` method is mocked to raise a `ValueError` with the message "Something unexpected".
*   5) The `sys.argv` attribute is mocked to simulate specific command-line arguments: `['tsrw', '-i', 'sample.csv', '-o', 'out_ok']`

**Test Data:**

*   Command-line arguments: `['tsrw', '-i', 'sample.csv', '-o', 'out_ok']`
*   Input file: `sample.csv` (The file existence check is mocked, so the actual file doesn't matter).
*   Output directory: `out_ok` (The directory existence check is mocked).

**Test Steps:**

1.  Patch `os.path.isfile`, `os.path.exists`, `os.makedirs`, and `TestStatisticReadWrite.run` as described in the Preconditions.
2.  Patch `sys.argv` to simulate the command-line arguments: `['tsrw', '-i', 'sample.csv', '-o', 'out_ok']`.
3.  Execute `cli.main()` within a `pytest.raises(SystemExit)` context.
4.  Capture stdout and stderr using `capsys`.

**Expected Results:**

*   1) `cli.main()` should raise a `SystemExit` exception.
*   2) The `SystemExit` exception should have a `code` attribute equal to 1.
*   3) Either stdout or stderr should contain the string "Error: Unexpected error occurred:".

**Assertions:**

*   `with pytest.raises(SystemExit) as exc_info:`: Asserts that a `SystemExit` exception is raised.
*   `assert exc_info.value.code == 1`: Asserts that the exit code is 1.
*   `assert "Error: Unexpected error occurred:" in captured.out or "Error: Unexpected error occurred:" in captured.err`: Asserts that the error message is printed to either stdout or stderr.
*   `mock_run.assert_called_once()`: Asserts that `TestStatisticReadWrite.run` was called exactly once.

**Postconditions:**

*   The program has exited with a non-zero exit code due to an unexpected exception.

**Test Code:** `test_cli.py::test_unexpected_exception`

**Status:** Pass

**Notes:**

*   This test relies on the `pytest` framework and the `pytest-mock` plugin (`mocker` fixture).
*   The test isolates the core logic by mocking file system interactions and the `TestStatisticReadWrite.run` method.
*   The specific type of exception raised (`ValueError`) is not as important as the fact that an unexpected exception is handled correctly.
*   The error message is expected to be printed, but the exact output stream (stdout or stderr) is not strictly enforced.
