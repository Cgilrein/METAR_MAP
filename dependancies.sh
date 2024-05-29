#!/bin/bash

# Update pip to the latest version
python -m pip install --upgrade pip

# Install necessary libraries
pip3 install neopixel
pip3 install adafruit-circuitpython-neopixel
pip3 install selenium
pip3 install webdriver-manager
pip3 install fake_useragent
pip3 install numpy

echo "All libraries installed successfully."