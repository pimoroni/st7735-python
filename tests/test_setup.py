from unittest import mock


def test_setup(gpiodevice, gpiod, spidev, numpy, st7735):
    _ = st7735.ST7735(port=0, cs=0, dc="GPIO24")

    gpiodevice.get_pin.assert_has_calls([
        mock.call("GPIO24", "st7735-dc", st7735.OUTL)
    ], any_order=True)


def test_setup_no_invert(gpiodevice, gpiod, spidev, numpy, st7735):
    _ = st7735.ST7735(port=0, cs=0, dc="GPIO24", invert=False)


def test_setup_with_backlight(gpiodevice, gpiod, spidev, numpy, st7735):
    display = st7735.ST7735(port=0, cs=0, dc="GPIO24", backlight="GPIO4")

    display.set_backlight(True)

    gpiodevice.get_pin.assert_has_calls([mock.call("GPIO4", "st7735-bl", st7735.OUTL)], any_order=True)


def test_setup_with_reset(gpiodevice, gpiod, spidev, numpy, st7735):
    _ = st7735.ST7735(port=0, cs=0, dc=24, rst="GPIO4")

    gpiodevice.get_pin.assert_has_calls([mock.call("GPIO4", "st7735-rst", st7735.OUTL)], any_order=True)
