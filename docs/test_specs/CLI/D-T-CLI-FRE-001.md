# Test Specification: D-T-CLI-FRE-001

**Test ID:** D-T-CLI-FRE-001

**Test Name:** CLI - Main Friendly Exception

**Source:** Developer

**Module:** CLI

**Category:** Error Handling

**Related Requirements:**

*   D-21
*   D-22
*   D-24

**Purpose:**
This test verifies that the `cli.main()` function correctly handles `FriendlyException` exceptions raised during the execution of the core logic (`TestStatisticReadWrite.run`). It checks that the program exits with a non-zero exit code and that the exception message is printed to stdout.

**Preconditions:**

*   1) The `os.path.abspath` function is mocked to return its input argument unchanged.
*   2) The `os.path.isfile` function is mocked to always return `True`.
*   3) The `os.path.exists` function is mocked to always return `False`.
*   4) The `os.makedirs` function is mocked to do nothing.
*   5) The `atexit.register` function is mocked to prevent actual log writing.
*   6) The `TestStatisticReadWrite.run` method is mocked to raise a `FriendlyException` with a specific message.
*   7) The `sys.argv` attribute is mocked to simulate specific command-line arguments: `['tsrw', '-i', 'sample.csv', '-o', 'out_ok']`

**Test Data:**

*   Command-line arguments: `['tsrw', '-i', 'sample.csv', '-o', 'out_ok']`
*   Input file: `sample.csv` (The file existence check is mocked, so the actual file doesn't matter).
*   Output directory: `out_ok` (The directory existence check is mocked).
*   Exception message: "Mocked FriendlyException"

**Test Steps:**

1.  Patch `os.path.abspath`, `os.path.isfile`, `os.path.exists`, `os.makedirs`, `atexit.register`, and `TestStatisticReadWrite.run` as described in the Preconditions.
2.  Patch `sys.argv` to simulate the command-line arguments: `['tsrw', '-i', 'sample.csv', '-o', 'out_ok']`.
3.  Execute `cli.main()` within a `pytest.raises(SystemExit)` context.
4.  Capture stdout and stderr using `capsys`.

**Expected Results:**

*   1) `cli.main()` should raise a `SystemExit` exception.
*   2) The `SystemExit` exception should have a `code` attribute equal to 1.
*   3) Stdout should contain the message "Mocked FriendlyException".

**Assertions:**

*   `with pytest.raises(SystemExit) as exc_info:`: Asserts that a `SystemExit` exception is raised.
*   `assert exc_info.value.code == 1`: Asserts that the exit code is 1.
*   `assert msg in captured.out`: Asserts that the `FriendlyException` message is printed to stdout.

**Postconditions:**

*   The program has exited with a non-zero exit code due to a `FriendlyException`.
*   The `FriendlyException` message has been printed to stdout.

**Test Code:** `test_cli.py::test_main_friendly_exception`

**Status:** Pass

**Notes:**

*   This test relies on the `pytest` framework and the `pytest-mock` plugin (`mocker` fixture).
*   The test isolates the core logic by mocking file system interactions and the `TestStatisticReadWrite.run` method.
*   The test verifies that the exception message is printed to stdout, which is the expected behavior for `FriendlyException`.
