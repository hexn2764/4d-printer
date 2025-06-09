# Test Specification: D-T-CLI-SSV-001

**Test ID:** D-T-CLI-SSV-001

**Test Name:** CLI - Success Scenario With Verbose And Logfolder

**Source:** Developer

**Module:** CLI

**Category:** Success Scenario

**Related Requirements:**

*   D-21
*   D-24
*   D-26

**Purpose:**
This test verifies that the `cli.main()` function executes successfully when provided with valid input and output arguments and the verbose flag (`-v`). It checks that the core logic (`TestStatisticReadWrite.run`) is executed exactly once and that verbose logging is enabled in the `Logger`.

**Preconditions:**

*   1) The `os.path.isfile` function is mocked to always return `True`.
*   2) The `os.path.exists` function is mocked to always return `True`.
*   3) The `os.makedirs` function is mocked to do nothing.
*   4) The `TestStatisticReadWrite.run` method is mocked to track its invocation.
*   5) The `Logger.set_verbose` method is mocked to track its invocation, wrapping the original `set_verbose` method of a new `Logger` instance.
*   6) The `sys.argv` attribute is mocked to simulate specific command-line arguments: `['tsrw', '-i', 'sample.csv', '-o', 'out', '-v']`

**Test Data:**

*   Command-line arguments: `['tsrw', '-i', 'sample.csv', '-o', 'out', '-v']`
*   Input file: `sample.csv` (The file existence check is mocked, so the actual file doesn't matter).
*   Output directory: `out` (The directory existence check is mocked).

**Test Steps:**

1.  Patch `os.path.isfile`, `os.path.exists`, `os.makedirs`, `TestStatisticReadWrite.run`, and `Logger.set_verbose` as described in the Preconditions.
2.  Patch `sys.argv` to simulate the command-line arguments: `['tsrw', '-i', 'sample.csv', '-o', 'out', '-v']`.
3.  Execute `cli.main()`.

**Expected Results:**

*   1) `cli.main()` should execute without raising any exceptions.
*   2) `TestStatisticReadWrite.run` should be called exactly once.
*   3) `Logger.set_verbose` should be called exactly once with the argument `True`.

**Assertions:**

*   `mock_run.assert_called_once()`: Asserts that `TestStatisticReadWrite.run` was called exactly once.
*   `mock_set_verbose.assert_called_once_with(True)`: Asserts that `Logger.set_verbose` was called exactly once with `True`.

**Postconditions:**

*   The core logic of the application (`TestStatisticReadWrite.run`) has been executed.
*   Verbose logging has been enabled in the `Logger`.

**Test Code:** `test_cli.py::test_success_scenario_with_verbose_and_logfolder`

**Status:** Pass

**Notes:**

*   This test relies on the `pytest` framework and the `pytest-mock` plugin (`mocker` fixture).
*   The test isolates the core logic by mocking file system interactions, the `TestStatisticReadWrite.run` method, and the `Logger.set_verbose` method.
