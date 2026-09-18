from unittest import mock


def test_display(gpiodevice, gpiod, spidev, numpy, st7735):
    display = st7735.ST7735(port=0, cs=0, dc=24)
    numpy.dstack().flatten().tolist.return_value = [0xff, 0x00, 0xff, 0x00]
    display.display(mock.MagicMock())

    spidev.SpiDev().xfer3.assert_called_with([0xff, 0x00, 0xff, 0x00])


def test_color565(gpiodevice, gpiod, spidev, numpy, st7735):
    assert st7735.color565(255, 255, 255) == 0xFFFF


def test_image_to_data(gpiodevice, gpiod, spidev, numpy, st7735):
    numpy.dstack().flatten().tolist.return_value = []
    assert st7735.image_to_data(mock.MagicMock()) == []
