"""Test configuration.
These allow the mocking of various Python modules
that might otherwise have runtime side-effects.
"""
import sys
from unittest import mock

import pytest


@pytest.fixture(scope="function", autouse=False)
def st7735():
    import st7735
    yield st7735
    del sys.modules["st7735"]


@pytest.fixture(scope="function", autouse=False)
def gpiod():
    """Mock gpiod module."""
    sys.modules["gpiod"] = mock.MagicMock()
    sys.modules["gpiod.line"] = mock.MagicMock()
    yield sys.modules["gpiod"]
    del sys.modules["gpiod"]


@pytest.fixture(scope="function", autouse=False)
def gpiodevice():
    """Mock gpiodevice module."""
    sys.modules["gpiodevice"] = mock.MagicMock()
    sys.modules["gpiodevice"].get_pin.return_value = (mock.Mock(), 0)
    yield sys.modules["gpiodevice"]
    del sys.modules["gpiodevice"]


@pytest.fixture(scope="function", autouse=False)
def spidev():
    """Mock spidev module."""
    spidev = mock.MagicMock()
    sys.modules["spidev"] = spidev
    yield spidev
    del sys.modules["spidev"]


@pytest.fixture(scope="function", autouse=False)
def numpy():
    """Mock numpy module."""
    numpy = mock.MagicMock()
    sys.modules["numpy"] = numpy
    yield numpy
    del sys.modules["numpy"]
