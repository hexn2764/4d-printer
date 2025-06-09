# Test Specification: D-T-CLI-IXN-001

**Test ID:** D-T-CLI-IXN-001

**Test Name:** CLI - Invalid X Negative

**Source:** Developer

**Module:** CLI

**Category:** Argument Parsing

**Related Requirements:**

*   D-12
*   D-21
*   D-22

**Purpose:**
This test verifies that the command-line interface (CLI) correctly handles a negative integer value for the `-x` argument. It checks that the program exits with a non-zero exit code and prints an appropriate error message to the console.

**Preconditions:**

*   1) The `sys.argv` attribute is mocked to simulate command-line arguments.
*   2) `os.path.isfile` is mocked to return True.
*   3) `os.path.exists` is mocked to return True.
*   4) `os.makedirs` is mocked.

**Test Data:**

*   `invalid_x`: "-1" (a string representing a negative integer value for the `-x` argument).
*   Command-line arguments: `["tsrw", "-i", "input.csv", "-o", "output", "-x", "-1"]`

**Test Steps:**

1.  Patch `sys.argv` to simulate the command-line arguments with the negative `-x` value.
2.  Patch `os.path.isfile` to return True.
3.  Patch `os.path.exists` to return True.
4.  Patch `os.makedirs` to do nothing.
5.  Execute `cli.main()` within a `pytest.raises(SystemExit)` context.
6.  Capture stdout and stderr using `capsys`.

**Expected Results:**

*   1) `cli.main()` should raise a `SystemExit` exception.
*   2) The `SystemExit` exception should have a non-zero `code` attribute.
*   3) The console output (either stdout or stderr) should contain an error message indicating an invalid `top_x` value. The message should include the invalid value (-1).

**Assertions:**

*   `with pytest.raises(SystemExit) as exc_info:`: Asserts that a `SystemExit` exception is raised.
*   `assert exc_info.value.code != 0`: Asserts that the exit code is not 0.
*   `error_message = f"Error: Invalid top_x value: {invalid_x}"` and `assert error_message in captured.err or error_message in captured.out`: Asserts that the correct error message, including the invalid value, is printed to either stdout or stderr.

**Postconditions:**

*   The program has exited with a non-zero exit code.
*   An appropriate error message has been printed to the console.

**Test Code:** `test_cli.py::test_cli_invalid_x_negative`

**Status:** Pass

**Notes:**

*   This test relies on the `pytest` framework, the `pytest-mock` plugin (`mocker` fixture), and the `capsys` fixture.
*   The test uses mocking to isolate the CLI argument parsing logic.
