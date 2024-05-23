#!/bin/bash

# Update pip to the latest version
python -m pip install --upgrade pip

# Install necessary libraries
pip install neopixel
pip install adafruit-circuitpython-neopixel
pip install selenium
pip install webdriver-manager
pip install fake_useragent

echo "All libraries installed successfully."