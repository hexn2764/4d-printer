# Test Statistic Read and Write

This project provides a command-line tool (`tsrw`) and a Python API for reading, analyzing, and exporting test execution data from CSV files. It allows users to:

*   Read test data from a CSV file with a specific format (columns: "Test case", "Duration", "Status").
*   Analyze the data to calculate:
    *   Total number of test cases.
    *   Number of passed, failed, and other status test cases.
    *   Total execution time (duration).
    *   The top X longest-running test cases.
*   Display the analysis results on the console, either in a formatted table view or a basic list view.
*   Export the data to a new CSV file, sorted by a specified column (default: "Duration").
*   Optionally enable verbose logging to the console and/or to a log file.

The tool is designed to be used either from the command line for quick analysis or integrated into other Python scripts via its API for more complex workflows.

## 1. Project Structure

Below is the general folder and file layout of the project:

```
.
├── docs
│   ├── SRS                                 <-- Software Requirements Specification
│   ├── test_specs                          <-- Test Case Specifications
│   │   ├── ...
│   │   ├── create_spec_templates.py
│   └── uml                                 <-- UML diagrams of the project
│   └── Aufgabe_Python_en.pdf               <-- The task
├── sample_data                             <-- Given input .csv Files
├── test_statistic_read_write               <-- Source files
│   ├── ...
│   └── test_statistic_read_write.py        <-- TestStatisticReadWrite (the desired class)
├── tests                                   <-- Test files
├── LICENSE
├── pytest.ini                              <-- pytest configuration
├── README.md                               <-- This file (you are reading it here)
├── requirements.txt                        <-- Installation requirements
├── setup.py                                <-- pip install script
└── usage_example.py

```
---

## 2. Installation

Follow these steps to install and run the project:

### a) Create a Virtual Environment (Optional but Recommended)

This ensures isolated dependency management.

*   **Linux/macOS**:

    ```
    python3 -m venv .venv
    source .venv/bin/activate
    ```

*   **Windows**:

    ```
    python -m venv .venv
    .venv\Scripts\activate
    ```

### b) Install Requirements

In the project's root directory, run:

```
pip install -r requirements.txt
```

This installs all necessary packages from **requirements.txt**.

### c) Install the Package

Run:

```
pip install -e .
```

for an editable install (or `pip install .` for a standard install). This makes the `tsrw` command-line tool available.

---

## 3. Usage

The project has two modes: **Client Mode (CLI)** and **Developer Mode (API)**.

### a) Client Mode (CLI - `tsrw`)

Use the `tsrw` command to process CSV files. Run `tsrw -h` for help:

```
tsrw -h
```

**Examples:**

*   Basic: Read 'sample.csv', output to 'output', show top 10:

    ```
    tsrw -i sample_data/sample.csv -o output
    ```

*   Specify top X to display:

    ```
    tsrw -i sample_data/sample.csv -o output -x 5
    ```

*   Enable verbose logging and set a log folder:

    ```
    tsrw -i sample_data/sample.csv -o output -v -L logs
    ```

*   Choose other key than `Duration` for sorting:

    ```
    tsrw -i sample_data/sample.csv -o output -s Requirement
    ```

### b) Developer Mode (API)

Integrate directly into your code (see **usage_example.py**). Example:

```python
import os
from test_statistic_read_write.test_statistic_read_write import TestStatisticReadWrite

def run_example():
    project_root = os.path.abspath(os.path.dirname(__file__))
    csv_path = os.path.join(project_root, 'sample_data', 'TestSuite_Normal.csv')
    output_folder = os.path.join(project_root, 'output')

    tsrw = TestStatisticReadWrite(
        csv_path=csv_path,
        output_folder=output_folder,
        top_x=3,
        sort_key="Duration",                            # <--- optional
        log_folder=os.path.join(project_root, "logs"),  # <--- optional
        verbose=True                                    # <--- optional
    )
    tsrw.run()

if __name__ == "__main__":
    run_example()
```

---

## 4. Documentation

Find documentation in the **docs** folder:

*   **SRS/**: Software Requirements Specification.
*   **uml/**: UML diagrams of the architecture.
*   **test_specs/**: Detailed test specifications for each module.

---

## 5. Testing

The project uses **pytest** and **pytest-cov** for coverage reporting. In the project root, run:

```
pytest
```

The warnings can be ignored, as they caused by the name of the project folder. For coverage details, use:

```
pytest --cov=test_statistic_read_write --cov-report=html
```

This generates **htmlcov/index.html** with an interactive coverage report.

---

## 6. About `create_spec_templates.py`

**docs/test_specs/create_spec_templates.py** automates creating new test spec files/folders. It's not part of the core project and isn't directly tested. To add a template:

1.  Update the dictionary in **create_spec_templates.py**.
2.  Run the script.
3.  It generates the folder and .md template.

Use this script at your discretion, as it's not as extensively tested as the main application.

