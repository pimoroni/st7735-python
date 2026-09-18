2.0.0
-----

* Enhancement: Repackage to the uv/hatchling method, with PyPI trusted publishing
* Enhancement: Version is derived from the git tag, __version__ from package metadata
* Python 3.9 or later, 3.7 and 3.8 support dropped

1.0.0
-----

* Rename module from ST7735 to st7735
* Port to gpiod/gpiodevice

0.0.5
-----

* Add support for choosing between BGR/RGB displays
* Add methods for display power and sleep control

0.0.4-post1
-----------

* Repackage with Markdown README/setup.cfg
* Fix `__version__` to 0.0.4
* Update dependencies in README

0.0.4
-----

* Depend upon spidev==3.4.0 for stability fixes
* Switch from manual data chunking to spidev.xfer3()


0.0.3
-----

* Fixed backlight pin
* Added `set_backlight`
* Added constants BG_SPI_CS_FRONT and BG_SPI_CS_BACK
* Added module `__version__`

0.0.2
-----

* Support for multiple display sizes/orientations

0.0.1
-----

* Initial Release
