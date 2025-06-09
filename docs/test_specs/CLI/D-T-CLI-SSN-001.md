# Test Specification: D-T-CLI-SSN-001

**Test ID:** D-T-CLI-SSN-001

**Test Name:** CLI - Success Scenario No Verbose

**Source:** Developer

**Module:** CLI

**Category:** Success Scenario

**Related Requirements:**

*   D-21
*   D-26

**Purpose:**
This test verifies that the `cli.main()` function executes successfully when provided with valid input and output arguments and no verbose flag. It checks that the core logic (`TestStatisticReadWrite.run`) is executed exactly once.

**Preconditions:**

*   1) The `os.path.isfile` function is mocked to always return `True`.
*   2) The `os.path.exists` function is mocked to always return `True`.
*   3) The `os.makedirs` function is mocked to do nothing.
*   4) The `TestStatisticReadWrite.run` method is mocked to track its invocation.
*   5) The `sys.argv` attribute is mocked to simulate specific command-line arguments: `['tsrw', '-i', 'sample.csv', '-o', 'out']`

**Test Data:**

*   Command-line arguments: `['tsrw', '-i', 'sample.csv', '-o', 'out']`
*   Input file: `sample.csv` (The file existence check is mocked, so the actual file doesn't matter).
*   Output directory: `out` (The directory existence check is mocked).

**Test Steps:**

1.  Patch `os.path.isfile`, `os.path.exists`, `os.makedirs`, and `TestStatisticReadWrite.run` as described in the Preconditions.
2.  Patch `sys.argv` to simulate the command-line arguments: `['tsrw', '-i', 'sample.csv', '-o', 'out']`.
3.  Execute `cli.main()`.

**Expected Results:**

*   1) `cli.main()` should execute without raising any exceptions.
*   2) `TestStatisticReadWrite.run` should be called exactly once.

**Assertions:**

*   `mock_run.assert_called_once()`: Asserts that `TestStatisticReadWrite.run` was called exactly once.

**Postconditions:**

*   The core logic of the application (`TestStatisticReadWrite.run`) has been executed.

**Test Code:** `test_cli.py::test_success_scenario_no_verbose`

**Status:** Pass

**Notes:**

*   This test relies on the `pytest` framework and the `pytest-mock` plugin (`mocker` fixture).
*   The test isolates the core logic by mocking file system interactions and the `TestStatisticReadWrite.run` method.
