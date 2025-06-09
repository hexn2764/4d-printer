# test_statistic_read_write/_analyser.py

from typing import Dict, Any, List, Tuple
from ._data import Data
from ._exceptions import InvalidTopX
from ._logger import Logger

class Analyser:
    """
    Performs analysis of Data. The results are passed to Printer.
    """

    def __init__(self):
        self.logger = Logger()

    def analyze(self, data: Data, top_x: int) -> Dict[str, Any]:
        """
        Access point called from outside. It orchestrates the analysis by calling
        private sub-methods and aggregates their results into a dictionary.

        Args:
            data (Data): The data object containing the information to be analyzed.
            top_x (int): The number of top entries to retrieve based on duration.

        Returns:
            Dict[str, Any]: A dictionary with analysis results:
            {
                "total_duration": float,                                        # The total duration of all entries.
                "top_x_entries": List[Tuple[int, Dict[str, Any]]]               # A list of tuples, where each tuple contains
                                                                                # the ID of an entry and a dictionary representing
                                                                                # the entry's data.
                "test_case_counts": Tuple[int, int, int],                       # (total_test_cases, valid_test_cases, skipped_lines)
                "status_counts": Dict[str, int]                                 # A dictionary where keys are statuses and values
                                                                                # are the corresponding counts.
            }
        """

        if not isinstance(top_x, int) or top_x < 0:
            self.logger.log_error(f"Analyser: Invalid top_x value: {top_x}. Must be a non-negative integer.")
            raise InvalidTopX(f"Invalid top_x value: {top_x}. Must be a non-negative integer.")

        total_duration = self._get_total_duration(data)
        top_x_entries = self._get_top_x_entries(data, top_x)
        test_case_counts = self._get_test_case_counts(data)
        status_counts = self._get_status_counts(data)

        return {
            "total_duration": total_duration,
            "top_x_entries": top_x_entries,
            "test_case_counts": test_case_counts,
            "status_counts": status_counts
        }

    def _get_total_duration(self, data: Data) -> float:
        """
        Calculates the total duration from the data.
        
        Args:
            data (Data): The data object containing duration values.
        
        Returns:
            float: The sum of all duration values.
        """
        return sum(data.sorted_values.get("Duration"))

    def _get_top_x_entries(self, data: Data, top_x: int) -> List[Tuple[int, Dict[str, Any]]]:
        """
        Retrieves the top X entries with the longest durations.

        Args:
            data (Data): The data object containing sorted duration indices.
            top_x (int): The number of top entries to retrieve.

        Returns:
            List[Tuple[int, Dict[str, Any]]]:                                   # A list of tuples, each containing an ID and its associated data
            or                                                                  # from the `data.data` dictionary.
            []                                                                  # if top_x <= 0
        """

        if top_x <= 0 or not data.sorted_ids.get("Duration"):
            return []
        else:
            slice_part = data.sorted_ids.get("Duration")[-top_x:]
            top_sorted_ids = list(reversed(slice_part))

            top_entries = [(cid, data.data[cid]) for cid in top_sorted_ids]

            return top_entries

    def _get_test_case_counts(self, data: Data) -> Tuple[int, int, int]:
        """
        Gets the total number of test cases, number of valid entries, and the number of skipped lines.

        Args:
            data (Data): The data object.

        Returns:
            Tuple[int, int, int]: A tuple containing:
                                - the total number of test cases,
                                - the number of valid test cases,
                                - the number of skipped lines.
        """
        valid_test_cases = len(data.data)
        skipped_lines = len(data.review_lines)
        total_test_cases = valid_test_cases + skipped_lines
        return total_test_cases, valid_test_cases, skipped_lines


    def _get_status_counts(self, data: Data) -> Dict[str, int]:
        """
        Counts the occurrences of each status in the data.

        Args:
            data (Data): The data object.

        Returns:
            Dict[str, int]: A dictionary where keys are statuses and values are their counts.
        """
        return {status: len(ids) for status, ids in data.status_collections.items()}
