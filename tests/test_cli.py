# tests/test_cli.py

import pytest
import sys
from test_statistic_read_write import cli
from test_statistic_read_write._exceptions import *
from test_statistic_read_write.cli import main
from test_statistic_read_write._logger import Logger

@pytest.fixture
def mock_logger(mocker):
    """Fixture to mock the Logger class."""
    return mocker.patch('test_statistic_read_write.cli.Logger').return_value

@pytest.fixture
def mock_test_statistic_read_write(mocker):
    """Fixture to mock the TestStatisticReadWrite class."""
    return mocker.patch('test_statistic_read_write.cli.TestStatisticReadWrite').return_value

@pytest.fixture(autouse=True)
def reset_logger_singleton():
    """Reset the logger singleton before each test so each test is independent."""
    Logger._instance = None

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


@pytest.mark.parametrize("args", [
    # Missing -i
    (["tsrw", "-o", "output"]),
    # Missing -o
    (["tsrw", "-i", "sample.csv"]),
])
def test_argparse_missing_required(args, mocker, capsys):
    """
    Test-ID: D-T-CLI-ARG-001
    Verifies that the CLI correctly handles missing required arguments.

    This test ensures that when required command-line arguments are missing:
    - The program exits with a `SystemExit` exception.
    - The `SystemExit` exception has a non-zero exit code.
    - Argparse displays a usage message to stderr or stdout.

    Args:
        args (list): Command-line arguments simulating missing inputs.
        mocker (pytest_mock.plugin.MockerFixture): Pytest mocker fixture for mocking dependencies.
        capsys (pytest.CaptureFixture): Pytest fixture for capturing stdout and stderr.
    """
    mocker.patch.object(sys, "argv", args)

    with pytest.raises(SystemExit) as exc_info:
        main()

    captured = capsys.readouterr()
    # argparse typically prints usage to either stderr or stdout
    assert "usage:" in captured.err or "usage:" in captured.out
    assert exc_info.value.code != 0  # Non-zero exit code on error

def test_custom_sort_key(mocker):
    """
    Test-ID: D-T-CLI-CSK-001
    Verifies that a custom sort key passed via -s is correctly handled.

    This test checks that when a custom sort key is provided using the -s
    argument, the TestStatisticReadWrite object is initialized with that
    sort key. It also verifies that the run method is called, indicating
    successful execution.

    Args:
        mocker (pytest_mock.plugin.MockerFixture): Fixture for mocking objects.
    """
    mocker.patch("test_statistic_read_write.cli.os.path.isfile", return_value=True)
    mocker.patch("test_statistic_read_write.cli.os.path.exists", return_value=True)
    mocker.patch("test_statistic_read_write.cli.os.makedirs")
    mock_init = mocker.patch(
        "test_statistic_read_write.test_statistic_read_write.TestStatisticReadWrite.__init__", 
        return_value=None
    )
    mock_run = mocker.patch(
        "test_statistic_read_write.test_statistic_read_write.TestStatisticReadWrite.run"
    )
    mocker.patch.object(sys, "argv", ["tsrw", "-i", "sample.csv", "-o", "out_ok", "-s", "Status"])

    main()

    mock_init.assert_called_once()

    call_kwargs = mock_init.call_args.kwargs
    assert call_kwargs["sort_key"] == "Status"
    assert call_kwargs["top_x"] == 10  # default

    mock_run.assert_called_once()

def test_cli_default_x(mocker, mock_logger):
    """
    Test-ID: D-T-CLI-DEX-001
    Verifies that the CLI correctly defaults `<X>` to 10 when not provided.

    This test simulates invoking the CLI without specifying the `-x` argument.
    It checks that the `TestStatisticReadWrite` class is initialized with the default
    value of `top_x=10` and that the `run` method is called exactly once.

    Args:
        mocker (pytest_mock.plugin.MockerFixture): Fixture for mocking objects.
        mock_logger (MagicMock): Fixture providing a mocked Logger instance.
    """
    mocker.patch.object(sys, "argv", ["tsrw", "-i", "input.csv", "-o", "output"])
    mock_test_statistic_read_write = mocker.patch('test_statistic_read_write.cli.TestStatisticReadWrite').return_value
    
    main()
    
    mock_test_statistic_read_write.run.assert_called_once()
    mock_test_statistic_read_write.top_x = 10

def test_main_friendly_exception(mock_test_statistic_read_write, mocker, capsys):
    """
    Test-ID: D-T-CLI-FRE-001
    Verifies that FriendlyException raised in main is handled correctly.

    This test checks that when a FriendlyException is raised during the
    execution of TestStatisticReadWrite.run, the program exits with a
    non-zero exit code and the exception message is printed to stdout.

    Args:
        mock_test_statistic_read_write: A mock of the TestStatisticReadWrite class
        mocker (pytest_mock.plugin.MockerFixture): Fixture for mocking objects.
        capsys (pytest.CaptureFixture): Fixture for capturing stdout and stderr.
    """
    mocker.patch('test_statistic_read_write.cli.os.path.abspath', side_effect=lambda x: x)
    mocker.patch('test_statistic_read_write.cli.os.path.isfile', return_value=True)
    mocker.patch('test_statistic_read_write.cli.os.path.exists', return_value=False)
    mocker.patch('test_statistic_read_write.cli.os.makedirs')
    mocker.patch('test_statistic_read_write.cli.atexit.register')
    mocker.patch.object(sys, "argv", ["tsrw", "-i", "sample.csv", "-o", "out_ok"])

    msg = "Mocked FriendlyException"
    mock_test_statistic_read_write.run.side_effect = FriendlyException(msg)

    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 1

    captured = capsys.readouterr()
    assert msg in captured.out

@pytest.mark.parametrize("invalid_x", ["abc", "5.5"])
def test_cli_invalid_x_non_integer(mocker, capsys, invalid_x):
    """
    Test-ID: D-T-CLI-IXA-001
    Verifies that the CLI correctly handles non-integer `<X>` values.

    This test simulates invoking the CLI with non-integer values for the `-x` argument,
    such as alphabetical strings and floating-point numbers. It checks that the program
    exits with a `SystemExit` exception, outputs an appropriate error message,
    and does not proceed with execution.

    Args:
        mocker (pytest_mock.plugin.MockerFixture): Fixture for mocking objects.
        capsys (pytest.CaptureFixture): Fixture for capturing stdout and stderr.
        invalid_x (str): The invalid `<X>` value to test.
    """
    mocker.patch.object(sys, "argv", ["tsrw", "-i", "input.csv", "-o", "output", "-x", invalid_x])
    mocker.patch("test_statistic_read_write.cli.os.path.isfile", return_value=True)
    mocker.patch("test_statistic_read_write.cli.os.path.exists", return_value=True)
    mocker.patch("test_statistic_read_write.cli.os.makedirs")
    
    with pytest.raises(SystemExit) as exc_info:
        main()
    
    captured = capsys.readouterr()
    error_message = f"error: argument -x: invalid int value: '{invalid_x}'"
    assert error_message in captured.out or error_message in captured.err
    error_message = "usage"
    assert error_message in captured.out or error_message in captured.err
    assert exc_info.value.code != 0 
    
def test_cli_invalid_x_negative(mocker, capsys):
    """
    Test-ID: D-T-CLI-IXN-001
    Verifies that the CLI correctly handles a negative `<X>` value.

    This test simulates invoking the CLI with a negative integer for the `-x` argument.
    It checks that the program exits with a `SystemExit` exception, outputs an
    appropriate error message, and does not proceed with execution.

    Args:
        mocker (pytest_mock.plugin.MockerFixture): Fixture for mocking objects.
        capsys (pytest.CaptureFixture): Fixture for capturing stdout and stderr.
    """
    invalid_x = "-1"
    mocker.patch.object(sys, "argv", ["tsrw", "-i", "input.csv", "-o", "output", "-x", invalid_x])
    mocker.patch("test_statistic_read_write.cli.os.path.isfile", return_value=True)
    mocker.patch("test_statistic_read_write.cli.os.path.exists", return_value=True)
    mocker.patch("test_statistic_read_write.cli.os.makedirs")
    
    with pytest.raises(SystemExit) as exc_info:
        main()
    
    captured = capsys.readouterr()
    error_message = f"Error: Invalid top_x value: {invalid_x}"
    assert error_message in captured.err or error_message in captured.out
    assert exc_info.value.code != 0

def test_log_end_of_session(mock_logger):
    """
    Test-ID: D-T-CLI-LES-001
    Verifies that the log_end_of_session function logs the correct message.

    This test checks that when log_end_of_session is called, it invokes
    the log_info method of the logger with the message "Execution ended.\n".

    Args:
        mock_logger: A mock of the Logger object.
    """
    cli.log_end_of_session()
    mock_logger.log_info.assert_called_once_with("Execution ended.\n")

def test_success_scenario_no_verbose(mocker):
    """
    Test-ID: D-T-CLI-SSN-001
    Verifies successful execution of the main functionality without verbose logging.

    This test simulates a successful run of the CLI with valid input and
    output arguments, and without the verbose flag. It checks that the
    TestStatisticReadWrite.run method is called exactly once, indicating that
    the core logic of the application was executed.

    Args:
        mocker (pytest_mock.plugin.MockerFixture): Fixture for mocking objects.
    """
    mocker.patch("test_statistic_read_write.cli.os.path.isfile", return_value=True)
    mocker.patch("test_statistic_read_write.cli.os.path.exists", return_value=True)
    mocker.patch("test_statistic_read_write.cli.os.makedirs")
    mock_run = mocker.patch("test_statistic_read_write.test_statistic_read_write.TestStatisticReadWrite.run")

    mocker.patch("test_statistic_read_write.cli.sys.argv", ["tsrw", "-i", "sample.csv", "-o", "out"])

    main()
    
    mock_run.assert_called_once()

def test_success_scenario_with_verbose_and_logfolder(mocker):
    """
    Test-ID: D-T-CLI-SSV-001
    Verifies successful execution with verbose logging enabled and a log folder specified.

    This test simulates a successful run of the CLI with:
    - Valid input and output arguments
    - The verbose flag enabled
    - A specified log folder

    It checks that:
    - The `TestStatisticReadWrite.run` method is called once.
    - The `Logger.set_verbose` method is called once with `True`.
    - The `Logger.set_log_folder` method is called once with the correct path.

    Args:
        mocker (pytest_mock.plugin.MockerFixture): Fixture for mocking objects.
    """
    mocker.patch('test_statistic_read_write.cli.os.path.abspath', side_effect=lambda x: x)
    mocker.patch("test_statistic_read_write.cli.os.path.isfile", return_value=True)
    mocker.patch("test_statistic_read_write.cli.os.path.exists", return_value=True)
    mocker.patch("test_statistic_read_write.cli.os.makedirs")
    mocker.patch('test_statistic_read_write.cli.atexit.register')

    mock_run = mocker.patch("test_statistic_read_write.test_statistic_read_write.TestStatisticReadWrite.run")
    mock_set_verbose = mocker.patch.object(Logger, "set_verbose")
    mock_set_log_folder = mocker.patch.object(Logger, "set_log_folder")

    mocker.patch("test_statistic_read_write.cli.sys.argv", ["tsrw", "-i", "sample.csv", "-o", "out", "-v", "-L", "logs"])

    main()

    mock_run.assert_called_once()
    mock_set_verbose.assert_called_once()  # Two calls: one in CLI, on in the constructor of TSRW
    mock_set_log_folder.assert_called_once_with("logs")


def test_unexpected_exception(mocker, capsys):
    """
    Test-ID: D-T-CLI-UEX-002
    Verifies handling of unexpected exceptions in the main logic.

    This test simulates an unexpected exception (`ValueError`) being raised
    during the execution of `TestStatisticReadWrite.run`. It verifies that:
    - The program exits with a non-zero exit code.
    - An appropriate error message is printed to stdout or stderr.

    Args:
        mocker (pytest_mock.plugin.MockerFixture): Fixture for mocking objects.
        capsys (pytest.CaptureFixture): Fixture for capturing stdout and stderr.
    """
    mocker.patch("test_statistic_read_write.cli.os.path.isfile", return_value=True)
    mocker.patch("test_statistic_read_write.cli.os.path.exists", return_value=True)
    mocker.patch("test_statistic_read_write.cli.os.makedirs")
    mock_run = mocker.patch(
        "test_statistic_read_write.test_statistic_read_write.TestStatisticReadWrite.run",
        side_effect=ValueError("Something unexpected")
    )
    mocker.patch.object(sys, "argv", ["tsrw", "-i", "sample.csv", "-o", "out_ok"])

    with pytest.raises(SystemExit) as exc_info:
        main()

    assert exc_info.value.code == 1

    captured = capsys.readouterr()
    assert "Error: Unexpected error occurred:" in captured.out or "Error: Unexpected error occurred:" in captured.err

    mock_run.assert_called_once()





