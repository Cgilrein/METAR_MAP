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

# Function to download geckodriver
download_geckodriver() {
    GECKODRIVER_VERSION="v0.30.0"
    GECKODRIVER_TAR="geckodriver-$GECKODRIVER_VERSION-linux-arm7.tar.gz"
    GECKODRIVER_URL="https://github.com/mozilla/geckodriver/releases/download/$GECKODRIVER_VERSION/$GECKODRIVER_TAR"

    echo "Checking URL: $GECKODRIVER_URL"
    if curl --output /dev/null --silent --head --fail "$GECKODRIVER_URL"; then
        echo "URL exists: $GECKODRIVER_URL"
        echo "Downloading geckodriver..."
        curl -L -o $GECKODRIVER_TAR $GECKODRIVER_URL
        if [ $? -ne 0 ]; then
            echo "Failed to download geckodriver"
            exit 1
        fi

        echo "Extracting geckodriver..."
        tar -xvzf $GECKODRIVER_TAR
        if [ $? -ne 0 ]; then
            echo "Failed to extract geckodriver"
            exit 1
        fi

        echo "Moving geckodriver to /usr/local/bin/..."
        sudo mv geckodriver /usr/local/bin/
        if [ $? -ne 0 ]; then
            echo "Failed to move geckodriver to /usr/local/bin/"
            exit 1
        fi

        echo "Making geckodriver executable..."
        sudo chmod +x /usr/local/bin/geckodriver
        if [ $? -ne 0 ]; then
            echo "Failed to make geckodriver executable"
            exit 1
        fi

        echo "geckodriver installed successfully."
    else
        echo "URL does not exist: $GECKODRIVER_URL"
        exit 1
    fi
}

# Download geckodriver
download_geckodriver

echo "All libraries and geckodriver installed successfully."
