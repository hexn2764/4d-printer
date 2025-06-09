# Test Specification: D-T-CLI-IXA-001

**Test ID:** D-T-CLI-IXA-001

**Test Name:** CLI - Invalid X Non-Integer

**Source:** Developer

**Module:** CLI

**Category:** Argument Parsing

**Related Requirements:**

*   D-12
*   D-21
*   D-22

**Purpose:**
This test verifies that the command-line interface (CLI) correctly handles invalid, non-integer values for the `-x` argument. It checks that the program exits with a non-zero exit code and prints an appropriate error message to the console.

**Preconditions:**

*   1) The `sys.argv` attribute is mocked to simulate command-line arguments.
*   2) `os.path.isfile` is mocked to return True.
*   3) `os.path.exists` is mocked to return True.
*   4) `os.makedirs` is mocked.

**Test Data:**

*   `invalid_x`: A parameterized input representing an invalid, non-integer value for the `-x` argument. Examples: "abc", "5.5".
*   Command-line arguments: `["tsrw", "-i", "input.csv", "-o", "output", "-x", <invalid_x>]`

**Test Steps:**

1.  Patch `sys.argv` to simulate the command-line arguments with the invalid `-x` value.
2.  Patch `os.path.isfile` to return True.
3.  Patch `os.path.exists` to return True.
4.  Patch `os.makedirs` to do nothing.
5.  Execute `cli.main()` within a `pytest.raises(SystemExit)` context.
6.  Capture stdout and stderr using `capsys`.

**Expected Results:**

*   1) `cli.main()` should raise a `SystemExit` exception.
*   2) The `SystemExit` exception should have a non-zero `code` attribute.
*   3) The console output (either stdout or stderr) should contain an error message indicating an invalid int value for the `-x` argument. The message should include the invalid value.
*   4) The console output (either stdout or stderr) should contain a "usage" message.

**Assertions:**

*   `with pytest.raises(SystemExit) as exc_info:`: Asserts that a `SystemExit` exception is raised.
*   `assert exc_info.value.code != 0`: Asserts that the exit code is not 0.
*   `error_message = f"error: argument -x: invalid int value: '{invalid_x}'"` and `assert error_message in captured.out or error_message in captured.err`: Asserts that the correct error message, including the invalid value, is printed to either stdout or stderr.
*   `error_message = "usage"` and `assert error_message in captured.out or error_message in captured.err`: Asserts that usage message is printed to either stdout or stderr.

**Postconditions:**

*   The program has exited with a non-zero exit code.
*   An appropriate error message has been printed to the console.

**Test Code:** `test_cli.py::test_cli_invalid_x_non_integer`

**Status:** Pass

**Notes:**

*   This test relies on the `pytest` framework, the `pytest-mock` plugin (`mocker` fixture), and the `capsys` fixture.
*   The test is parameterized using `@pytest.mark.parametrize` to run with different invalid `-x` values.
*   The test uses mocking to isolate the CLI argument parsing logic.
