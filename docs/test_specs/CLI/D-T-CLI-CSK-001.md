# Test Specification: D-T-CLI-CSK-001

**Test ID:** D-T-CLI-CSK-001

**Test Name:** CLI - Custom Sort Key

**Source:** Developer

**Module:** CLI

**Category:** Argument Parsing

**Related Requirements:**

*   D-10
*   D-20
*   D-21

**Purpose:**
This test verifies that the `cli.main()` function correctly handles a custom sort key provided via the `-s` command-line argument. It checks that the `TestStatisticReadWrite` object is initialized with the specified sort key and that the `run` method is executed.

**Preconditions:**

*   1) The `os.path.isfile` function is mocked to always return `True`.
*   2) The `os.path.exists` function is mocked to always return `True`.
*   3) The `os.makedirs` function is mocked to do nothing.
*   4) The `TestStatisticReadWrite.__init__` method is mocked to track its invocation and arguments. It returns `None` to bypass the actual initialization.
*   5) The `TestStatisticReadWrite.run` method is mocked to track its invocation.
*   6) The `sys.argv` attribute is mocked to simulate specific command-line arguments: `['tsrw', '-i', 'sample.csv', '-o', 'out_ok', '-s', 'Status']`

**Test Data:**

*   Command-line arguments: `['tsrw', '-i', 'sample.csv', '-o', 'out_ok', '-s', 'Status']`
*   Input file: `sample.csv` (The file existence check is mocked, so the actual file doesn't matter).
*   Output directory: `out_ok` (The directory existence check is mocked).
*   Sort key: `Status` (Provided via the `-s` argument).

**Test Steps:**

1.  Patch `os.path.isfile`, `os.path.exists`, `os.makedirs`, `TestStatisticReadWrite.__init__`, and `TestStatisticReadWrite.run` as described in the Preconditions.
2.  Patch `sys.argv` to simulate the command-line arguments: `['tsrw', '-i', 'sample.csv', '-o', 'out_ok', '-s', 'Status']`.
3.  Execute `cli.main()`.

**Expected Results:**

*   1) `cli.main()` should execute without raising any exceptions.
*   2) `TestStatisticReadWrite.__init__` should be called exactly once.
*   3) The `sort_key` argument passed to `TestStatisticReadWrite.__init__` should be "Status".
*   4) The `top_x` argument passed to `TestStatisticReadWrite.__init__` should be 10 (the default value).
*   5) `TestStatisticReadWrite.run` should be called exactly once.

**Assertions:**

*   `mock_init.assert_called_once()`: Asserts that `TestStatisticReadWrite.__init__` was called exactly once.
*   `assert call_kwargs["sort_key"] == "Status"`: Asserts that the `sort_key` argument passed to `TestStatisticReadWrite.__init__` is "Status".
*   `assert call_kwargs["top_x"] == 10`: Asserts that the `top_x` argument passed to `TestStatisticReadWrite.__init__` is 10.
*   `mock_run.assert_called_once()`: Asserts that `TestStatisticReadWrite.run` was called exactly once.

**Postconditions:**

*   The `TestStatisticReadWrite` object has been initialized with the custom sort key "Status" and default `top_x` value of 10.
*   The `TestStatisticReadWrite.run` method has been executed.

**Test Code:** `test_cli.py::test_custom_sort_key`

**Status:** Pass

**Notes:**

*   This test relies on the `pytest` framework and the `pytest-mock` plugin (`mocker` fixture).
*   The test isolates the core logic by mocking file system interactions and the `TestStatisticReadWrite` class's methods.
*   The specific sort key "Status" is used as an example, but the test should pass with any valid sort key.
