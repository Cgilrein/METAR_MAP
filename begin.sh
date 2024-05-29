#!/bin/bash

# Get the current directory and script path
currentDirectory=$(pwd)
pathToScript="$currentDirectory/METAR_MA.py"

# Create the command to run the script
commandLine="sudo python3 $pathToScript &"

# Make sure your script is executable
sudo chmod +x $pathToScript

# Make rc.local executable
sudo chmod +x /etc/rc.local

# Append the command before the line containing 'exit 0' in /etc/rc.local
sudo sed -i -e "\|exit 0|i $commandLine" /etc/rc.local
