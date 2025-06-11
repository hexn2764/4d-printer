# usage_example.py

import os
from test_statistic_read_write.test_statistic_read_write import TestStatisticReadWrite

def run_example():
    project_root = os.path.abspath(os.path.dirname(__file__))
    csv_path = os.path.join(project_root, 'sample_data', '4d_printer_test_data.csv')
    output_folder = os.path.join(project_root, 'output')
    top_x = 50

    tsrw = TestStatisticReadWrite(
        csv_path=csv_path, 
        output_folder=output_folder, 
        top_x=top_x, 
        sort_key="Duration",                                # optional
        log_folder=os.path.join(project_root, "logs"),      # optional
        verbose=False                                       # optional 
    )
    tsrw.run()

    tsrw.csv_path = os.path.join(project_root, 'sample_data', '4d_printer_test_data.csv')
    tsrw.sort_key = "Requirement"
    tsrw.top_x = 3
    tsrw.reset()
    tsrw.run()

    # raises an exception
    # tsrw.top_x = -5

    # raises an exception
    # tsrw.csv_path = "nonexistent_foobar"

if __name__ == "__main__":
    run_example()
