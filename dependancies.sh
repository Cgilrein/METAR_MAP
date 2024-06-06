#!/bin/bash

# Update the package list
sudo apt-get update

# Install necessary packages
sudo apt-get install -y python3-pip python3-venv firefox-esr wget tar

# Update pip to the latest version
python3 -m pip install --upgrade pip --break-system-packages

# Create and activate a virtual environment
python3 -m venv selenium-env
source selenium-env/bin/activate

# Install necessary Python libraries within the virtual environment
pip install rpi_ws281x adafruit-circuitpython-neopixel --break-system-packages
pip install neopixel --break-system-packages
pip install adafruit-circuitpython-neopixel --break-system-packages
pip install selenium --break-system-packages
pip install webdriver-manager --break-system-packages
pip install fake_useragent --break-system-packages
pip install numpy --break-system-packages

# Download and install geckodriver
GECKODRIVER_VERSION="v0.30.0"
wget "https://github.com/mozilla/geckodriver/releases/download/$GECKODRIVER_VERSION/geckodriver-$GECKODRIVER_VERSION-linux-arm7.tar.gz"
tar -xvzf "geckodriver-$GECKODRIVER_VERSION-linux-arm7.tar.gz"
sudo mv geckodriver /usr/local/bin/
sudo chmod +x /usr/local/bin/geckodriver

echo "All libraries and geckodriver installed successfully."
