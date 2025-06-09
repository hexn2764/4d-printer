# Test Specification: D-T-PAR-DPV-001

**Test ID:** D-T-PAR-DPV-001

**Test Name:** Parser - Duration Parse Valid

**Source:** Developer

**Module:** Parser

**Category:** Duration Parse Valid

**Related Requirements:**

*   D-6
*   D-9
*   D-21

**Purpose:**
This test verifies that the `DurationParser.parse` method correctly parses valid duration strings, including various time units, case insensitivity, and extra spaces. It also covers cases where the input is invalid and ensures that appropriate error messages are logged.

**Preconditions:**

*   1) A `DurationParser` instance is created.
*   2) The `Logger` class is mocked.

**Test Data:**
The test uses a parametrized set of inputs, including:
* Valid single time unit strings (e.g., "5 sec", "1.5 hour").
* Valid multiple time unit strings (e.g., "2 min 48 sec").
* Case-insensitive and extra space variations (e.g., "5 SEC", "  5   sec  ").
* Invalid format strings (e.g., "", "5", "5sec").
* Strings with unknown units (e.g., "5 seconds", "50 cent").
* Strings with repeated units (e.g., "5 sec 5 sec").
* Strings with negative or zero total duration (e.g., "-0 sec", "0 min 0 sec").
* Strings with invalid numeric values (covered in a separate test).
* Strings with unregonized component (e.g., "5 sec extra")

**Test Steps:**

1.  For each input string in the test data:
    *   Call the `DurationParser.parse` method with the input string.
    *   If the input is expected to be valid:
        *   Verify that the returned value is approximately equal to the expected duration in seconds.
    *   If the input is expected to be invalid:
        *   Verify that the returned value is `None`.
        *   Verify that the appropriate error message is logged using `mock_logger.log_error`.

**Expected Results:**

*   1) Valid duration strings are parsed correctly, returning the equivalent duration in seconds.
*   2) Invalid duration strings return `None`.
*   3) Appropriate error messages are logged for invalid inputs.

**Assertions:**

*   `assert result == pytest.approx(expected)`: Asserts that the parsed duration is approximately equal to the expected value for valid inputs.
*   `assert result is None`: Asserts that `None` is returned for invalid inputs.
*   `mock_logger.log_error.assert_called_once_with(log_message)`: Asserts that the expected error message is logged for invalid inputs.

**Postconditions:**

*   The `DurationParser` has been tested with a variety of valid and invalid inputs.
*   The `Logger` has received error messages for invalid inputs.

**Test Code:** `test_parser.py::test_duration_parser_parse`

**Status:** Pass

**Notes:**

*   This test uses `pytest.mark.parametrize` to efficiently test multiple inputs.
*   The `pytest.approx` function is used to compare floating-point numbers with a tolerance for potential rounding errors.
*   The test covers a wide range of valid and invalid scenarios to ensure the robustness of the `DurationParser`.
