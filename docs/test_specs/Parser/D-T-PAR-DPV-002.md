# Test Specification: D-T-PAR-DPV-002

**Test ID:** D-T-PAR-DPV-002

**Test Name:** Parser - Duration Parse Invalid numeric

**Source:** Developer

**Module:** Parser

**Category:** Duration Parse Invalid

**Related Requirements:**

*   D-6
*   D-9
*   D-21

**Purpose:**
This test verifies that the `DurationParser.parse` method correctly handles cases where the input string contains an invalid numeric value (e.g., a non-numeric string where a number is expected).

**Preconditions:**

*   1) A `DurationParser` instance is created.
*   2) The `Logger` class is mocked.
*   3) The built-in `float` function is mocked to raise a `ValueError`.

**Test Data:**

*   Input string: "5 sec" (although the specific string is less important in this case, as `float` is mocked).

**Test Steps:**

1.  Mock the built-in `float` function to raise a `ValueError` when called.
2.  Call the `DurationParser.parse` method with the input string "5 sec".

**Expected Results:**

*   1) The `DurationParser.parse` method should return `None`.
*   2) An error message should be logged indicating an invalid numeric value.

**Assertions:**

*   `assert result is None`: Asserts that `None` is returned.
*   `mock_logger.log_error.assert_called_with("DurationParser: Invalid numeric value '5' in '5 sec'")`: Asserts that the correct error message is logged.

**Postconditions:**

*   The `DurationParser` has been tested with an invalid numeric input.
*   The `Logger` has received an error message.

**Test Code:** `test_parser.py::test_duration_parser_parse_invalid_numeric`

**Status:** Pass

**Notes:**

*   This test specifically targets the error handling for invalid numeric values.
*   The `mocker` fixture is used to mock the built-in `float` function.
*   The test uses a specific input string ("5 sec"), but the actual value is less relevant because of the mocking of `float`.
*   The test implicitly assumes that the input is validated as a number before attempting to convert it to float.
