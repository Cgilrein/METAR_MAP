#!/bin/bash

# Update the package list and install dependencies
sudo apt-get update
sudo apt-get install -y wget tar python3-pip python3-venv firefox-esr

# Create and activate a virtual environment
python3 -m venv selenium-env
source selenium-env/bin/activate

# Install necessary Python libraries within the virtual environment
pip install rpi_ws281x adafruit-circuitpython-neopixel selenium webdriver-manager fake_useragent numpy --break-system-packages

# Function to download geckodriver
download_geckodriver() {
    GECKODRIVER_VERSION="v0.33.0"
    GECKODRIVER_TAR="geckodriver-$GECKODRIVER_VERSION-linux32.tar.gz"
    GECKODRIVER_URL="https://github.com/mozilla/geckodriver/releases/download/$GECKODRIVER_VERSION/$GECKODRIVER_TAR"

    echo "Downloading geckodriver from $GECKODRIVER_URL"
    wget -O $GECKODRIVER_TAR $GECKODRIVER_URL
    if [ $? -ne 0 ]; then
        echo "Failed to download geckodriver"
        exit 1
    fi

    echo "Extracting geckodriver"
    tar -xvzf $GECKODRIVER_TAR
    if [ $? -ne 0 ]; then
        echo "Failed to extract geckodriver"
        exit 1
    fi

    echo "Moving geckodriver to /usr/local/bin/"
    sudo mv geckodriver /usr/local/bin/
    if [ $? -ne 0 ]; then
        echo "Failed to move geckodriver to /usr/local/bin/"
        exit 1
    fi

    echo "Making geckodriver executable"
    sudo chmod +x /usr/local/bin/geckodriver
    if [ $? -ne 0 ]; then
        echo "Failed to make geckodriver executable"
        exit 1
    fi

    echo "geckodriver installed successfully."
}

# Download geckodriver
download_geckodriver

echo "All libraries and geckodriver installed successfully."
