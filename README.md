# 4D Printer: A Fun Project Done Seriously

<p align="center">
  <img src="./docs/img/header.png" alt="4D printer object result"/>
</p>

This is a fun and fictional software project, but I approached it as a serious engineering exercise. 

By applying sound engineering principles - from architecture and testing to packaging and deployment - even a simple data-processing task can be built as a robust, reusable software component. This project illustrates that process.

The 4D printer concept, story, and implementation are fictional and were developed solely for this public educational example.

This README documents the process and results.

## 1. Project Legend

Imagine the following scenario:

Hypercube Limited, a company developing novel 4D printers, is working on printers that produce objects which evolve and change their shape over time - their behavior is defined not only in three spatial dimensions, but also across time.

As a developer, you are asked to support the project by providing tools to analyze the results of printer tests.

You are given a dataset generator that simulates test results for the printer. This is perfectly acceptable: thanks to the time-independent properties of 4D models, many tests can be performed even before the physical printer is fully developed.

Hypercube Limited sends the following project specification:

> **Dear Developer**,
> 
> The data generator creates a CSV file containing the following information:
>
> - Test case: in the format <requirement>\<test case name>
> - Duration: e.g. "7.4 sec", "12 min 8 sec" (time format)
> - Status: Passed, Failed, or Unknown
> 
> Example rows:
> ```
> 15_SafetyBattery_2\StartupTest;4 millisecond 62 nanosecond;Unknown
> SynchronizationProtocol_5\MaterialTransformationTest;96 s;Failed
> 62_NavigationProtocol\Function;8 nanosecond 86 s;Unknown
> 5_NozzleSynchronizationUnit\PlatformLevelingCheck;14 millisecond;Passed
> ```
> **Your task**:
> 
> Develop a class named `TestStatisticReadWrite` in a programming language of your choice, which:
> 
> - Prints the following information to the command window:
>   - Number of test cases
>   - Number of Passed, Failed, Unknown test cases
>   - The names and runtimes of the top <X> longest-running test cases
>   - The total runtime
> 
> - Writes a new CSV with the following columns, sorted by runtime:
>   - Requirement
>   - Test case name
>   - Status
>   - Runtime (in seconds, as a plain number without time formatting)
> 
> The class should accept the following input arguments:
> 
> - Path to the input CSV
> - Path to the output folder for the new CSV
> - The number of top test cases <X>
> 
> Please implement the class as if it were to be delivered to a real customer.
> 
> Kind regards,
> 
> Hypercube Limited


## 2. How I Approached the Task

### 2.1. Requirements Mapping

I started by analyzing the client’s requirements and mapping them to **functional requirements** (FR), **non-functional requirements** (NFR), and **constraints** - to formalize the informal text provided in the task description.

For example:

- **C-FR3:** Accept input arguments for CSV paths and the number of test cases `<X>`:
  - Path to given CSV
  - Path to folder containing the new CSV
  - Number of test cases `<X>`

- **C-NFR1:** Implement the class `TestStatisticReadWrite` in a way that it can be delivered to a real customer.

After that, I mapped the client requirements to my own **developer requirements**.
Developer requirements represent an interpretation of the client's needs in technical terms.

| Client Requirement | Requirement Description | Developer Requirement | Status |
|---|---|---|---|
|...||||
| C-FR3 | Accept input arguments for CSV paths and the number of test cases `<X>`:<br>- Path to given CSV<br>- Path to folder containing the new CSV<br>- Number of test cases `<X>` | D-10, D-11, D-12 | Complete |
|...||||
| C-NFR1 | Implement the class TestStatisticReadWrite in a way that it can be delivered to a real customer. | D-21, D-22, D-23, D-24, D-25, D-26, D-27 | Complete |

Developer requirements extend the client's original requirements by adding technical points I considered necessary for a professional implementation.

For example:

Without ongoing contact with the client, it is difficult to precisely interpret what "in a way that it can be delivered to a real customer" means. This could refer to packaging and distribution, extensive documentation, robust error handling, or ensuring a sufficient level of test coverage.
Such aspects would normally be clarified through further discussion with the client.

In this case, I made several assumptions to guide the implementation:
- Since the project must be deliverable, it should include a comprehensive test suite and achieve an acceptable level of test coverage.
- The CSV datasets may contain errors; the program must handle them correctly and gracefully.
- To provide visibility into the process, the program should include logging capabilities.
- And so on.

As a result, the developer requirements include additional points that extend the original task. For example:

| Developer Requirement | Description |
|---|---|
|...||
| D-21 | The program must be fully covered by comprehensive tests. |
| D-22 | Errors and exceptions must be handled gracefully, with informative error messages provided to the user. |
| D-23 | Errors, warnings, and informational messages must be logged. |
|...||


Finally, I summarized all project requirements in the **Software Requirements Specification** (SRS) document.

Having established a clear list of requirements, I moved on to class and object design.


### 2.2 Class Diagram

<p align="center">
  <img src="./docs/uml/jpg/class_diagram_simplified.jpg" alt="Class Diagram"/>
</p>

I decided to follow two core software engineering principles:
- Separation of Concerns
- Modularity

In particular, this means that every class and method I wrote is responsible for exactly one clearly defined task.

For example:

- The `Data` class represents an in-memory information database of the CSV contents.
- The `CSVHandler` is responsible for writing to and reading from this database.
- The `Analyzer` performs analysis on the data: calculating statistics, ordering results, selecting the top-X longest-running test cases.
- The `Printer` is responsible solely for presenting the analyzed data - but no class reads, analyzes, and prints at the same time.

This architecture enables a modular design where components can be easily replaced or extended without impacting the rest of the system.

For instance, we could implement a different `Printer` that generates a PDF report instead of printing to the console - and we would not need to modify the rest of the codebase. The new printer would simply conform to the existing interface and could be plugged in seamlessly.

### 2.3. Software Patterns

I applied two software design patterns in this project:

- **Strategy Pattern**: The parsing logic follows a lightweight Strategy Pattern. Each field is parsed by an interchangeable parser object that implements a common interface (`EntryParser`). The `CSVHandler` delegates parsing to these field-specific parser strategies, enabling clear separation of concerns and making the parsing logic easily extensible.
- **Singleton Pattern**: The logging logic is implemented using a Singleton Pattern. All components of the system share a single `Logger` instance, ensuring that all log messages are written to a consistent log destination without requiring explicit coordination between classes.

### 2.4. Design Extensions

I generalized the logic of several features to make the system more flexible and maintainable.

For example, although the task explicitly required sorting the results by `Duration`, I extended the implementation to support sorting by any column, with "Duration" used as the default. This approach ensures that no code changes are required if a different sorting key is preferred in the future - only a configuration parameter needs to be adjusted.

Similarly, the parser logic was designed to be extensible. The CSV structure may evolve over time, so I implemented a polymorphic parser architecture. Each field is handled by a dedicated parser class, and new parsers can be easily added without modifying the core logic. This makes the system robust against potential changes to the CSV format.

### 2.5. Creating the Codebase 

Having the diagram, I mapped the project into code by creating the corresponding classes and populating them with methods. I documented each method with a clear docstring to explicitly state its purpose.

Whenever I noticed that a method was performing too many responsibilities, I refactored it into smaller methods, refining both the code and the class diagram accordingly.

Software engineering is an iterative process, so I made adjustments at both the design and code levels throughout development.

### 2.6. Creating Tests

My approach followed a style similar to test-driven development (TDD) - I wrote tests in parallel with the source code.

Achieving a 90-100% test coverage required writing many tests; in fact, the amount of test code now exceeds the size of the project source code. I created over 100 tests to achieve this coverage, and wrote a test specification for each test.

Each test specification has a clear identifier and description. A typical test specification header looks like this:

> **Test ID:** D-T-CLI-ACX-001
> 
> **Test Name:** CLI - Accepts Custom X
> 
> **Source:** Developer
> 
> **Module:** CLI
> 
> **Category:** Argument Parsing
> 
> **Related Requirements:**
> 
> *   D-12
> *   D-21
> 
> **Test Code:** `test_cli.py::test_cli_accepts_custom_x`
> 
> **Status:** Pass
>

This test covers requirements D-12 and D-21, and is implemented in the tests folder as follows:

```python
def test_cli_accepts_custom_x(mocker, mock_logger):
    """
    Test-ID: D-T-CLI-ACX-001
    Verifies that the CLI correctly handles a custom `<X>` value.

    This test simulates invoking the CLI with a custom integer value for the `-x` argument.
    It checks that the `TestStatisticReadWrite` class is initialized with `top_x=5`
    and that the `run` method is called exactly once.

    Args:
        mocker (pytest_mock.plugin.MockerFixture): Fixture for mocking objects.
        mock_logger (MagicMock): Fixture providing a mocked Logger instance.
    """
    mocker.patch.object(sys, "argv", ["tsrw", "-i", "input.csv", "-o", "output", "-x", "5"])
    mock_test_statistic_read_write = mocker.patch('test_statistic_read_write.cli.TestStatisticReadWrite').return_value
    
    main()
    
    mock_test_statistic_read_write.run.assert_called_once()
    mock_test_statistic_read_write.top_x = 5
```

This structure allowed me to create the following traceability logic:
- A client requirement (`C-X`) is considered **satisfied** if all corresponding developer requirements (`D-Y`) mapped to it are **complete**.
- A developer requirement is considered **complete** if all corresponding tests have a status of **Pass**.

This enables traceability from developer requirements to test cases, as shown below:

| Developer Requirement | Description | Tests | Status |
|---|---|---|---|
| D-12 | The TestStatisticReadWrite class shall accept the number of top test cases (`<X>`) as an argument (defaulting to 10). |D-T-CLI-ACX-001, D-T-CLI-DEX-001, D-T-CLI-IXA-001,  D-T-CLI-IXN-001  | Complete |


Finally, I created a test case matrix to provide a clear overview of all test cases and their current status:

| Test ID            | Description                                                                                                 | Status |
|--------------------|-------------------------------------------------------------------------------------------------------------|--------|
| D-T-CLI-ACX-001    | Verify that the CLI correctly handles and uses a custom <X> value.                                            | Pass   |
| D-T-CLI-ARG-001    | Ensure that the CLI handles missing required command-line arguments properly.                               | Pass   |


### 2.7. Packaging and Installation Pipeline

After completing the project, I packaged it as a `tsrw` Python package for installation via `pip`.

I also provided a developer mode, allowing the functionality to be integrated directly into other Python code.

The following sections contain installation instructions and usage examples.


## 3. Project Structure

Below is the general folder and file layout of the project:

```
.
├── docs
│   ├── SRS                                 <-- Software Requirements Specification
│   ├── test_specs                          <-- Test Case Specifications (per module)
│   │   ├── ...
│   │   ├── create_spec_templates.py        <-- Template generator for test specs
│   └── uml                                 <-- UML diagrams of the project
│       ├── jpg                             <-- Rendered UML diagrams (images)
│       └── puml                            <-- UML sources in PlantUML format
├── sample_data                             <-- Contains dataset generator and generated sample data
│   └── generator.py
├── test_statistic_read_write               <-- Source files
│   ├── cli.py                              <-- CLI entry point
│   ├── _csv_handler.py
│   ├── _data.py
│   ├── _logger.py
│   ├── _parser.py
│   ├── _printer.py
│   ├── _analyser.py
│   ├── _exceptions.py
│   └── test_statistic_read_write.py        <-- Main orchestrator class
├── tests                                   <-- Test files (pytest-based)
│   ├── ...
├── LICENSE
├── pyproject.toml                          <-- Build system configuration
├── pytest.ini                              <-- pytest configuration
├── README.md                               <-- Project documentation (you are reading it here)
├── requirements.txt                        <-- Installation requirements
├── setup.py                                <-- pip install script
└── usage_example.py                        <-- API usage example

```
---

## 4. Installation

To install the project, follow these steps.

All commands should be run from the project `root` directory (where `requirements.txt` and `setup.py` are located).

First, it is recommended to create a virtual environment to ensure isolated dependency management.
This prevents the project’s dependencies from affecting your global Python installation.


```
python3 -m venv .venv
source .venv/bin/activate
```

Next, install the required packages:

```
pip install -r requirements.txt
```

This installs all necessary packages from **requirements.txt**.

Finally, install the project itself as a package. For development, use an editable install:

```
pip install -e .
```

Alternatively, use:

```
pip install .
```

for a standard installation. After installation, the `tsrw` command-line tool will be available.

---

## 5. Usage

To generate test results data, use the generator:

`tsrw -g`

This will generate a dataset of fictional test results in the `sample_data` folder.
The default filename is:

```
4d_printer_test_data.csv
```

You can also specify a different filename:

```
tsrw -g "name"
```

The project supports two modes of use: **Client Mode** (CLI) and **Developer Mode** (API).

### 5.1 Client Mode (CLI - `tsrw`)

Use the `tsrw` command to process CSV files. Run `tsrw -h` for help:

```
tsrw -h
```

**Examples:**

*   Basic: Read `sample.csv`, output to `output`, show top 10:

    ```
    tsrw -i sample_data/sample.csv -o output
    ```

*   Specify `top X` to display:

    ```
    tsrw -i sample_data/sample.csv -o output -x 5
    ```

*   Enable `verbose` logging and set a log folder:

    ```
    tsrw -i sample_data/sample.csv -o output -v -L logs
    ```

*   Choose other key than `Duration` for sorting:

    ```
    tsrw -i sample_data/sample.csv -o output -s Requirement
    ```

### 5.2 Developer Mode (API)

You can also integrate `tsrw` functionality directly into your code (see `usage_example.py`).
Example:

```python
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

if __name__ == "__main__":
    run_example()
```


## 6. Testing

The project uses `pytest` for running tests, and `pytest-cov` for generating coverage reports.

From the project root directory, run:

```
pytest
```

This will automatically:
- run all tests (located in the `tests/` folder)
- generate a coverage report
- create an interactive HTML coverage report at:

```
htmlcov/index.html
```

You can open this file in your browser to explore detailed coverage results.

## 7. Conclusion

By applying professional software engineering practices - including architecture design, defensive programming, automated testing, and packaging - one ensures that the resulting solution is robust, maintainable, and ready for delivery. 

While this project began as a simple CSV processing task, it demonstrates how disciplined engineering can transform such tasks into production-quality components.

## 8. License

This project is licensed under the MIT License. See [LICENSE](./LICENSE) for details.  
Attribution is required. If you use or adapt this project, please credit the author:

    Kirill Sedow (GitHub: hexn2764, contact.kirill@proton.me)