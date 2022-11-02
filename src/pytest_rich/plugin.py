"""
Proof of concept for pytest + rich integration.
"""
import sys

import pytest

from pytest_rich.terminal import RichTerminalReporter


def pytest_addoption(parser):
    """
    Called at the beginning of the test session to add command line options.

    Hook type: Initialization

    [Pytest docs](https://docs.pytest.org/en/latest/reference/reference.html#pytest.hookspec.pytest_addoption)
    """
    parser.addoption("--rich", action="store_true", default=False)


@pytest.hookimpl(trylast=True)
def pytest_configure(config):
    """
    Called for every plugin and initial conftest file after command line options have been parsed.

    Hook type: Initialization

    [Pytest docs](https://docs.pytest.org/en/latest/reference/reference.html#pytest.hookspec.pytest_configure)
    """
    if sys.stdout.isatty() and config.getoption("rich"):
        standard_reporter = config.pluginmanager.getplugin("terminalreporter")
        config.pluginmanager.unregister(standard_reporter)
        config.pluginmanager.register(
            RichTerminalReporter(config), "rich-terminal-reporter"
        )
