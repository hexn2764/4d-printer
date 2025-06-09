tests_info = {
    # Analyser
    "D-T-AN-AN-001": {
        "Test Name": "Analyser - Analyze",
        "Source": "Developer",
        "Module": "Analyser",
        "Category": "Analyze",
        "Test Code": "test_analyser.py::test_analyze"
    },
    "D-T-AN-AN-002": {
        "Test Name": "Analyser - Analyze",
        "Source": "Developer",
        "Module": "Analyser",
        "Category": "Analyze",
        "Test Code": "test_analyser.py::test_analyze_negative_top_x"
    },
    "D-T-AN-GDU-001": {
        "Test Name": "Analyser - Get Total Duration",
        "Source": "Developer",
        "Module": "Analyser",
        "Category": "Get Duration",
        "Test Code": "test_analyser.py::test_get_total_duration"
    },
    "D-T-AN-GTX-001": {
        "Test Name": "Analyser - Get Top X Entries",
        "Source": "Developer",
        "Module": "Analyser",
        "Category": "Get Top X",
        "Test Code": "test_analyser.py::test_get_top_x_entries"
    },
    "D-T-AN-GTX-002": {
        "Test Name": "Analyser - Get Top X Entries Empty",
        "Source": "Developer",
        "Module": "Analyser",
        "Category": "Get Top X",
        "Test Code": "test_analyser.py::test_get_top_x_entries_empty"
    },
    "D-T-AN-GTX-003": {
        "Test Name": "Analyser - Get Top X Entries X Larger Than Data Size",
        "Source": "Developer",
        "Module": "Analyser",
        "Category": "Get Top X",
        "Test Code": "test_analyser.py::test_get_top_x_entries_x_larger_than_data_size"
    },
    "D-T-AN-GTX-004": {
        "Test Name": "Analyser - Get Zero Top X Entries",
        "Source": "Developer",
        "Module": "Analyser",
        "Category": "Get Top X",
        "Test Code": "test_analyser.py::test_analyser.py::test_get_zero_top_x_entries"
    },
    


    # CLI
    "D-T-CLI-ACX-001": {
        "Test Name": "CLI - Accepts Custom X",
        "Source": "Developer",
        "Module": "CLI",
        "Category": "Argument Parsing",
        "Test Code": "test_cli.py::test_cli_accepts_custom_x"
    },
    "D-T-CLI-ARG-001": {
        "Test Name": "CLI - Argparse Missing Required",
        "Source": "Developer",
        "Module": "CLI",
        "Category": "Argument Parsing",
        "Test Code": "test_cli.py::test_argparse_missing_required"
    },
    "D-T-CLI-CSK-001": {
        "Test Name": "CLI - Custom Sort Key",
        "Source": "Developer",
        "Module": "CLI",
        "Category": "Custom Sort Key",
        "Test Code": "test_cli.py::test_custom_sort_key"
    },
    "D-T-CLI-DEX-001": {
        "Test Name": "CLI - Default X",
        "Source": "Developer",
        "Module": "CLI",
        "Category": "Argument Parsing",
        "Test Code": "test_cli.py::test_cli_default_x"
    },
    "D-T-CLI-FRE-001": {
        "Test Name": "CLI - Main Friendly Exception",
        "Source": "Developer",
        "Module": "CLI",
        "Category": "Friendly Exception",
        "Test Code": "test_cli.py::test_main_friendly_exception"
    },
    "D-T-CLI-IXA-001": {
        "Test Name": "CLI - Invalid X Non-Integer",
        "Source": "Developer",
        "Module": "CLI",
        "Category": "Argument Parsing",
        "Test Code": "test_cli.py::test_cli_invalid_x_non_integer"
    },
    "D-T-CLI-IXN-001": {
        "Test Name": "CLI - Invalid X Negative",
        "Source": "Developer",
        "Module": "CLI",
        "Category": "Argument Parsing",
        "Test Code": "test_cli.py::test_cli_invalid_x_negative"
    },
    "D-T-CLI-LES-001": {
        "Test Name": "CLI - Log End Of Session",
        "Source": "Developer",
        "Module": "CLI",
        "Category": "Log End of Session",
        "Test Code": "test_cli.py::test_log_end_of_session"
    },
    "D-T-CLI-SSN-001": {
        "Test Name": "CLI - Success Scenario No Verbose",
        "Source": "Developer",
        "Module": "CLI",
        "Category": "Success Scenario No Verbose",
        "Test Code": "test_cli.py::test_success_scenario_no_verbose"
    },
    "D-T-CLI-SSV-001": {
        "Test Name": "CLI - Success Scenario With Verbose And Logfolder",
        "Source": "Developer",
        "Module": "CLI",
        "Category": "Success Scenario Verbose",
        "Test Code": "test_cli.py::test_success_scenario_with_verbose_and_logfolder"
    },
    "D-T-CLI-UEX-002": {
        "Test Name": "CLI - Unexpected Exception",
        "Source": "Developer",
        "Module": "CLI",
        "Category": "Unexpected Exception",
        "Test Code": "test_cli.py::test_unexpected_exception"
    },


    # CSV Handler
    "D-T-CSV-EXC-001": {
        "Test Name": "CSV Handler - Export CSV Valid",
        "Source": "Developer",
        "Module": "CSV Handler",
        "Category": "Export CSV",
        "Test Code": "test_csv_handler.py::test_export_csv_valid"
    },
    "D-T-CSV-EXC-003": {
        "Test Name": "CSV Handler - Export CSV File Write Error",
        "Source": "Developer",
        "Module": "CSV Handler",
        "Category": "Export CSV",
        "Test Code": "test_csv_handler.py::test_export_csv_file_write_error"
    },
    "D-T-CSV-LRV-001": {
        "Test Name": "CSV Handler- Log Review Lines",
        "Source": "Developer",
        "Module": "CSV Handler",
        "Category": "Logging",
        "Test Code": "test_csv_handler.py::test_log_review_lines"
    },
    "D-T-CSV-RDC-001": {
        "Test Name": "CSV Handler - Read CSV Valid File",
        "Source": "Developer",
        "Module": "CSV Handler",
        "Category": "Read CSV",
        "Test Code": "test_csv_handler.py::test_read_csv_valid_file"
    },
    "D-T-CSV-RDC-002": {
        "Test Name": "CSV Handler - Read CSV File Not Found",
        "Source": "Developer",
        "Module": "CSV Handler",
        "Category": "Read CSV",
        "Test Code": "test_csv_handler.py::test_read_csv_file_not_found"
    },
    "D-T-CSV-RDC-003": {
        "Test Name": "CSV Handler - Read CSV Empty File",
        "Source": "Developer",
        "Module": "CSV Handler",
        "Category": "Read CSV",
        "Test Code": "test_csv_handler.py::test_read_csv_empty_file"
    },
    "D-T-CSV-RDC-004": {
        "Test Name": "CSV Handler - Read CSV Invalid Header Columns",
        "Source": "Developer",
        "Module": "CSV Handler",
        "Category": "Read CSV",
        "Test Code": "test_csv_handler.py::test_read_csv_invalid_header_columns"
    },
    "D-T-CSV-RDC-005": {
        "Test Name": "CSV Handler - Read CSV Invalid Header Format",
        "Source": "Developer",
        "Module": "CSV Handler",
        "Category": "Read CSV",
        "Test Code": "test_csv_handler.py::test_read_csv_invalid_header_format"
    },
    "D-T-CSV-RDC-006": {
        "Test Name": "CSV Handler - Read CSV No Data Lines",
        "Source": "Developer",
        "Module": "CSV Handler",
        "Category": "Read CSV",
        "Test Code": "test_csv_handler.py::test_read_csv_no_data_lines"
    },
    "D-T-CSV-RDC-007": {
        "Test Name": "CSV Handler - Read CSV No Valid Lines",
        "Source": "Developer",
        "Module": "CSV Handler",
        "Category": "Read CSV",
        "Test Code": "test_csv_handler.py::test_read_csv_no_valid_lines"
    },
    "D-T-CSV-RDC-008": {
        "Test Name": "CSV Handler - Read CSV Skip Lines With Incorrect Number Of Columns",
        "Source": "Developer",
        "Module": "CSV Handler",
        "Category": "Read CSV",
        "Test Code": "test_csv_handler.py::test_read_csv_skip_lines_with_incorrect_number_of_columns"
    },
    "D-T-CSV-RDC-009": {
        "Test Name": "CSV Handler - Read CSV Skip Lines With Empty Fields",
        "Source": "Developer",
        "Module": "CSV Handler",
        "Category": "Read CSV",
        "Test Code": "test_csv_handler.py::test_read_csv_skip_lines_with_empty_fields"
    },
    "D-T-CSV-RDC-010": {
        "Test Name": "CSV Handler - Read CSV Skip Lines With Parse Errors",
        "Source": "Developer",
        "Module": "CSV Handler",
        "Category": "Read CSV",
        "Test Code": "test_csv_handler.py::test_read_csv_skip_lines_with_parse_errors"
    },
    "D-T-CSV-RDC-011": {
        "Test Name": "CSV Handler - Read CSV Status Parser Returns None",
        "Source": "Developer",
        "Module": "CSV Handler",
        "Category": "Read CSV",
        "Test Code": "test_csv_handler.py::test_read_csv_status_parser_returns_none"
    },

    # Data
    "D-T-DAT-AEW-001": {
        "Test Name": "Data - Add Entries With Same Values",
        "Source": "Developer",
        "Module": "Data",
        "Category": "Add Entries with same values",
        "Test Code": "test_data.py::test_add_entries_with_same_values"
    },
    "D-T-DAT-AME-001": {
        "Test Name": "Data - Add Multiple Entries Sorted",
        "Source": "Developer",
        "Module": "Data",
        "Category": "Add Multiple Entries",
        "Test Code": "test_data.py::test_add_multiple_entries_sorted"
    },
    "D-T-DAT-ASE-001": {
        "Test Name": "Data - Add Single Entry",
        "Source": "Developer",
        "Module": "Data",
        "Category": "Add Single Entry",
        "Test Code": "test_data.py::test_add_single_entry"
    },
    "D-T-DAT-CSC-001": {
        "Test Name": "Data - Count Statuses",
        "Source": "Developer",
        "Module": "Data",
        "Category": "Status Counts",
        "Test Code": "test_data.py::test_data_counts_statuses"
    },
    "D-T-DAT-INI-001": {
        "Test Name": "Data - Initial State",
        "Source": "Developer",
        "Module": "Data",
        "Category": "Initial State",
        "Test Code": "test_data.py::test_initial_state"
    },

    # Logger
    "D-T-LOG-EMS-001": {
        "Test Name": "Logger - Log Empty String",
        "Source": "Developer",
        "Module": "Logger",
        "Category": "Empty String",
        "Test Code": "test_logger.py::test_log_empty_string"
    },
    "D-T-LOG-ERR-001": {
        "Test Name": "Logger - Log Error",
        "Source": "Developer",
        "Module": "Logger",
        "Category": "Log Error",
        "Test Code": "test_logger.py::test_log_error"
    },
    "D-T-LOG-INF-001": {
        "Test Name": "Logger - Log Info",
        "Source": "Developer",
        "Module": "Logger",
        "Category": "Log Info",
        "Test Code": "test_logger.py::test_log_info"
    },
    "D-T-LOG-SIN-001": {
        "Test Name": "Logger - Singleton Behavior",
        "Source": "Developer",
        "Module": "Logger",
        "Category": "Singleton",
        "Test Code": "test_logger.py::test_singleton_behavior"
    },
    "D-T-LOG-SLF-001": {
        "Test Name": "Logger - Set Log Folder",
        "Source": "Developer",
        "Module": "Logger",
        "Category": "Set Log Folder",
        "Test Code": "test_logger.py::test_set_log_folder"
    },
    "D-T-LOG-SLU-001": {
        "Test Name": "Logger - Set Log Folder Updates Handler",
        "Source": "Developer",
        "Module": "Logger",
        "Category": "Set Log Folder Updates",
        "Test Code": "test_logger.py::test_set_log_folder_updates_handler"
    },
    "D-T-LOG-SPC-001": {
        "Test Name": "Logger - Log Special Characters",
        "Source": "Developer",
        "Module": "Logger",
        "Category": "Special Characters",
        "Test Code": "test_logger.py::test_log_special_characters"
    },
    "D-T-LOG-SVD-001": {
        "Test Name": "Logger - Set Verbose Disabled",
        "Source": "Developer",
        "Module": "Logger",
        "Category": "Set Verbose Disabled",
        "Test Code": "test_logger.py::test_set_verbose_disabled"
    },
    "D-T-LOG-SVE-001": {
        "Test Name": "Logger - Set Verbose Enabled",
        "Source": "Developer",
        "Module": "Logger",
        "Category": "Set Verbose Enabled",
        "Test Code": "test_logger.py::test_set_verbose_enabled"
    },
    "D-T-LOG-WAR-001": {
        "Test Name": "Logger - Log Warning",
        "Source": "Developer",
        "Module": "Logger",
        "Category": "Log Warning",
        "Test Code": "test_logger.py::test_log_warning"
    },

    # tsrw, orchestrator
    "D-T-ORC-LFC-001": {
        "Test Name": "Orchestrator - Log Folder Creation Failure",
        "Source": "Developer",
        "Module": "Orchestrator",
        "Category": "Initialization",
        "Test Code": "test_test_statistic_read_write.py::test_log_folder_creation_fails"
    },
    "D-T-ORC-OFC-001": {
        "Test Name": "Orchestrator - Output Folder Creation Failure",
        "Source": "Developer",
        "Module": "Orchestrator",
        "Category": "Initialization",
        "Test Code": "test_test_statistic_read_write.py::test_output_folder_creation_fails"
    },
    "D-T-ORC-RFE-001": {
        "Test Name": "Orchestrator - Run Friendly Exception at Read",
        "Source": "Developer",
        "Module": "Orchestrator",
        "Category": "Run Friendly Exception at Read",
        "Test Code": "test_test_statistic_read_write.py::test_run_friendly_exception_at_read"
    },
    "D-T-ORC-RFE-002": {
        "Test Name": "Orchestrator - Run Friendly Exception at Export",
        "Source": "Developer",
        "Module": "Orchestrator",
        "Category": "Run Friendly Exception at Export",
        "Test Code": "test_test_statistic_read_write.py::test_run_friendly_exception_at_export"
    },
    "D-T-ORC-RUE-001": {
        "Test Name": "Orchestrator - Run Unexpected Exception",
        "Source": "Developer",
        "Module": "Orchestrator",
        "Category": "Run Unexpected Exception",
        "Test Code": "test_test_statistic_read_write.py::test_run_unexpected_exception"
    },    
    "D-T-ORC-SSK-001": {
        "Test Name": "Orchestrator - Set Sort Key",
        "Source": "Developer",
        "Module": "Orchestrator",
        "Category": "Set Sort Key",
        "Test Code": "test_test_statistic_read_write.py::test_set_sort_key"
    },


    # Parser
    "D-T-PAR-DPV-001": {
        "Test Name": "Parser - Duration Parse Valid",
        "Source": "Developer",
        "Module": "Parser",
        "Category": "Duration Parse Valid",
        "Test Code": "test_parser.py::test_duration_parser_parse"
    },
    "D-T-PAR-DPV-002": {
        "Test Name": "Parser - Duration Parse Invalid numeric",
        "Source": "Developer",
        "Module": "Parser",
        "Category": "Duration Parse Invalid",
        "Test Code": "test_parser.py::test_duration_parser_parse_invalid_numeric"
    },
    "D-T-PAR-SPE-001": {
        "Test Name": "Parser - Status Parse Empty",
        "Source": "Developer",
        "Module": "Parser",
        "Category": "Status Parse Empty",
        "Test Code": "test_parser.py::test_status_parser_empty"
    },
    "D-T-PAR-SPS-001": {
        "Test Name": "Parser - Status Parse Spaces",
        "Source": "Developer",
        "Module": "Parser",
        "Category": "Status Parse Spaces",
        "Test Code": "test_parser.py::test_status_parser_spaces"
    },
    "D-T-PAR-SPV-001": {
        "Test Name": "Parser - Status Parse Valid",
        "Source": "Developer",
        "Module": "Parser",
        "Category": "Status Parse Valid",
        "Test Code": "test_parser.py::test_status_parser_valid"
    },
    "D-T-PAR-TCE-001": {
        "Test Name": "Parser - Test Case Empty",
        "Source": "Developer",
        "Module": "Parser",
        "Category": "Test Case Empty",
        "Test Code": "test_parser.py::test_test_case_parser_empty_part"
    },
    "D-T-PAR-TCI-001": {
        "Test Name": "Parser - Test Case Invalid",
        "Source": "Developer",
        "Module": "Parser",
        "Category": "Test Case Invalid",
        "Test Code": "test_parser.py::test_test_case_parser_invalid_format"
    },
    "D-T-PAR-TCV-001": {
        "Test Name": "Parser - Test Case Valid",
        "Source": "Developer",
        "Module": "Parser",
        "Category": "Test Case Valid",
        "Test Code": "test_parser.py::test_test_case_parser_valid"
    },
    "D-T-PAR-TCV-002": {
        "Test Name": "Parser - Test Case Valid with spaces",
        "Source": "Developer",
        "Module": "Parser",
        "Category": "Test Case Valid",
        "Test Code": "test_parser.py::test_test_case_parser_valid_spaces"
    },


    # Printer
    "D-T-PRI-DAO-001": {
        "Test Name": "Printer - Do Advanced Output",
        "Source": "Developer",
        "Module": "Printer",
        "Category": "Do Advanced Output",
        "Test Code": "test_printer.py::test_do_advanced_output"
    },
    "D-T-PRI-DBO-001": {
        "Test Name": "Printer - Do Basic Output",
        "Source": "Developer",
        "Module": "Printer",
        "Category": "Do Basic Output",
        "Test Code": "test_printer.py::test_do_basic_output"
    },
    "D-T-PRI-DRF-001": {
        "Test Name": "Printer - Display Results with Formatting",
        "Source": "Developer",
        "Module": "Printer",
        "Category": "Display Results with Formatting",
        "Test Code": "test_printer.py::test_display_results_with_formatting"
    },
    "D-T-PRI-DRN-001": {
        "Test Name": "Printer - Display Results No Entries",
        "Source": "Developer",
        "Module": "Printer",
        "Category": "Display Results No Entries",
        "Test Code": "test_printer.py::test_display_results_no_entries"
    },
    "D-T-PRI-DRN-002": {
        "Test Name": "Printer - Display Results No Formatting",
        "Source": "Developer",
        "Module": "Printer",
        "Category": "Display Results No Formatting",
        "Test Code": "test_printer.py::test_display_results_no_formatting"
    },
    "D-T-PRI-GWD-001": {
        "Test Name": "Printer - Get Width",
        "Source": "Developer",
        "Module": "Printer",
        "Category": "Get Width",
        "Test Code": "test_printer.py::test_get_width"
    },
    "D-T-PRI-GWE-001": {
        "Test Name": "Printer - Get Width Empty data",
        "Source": "Developer",
        "Module": "Printer",
        "Category": "Get Width Empty data",
        "Test Code": "test_printer.py::test_get_width_empty_data"
    },
    "D-T-PRI-GWL-001": {
        "Test Name": "Printer - Get Width Longer values",
        "Source": "Developer",
        "Module": "Printer",
        "Category": "Get Width Longer values",
        "Test Code": "test_printer.py::test_get_width_with_longer_data_values"
    },
}

import os

def process_test_entry(test_id, test_data, base_dir="docs/test_specs"):
    """
    Processes a single test entry from the tests_info dictionary.

    Args:
        test_id (str): The unique ID of the test case (e.g., "D-T-AN-GDU-001").
        test_data (dict): The dictionary containing test data for the given ID.
        base_dir (str): The base directory where test specifications are stored.
    """
    module_dir = create_module_directory(test_id, test_data, base_dir)
    file_path = create_test_spec_file(test_id, module_dir)

    if file_path:  # Only proceed if the file was newly created
        template = create_test_spec_template(test_id, test_data)
        write_template_to_file(file_path, template)

def create_module_directory(test_id, test_data, base_dir):
    """
    Creates a directory for the module if it doesn't exist.

    Args:
        test_id: unused
        test_data (dict): The dictionary containing test data.
        base_dir (str): The base directory where test specifications are stored.

    Returns:
        str: The path to the module directory.
    """
    module_name = test_data["Module"]
    module_dir = os.path.join(base_dir, module_name)
    os.makedirs(module_dir, exist_ok=True)
    return module_dir

def create_test_spec_file(test_id, module_dir):
    """
    Creates an .md file for the test specification if it doesn't exist.

    Args:
        test_id (str): The unique ID of the test case.
        module_dir (str): The path to the module directory.

    Returns:
        str or None: The path to the newly created file, or None if the file already exists.
    """
    file_path = os.path.join(module_dir, f"{test_id}.md")
    if not os.path.exists(file_path):
        return file_path
    else:
        return None

def create_test_spec_template(test_id, test_data):
    """
    Creates a test specification template filled with data from the test entry.

    Args:
        test_id (str): The unique ID of the test case.
        test_data (dict): The dictionary containing test data.

    Returns:
        str: The filled-in test specification template.
    """
    template = f"""# Test Specification: {test_id}

**Test ID:** {test_id}

**Test Name:** {test_data["Test Name"]}

**Source:** {test_data["Source"]}

**Module:** {test_data["Module"]}

**Category:** {test_data["Category"]}

**Related Requirements:**

*   [Requirement ID 1]
*   [Requirement ID 2]

**Purpose:**
<Description of the objective of this test>

**Preconditions:**

*   1) ...
*   2) ...

**Test Data:**

<Description of any specific input data used in this test>

**Test Steps:**

1.  <Step 1>
2.  <Step 2>
3.  <Step 3>

**Expected Results:**

*   <Expected Result 1>
*   <Expected Result 2>
*   <Expected Result 3>

**Assertions:**

*   `assert condition1`: <Description of assertion 1>
*   `assert condition2`: <Description of assertion 2>

**Postconditions:**

<Description of the state of the system after the test execution>

**Test Code:** {test_data["Test Code"]}

**Status:** [Pass/Fail/Not Executed]

**Notes:**

<Any additional notes or explanations>
"""
    return template

def write_template_to_file(file_path, template):
    """
    Writes the test specification template to the specified file.

    Args:
        file_path (str): The path to the file where the template should be written.
        template (str): The test specification template.
    """
    with open(file_path, "w") as f:
        f.write(template)

# Populate
for test_id, test_data in tests_info.items():
    process_test_entry(test_id, test_data)
