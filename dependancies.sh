#!/bin/bash

# Update the package list
sudo apt-get update

# Install necessary packages
sudo apt-get install -y python3-pip python3-venv firefox-esr wget curl tar

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


# Update the package list and install dependencies
sudo apt-get update
sudo apt-get install -y wget unzip

# Get the latest version number of ChromeDriver
LATEST_VERSION=$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE)

# Download the latest version of ChromeDriver
wget -N https://chromedriver.storage.googleapis.com/${LATEST_VERSION}/chromedriver_linux64.zip

# Unzip the downloaded file
unzip chromedriver_linux64.zip

# Move ChromeDriver to a directory in your PATH
sudo mv chromedriver /usr/local/bin/

# Give ChromeDriver executable permissions
sudo chmod +x /usr/local/bin/chromedriver

# Verify the installation
chromedriver --version

echo "Script Completed"