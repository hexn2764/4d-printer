# test_statistic_read_write/_data.py

import bisect
from typing import Dict, Any, List, Tuple

class Data:
    """
    Holds:
    - data: Dict[int, Dict[str, Any]] for all valid entries.
    - sorted_ids: Dict[str, List[int]] - a dictionary of lists. Each list contains IDs of entries, sorted by the corresponding key ("Requirement", "Test Case", "Duration", "Status").
    - sorted_values: Dict[str, List[Any]] - a dictionary of lists. Each list contains the values of a specific key ("Requirement", "Test Case", "Duration", "Status"), sorted in ascending order. These lists are used for efficient insertion using `bisect`.
    - status_collections: Dict[str, List[int]] - a dictionary storing lists of entry IDs for each unique status value.
    - review_lines: List[Tuple[int, str]] - a list of tuples, each containing the line number and reason for skipping invalid lines during CSV parsing.

    The CSVHandler writes here, no one else manipulates it directly except reading.
    """

    def __init__(self):
        self.data: Dict[int, Dict[str, Any]] = {}
        self.sorted_ids: Dict[str, List[int]] = {
            "Requirement": [],
            "Test Case": [],
            "Duration": [],
            "Status": []
        }
        self.sorted_values: Dict[str, List[Any]] = {
            "Requirement": [],
            "Test Case": [],
            "Duration": [],
            "Status": []
        }
        self.status_collections: Dict[str, List[int]] = {}
        self.review_lines: List[Tuple[int, str]] = []

    def _extract_requirement_sort_key(self, req_str: str) -> Tuple[int, str, int]:
        parts = req_str.split("_")
        
        if len(parts) >= 3:
            try:
                prefix_num = int(parts[0])
            except ValueError:
                prefix_num = float('inf')
            main_part = "_".join(parts[1:-1])
            try:
                suffix_num = int(parts[-1])
            except ValueError:
                suffix_num = 0
        elif len(parts) == 2:
            try:
                prefix_num = int(parts[0])
                main_part = parts[1]
                suffix_num = 0
            except ValueError:
                prefix_num = float('inf')
                main_part = parts[0]
                try:
                    suffix_num = int(parts[1])
                except ValueError:
                    suffix_num = 0
        else:
            prefix_num = float('inf')
            main_part = req_str
            suffix_num = 0
        
        return (prefix_num, main_part, suffix_num)



    def _insert_into_sorted_index(self, index_list: List[int], value_list: List[Any], key: int, value: Any):
        """
        Helper method to insert a key-value pair into the corresponding sorted index and value list.

        Maintains both the `sorted_ids` and `sorted_values` lists in a sorted order using binary insertion.

        Args:
            index_list (List[int]): The list of IDs sorted by the corresponding value.
            value_list (List[Any]): The list of values sorted in ascending order.
            key (int): The ID of the entry being inserted.
            value (Any): The value of the field being inserted.
        """
        idx = bisect.bisect_left(value_list, value)
        value_list.insert(idx, value)
        index_list.insert(idx, key)

    def add_entry(self, key: int, entry: Dict[str, Any]):
        """
        Inserts a new record into the data dictionary and maintains sorted indexes for each field.

        Args:
            key (int): The unique ID of the entry.
            entry (Dict[str, Any]): The dictionary containing the entry's data, with keys "Requirement", "Test Case", "Duration", and "Status".
        """
        # Store the entry "as is"
        self.data[key] = entry

        req_val = entry["Requirement"]
        tc_val = entry["Test Case"]
        dur_val = entry["Duration"]
        stat_val = entry["Status"]

        self._insert_into_sorted_index(
            self.sorted_ids["Requirement"],
            self.sorted_values["Requirement"],
            key,
            self._extract_requirement_sort_key(req_val)
        )

        self._insert_into_sorted_index(
            self.sorted_ids["Test Case"],
            self.sorted_values["Test Case"],
            key,
            tc_val
        )
        self._insert_into_sorted_index(
            self.sorted_ids["Duration"],
            self.sorted_values["Duration"],
            key,
            dur_val
        )
        self._insert_into_sorted_index(
            self.sorted_ids["Status"],
            self.sorted_values["Status"],
            key,
            stat_val
        )

        # Status
        if stat_val not in self.status_collections:  
            self.status_collections[stat_val] = []
        self.status_collections[stat_val].append(key) 

        
    def get_size(self) -> int:
        return len(self.data)
