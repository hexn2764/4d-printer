# test_statistic_read_write/cli.py

import os
import sys
import argparse
import atexit

from test_statistic_read_write._logger import Logger
from test_statistic_read_write.test_statistic_read_write import TestStatisticReadWrite
from test_statistic_read_write._exceptions import FriendlyException


def log_end_of_session():
    """Logs an end-of-session message."""
    logger = Logger()
    logger.log_info("Execution ended.\n")

def main():
    """
    CLI entry point for the TestStatisticReadWrite (tsrw) application.

    - Parses and validates command-line arguments.
    - Configures logging based on user-specified options.
    - Initializes the TestStatisticReadWrite processor with validated arguments.
    - Executes the main processing logic.
    - Handles exceptions, providing user-friendly error messages.
    - Logs the end of the session and the location of the log file, if applicable.

    Raises:
        FriendlyException: For any errors we may expect.
        Exception: For any unexpected errors that occur during processing.
    """
    parser = argparse.ArgumentParser(
        prog="tsrw",
        description=(
        "Process test statistics from a CSV file using TestStatisticReadWrite.\n"
        "\n"
        "Example usage:\n"
        "  tsrw -i sample.csv -o output\n"
        "  tsrw -i data.csv -o results -x 5 -v\n"
        "  tsrw -i input.csv -o output -L logs\n"
        "  tsrw -i input.csv -o output -s Requirement\n"
    ),
        formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=100, width=200)
    )
    parser.add_argument(
        "-i",
        required=True,
        metavar="<input CSV>",
        help="Path to the input CSV file."
    )
    parser.add_argument(
        "-o",
        required=True,
        metavar="<output dir>",
        help="Path to the output folder for export CSV."
    )
    parser.add_argument(
        "-x",
        type=int,
        default=10,
        metavar="<num top cases>",
        help="Number of top long-running test cases to display. Default is 10."
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="If set, mirror logs to console at INFO level."
    )
    parser.add_argument(
        "-L",
        metavar="<log dir>",
        help="If specified, write logs into this folder."
    )
    parser.add_argument(
        "-s",
        metavar="<sort key>",
        default="Duration",
        dest="sort_key",
        help="Specify the key for sorting the output CSV. "
             "Valid options are 'Requirement', 'Test Case', 'Duration', 'Status' and 'none'. "
             "Default is 'Duration'."
    )

    args = parser.parse_args()
    
    # Logger
    logger = Logger()
    log_folder = None
    if args.L:
        log_folder = os.path.abspath(args.L)
        
    # Try to always catch the end of the program into the log.
    atexit.register(log_end_of_session)

    logger.log_info("CLI: Execution started.")
    try:
        tsrw = TestStatisticReadWrite(
            csv_path=os.path.abspath(args.i),
            output_folder=os.path.abspath(args.o),
            top_x=args.x,
            sort_key=args.sort_key,
            log_folder=log_folder,
            verbose=args.verbose
        )
        tsrw.run()

        if log_folder:
            # If logging is enabled, we show user where the logs ended up
            print(f"Log file is stored in: {log_folder}/test_statistic_read_wrte.log")
            logger.log_info(f"CLI: Log file is in {log_folder}/test_statistic_read_wrte.log")

    except FriendlyException as fe:
        print(f"Error: {fe.user_message}")
        logger.log_error(f"CLI caught FriendlyException: {fe.user_message}")
        sys.exit(1)

    except Exception as e:
        logger.log_error(f"CLI: Execution failed unexpectedly: {e}")
        print(f"Error: Unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

