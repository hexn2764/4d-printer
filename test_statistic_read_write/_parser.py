# test_statistic_read_writec/_parser.py

import re
from typing import Optional, Dict, Any
from abc import ABC, abstractmethod
from ._logger import Logger

class EntryParser(ABC):
    """
    Abstract base class / interface for all parsers.
    Ensures that every parser implements the parse method.
    """

    @abstractmethod
    def parse(self, value: str) -> Optional[Any]:
        """
        Parses the input string and returns the processed value or None on error.
        Must be implemented by all subclasses.
        """
        pass

class TestCaseParser(EntryParser):
    __test__ = False
    """
    Validates and parses '<requirement>\\<test_case>' format.
    """
    def __init__(self):
        self.logger = Logger()

    def parse(self, value: str) -> Optional[Dict[str, str]]:
        r"""
        Parses a string in the format '<requirement>\<test_case>'.

        Args:
            value (str): The string to parse.

        Returns:
            Optional[Dict[str, str]]: A dictionary with 'Requirement' and 'Test Case'
            keys containing the parsed requirement and test case if the input string
            is valid. Returns None if the input string is invalid or if an error occurs
            during parsing.
        """
        if value.count("\\") != 1:
            self.logger.log_error(f"TestCaseParser: Expected exactly one backslash in '{value}'.")
            return None

        left, right = value.split("\\", 1)
        if not left.strip() or not right.strip():
            self.logger.log_error(
                f"TestCaseParser: One side of the backslash is empty in '{value}'."
            )
            return None

        return {
            "Requirement": left.strip(),
            "Test Case": right.strip()
        }

class DurationParser(EntryParser):
    """
    Parses time strings like "5 sec", "3 min 20 sec", applying checks for negativity,
    known units, zero duration, etc.
    """
    def __init__(self):
        self.logger = Logger()
        self.time_units = { # multipliers to convert into seconds
            'hr': 3600, 'hour': 3600,
            'min': 60,
            'sec': 1, 's': 1,
            'ms': 0.001, 'millisecond': 0.001,
            'ns': 1e-9, 'nanosecond': 1e-9
        }
        self.max_values = { # maximum allowed values. These can either be enforced while reading or logged as warnings.
            # Useful if a test format is unusual, e.g. 74 min 90 sec
            'hr': float('inf'), 'hour': float('inf'),
            'min': 59,
            'sec': 59, 's': 59,
            'ms': float('inf'), 'millisecond': float('inf'),
            'ns': float('inf'), 'nanosecond': float('inf')
        }
        self.pattern = re.compile(
            r'(-?\d+(\.\d+)?)\s+([a-zA-Z]+)',
            re.IGNORECASE
        )

    def parse(self, value: str) -> Optional[float]:
        """
        Parses a time string (e.g., "5 sec", "3 min 20 sec").

        Returns:
            Optional[float]: The duration in seconds if successful, None otherwise.
        """
        matches = list(self.pattern.finditer(value.lower()))
        if not matches:
            self.logger.log_error(f"DurationParser: Time format incorrect: '{value}'")
            return None

        matched_substrings = ''.join(m.group(0).replace(' ', '') for m in matches)
        stripped_input = value.lower().replace(' ', '')
        if matched_substrings != stripped_input:
            unrecognized = stripped_input.replace(matched_substrings, '')
            self.logger.log_error(
                f"DurationParser: Unrecognized components in '{value}': '{unrecognized}'"
            )
            return None

        total_seconds = 0.0
        used_units = set()

        for match in matches:
            numeric_str = match.group(1)
            unit = match.group(3)

            try:
                numeric_value = float(numeric_str)
            except ValueError:
                self.logger.log_error(f"DurationParser: Invalid numeric value '{numeric_str}' in '{value}'")
                return None

            if numeric_value < 0:
                self.logger.log_error(
                    f"DurationParser: Negative value '{numeric_value} {unit}' in '{value}'."
                )
                return None

            if unit not in self.time_units:
                self.logger.log_error(
                    f"DurationParser: Unknown unit '{unit}' in '{value}'."
                )
                return None

            if unit in used_units:
                self.logger.log_error(
                    f"DurationParser: Unit '{unit}' used multiple times in '{value}'."
                )
                return None
            used_units.add(unit)

            max_allowed = self.max_values[unit]
            if unit in ('min', 'sec', 's') and numeric_value > max_allowed:
                self.logger.log_warning(
                    f"DurationParser: '{numeric_value} {unit}' > '{max_allowed}' is unusual."
                )

            multiplier = self.time_units[unit]
            total_seconds += numeric_value * multiplier

        if total_seconds == 0.0:
            self.logger.log_error(f"DurationParser: Total duration is zero for '{value}'.")
            return None

        return total_seconds

class StatusParser(EntryParser):
    """
    Parses the Status column.
    """
    def __init__(self):
        self.logger = Logger()

    def parse(self, value: str) -> Optional[str]:
        """
        Parses a status string.

        Returns:
            Optional[str]: The stripped status string. Can return None in the future, if validity checks are applied.
        """
        return value.strip()
