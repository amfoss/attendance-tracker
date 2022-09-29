#!/usr/bin/env bash

# Install pip, git and requests
sudo apt install python3-pip git -y
sudo -H pip3 install requests

# Remove downloaded files
rm debian.sh
