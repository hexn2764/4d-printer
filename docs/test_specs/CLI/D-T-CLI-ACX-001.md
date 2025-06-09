# Test Specification: D-T-CLI-ACX-001

**Test ID:** D-T-CLI-ACX-001

**Test Name:** CLI - Accepts Custom X

**Source:** Developer

**Module:** CLI

**Category:** Argument Parsing

**Related Requirements:**

*   D-12
*   D-21

**Purpose:**
This test verifies that the command-line interface (CLI) correctly handles a custom value for the `-x` argument (specifying the number of top entries to display) and passes it to the `TestStatisticReadWrite` class during initialization.

**Preconditions:**

*   1) The `sys.argv` attribute is mocked to simulate command-line arguments.
*   2) The `TestStatisticReadWrite` class is mocked to track its instantiation and method calls.
*   3) The `Logger` class is mocked.

**Test Data:**

*   Command-line arguments: `["tsrw", "-i", "input.csv", "-o", "output", "-x", "5"]`
*   `input.csv`: Dummy input file (not used in this test).
*   `output`: Dummy output folder (not used in this test).
*   `x`: 5 (Custom value for the number of top entries).

**Test Steps:**

1.  Patch `sys.argv` to simulate the command-line arguments, including `-x 5`.
2.  Mock the `TestStatisticReadWrite` class to track its instantiation and prevent actual execution.
3.  Call the `main()` function of the CLI.

**Expected Results:**

*   1) The `TestStatisticReadWrite` object should be instantiated with `top_x` equal to 5.
*   2) The `run` method of the mocked `TestStatisticReadWrite` instance should be called exactly once.

**Assertions:**

*   `mock_test_statistic_read_write.run.assert_called_once()`: Asserts that the `run` method was called.
*   `mock_test_statistic_read_write.top_x = 5`: Asserts that the instance was created with `top_x` equal to 5.

**Postconditions:**

*   The CLI has been executed with a custom `-x` value.
*   The `TestStatisticReadWrite` object has been initialized with the custom `top_x` value.

**Test Code:** `test_cli.py::test_cli_accepts_custom_x`

**Status:** Pass

**Notes:**

*   This test relies on the `pytest` framework and the `pytest-mock` plugin (`mocker` fixture).
*   This test isolates the CLI argument parsing logic by mocking the `TestStatisticReadWrite` class and its methods.
*   It verifies that the custom value is correctly passed during initialization.
