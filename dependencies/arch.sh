#!/usr/bin/env bash

# Install pip, git and requests
sudo pacman -S python-pip git --noconfirm
sudo -H pip install requests

# Remove downloaded files
rm arch.sh
