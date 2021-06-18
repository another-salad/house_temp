"""Runs pylint and unit tests"""

from unittest import TestLoader, TextTestRunner

from pylint.lint import Run


def discover_and_run(start_dir: str = "tests/", pattern: str = "test*.py"):
    """Discovers and runs all unit tests from the specified DIR

    Args:
        start_dir (str, optional): The DIR to scan. Defaults to 'tests/'.
        pattern (str, optional): The naming convention for test files. Defaults to 'test*.py'.

    Returns:
        runner.run: The result of the test cases
    """
    tests = TestLoader().discover(start_dir, pattern=pattern)
    runner = TextTestRunner(verbosity=2)
    return runner.run(tests)


def print_stages(text: str):
    """Prints the stage names for clarity

    Args:
        text (str): The name of the stage
    """
    break_string = "#################################################################"
    for item in [break_string, text, break_string]:
        print(item)


if __name__ == "__main__":
    print_stages("Running unit tests")
    discover_and_run()
    print_stages('Running pylint')
    Run(["app.py", "common/"])
