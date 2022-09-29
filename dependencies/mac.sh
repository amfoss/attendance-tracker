#!/usr/bin/env bash

# Install pip, git and requests
if [[ $(command -v brew) == "" ]]; then
        /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    fi
    brew install python3
    pip3 install requests

# Remove downloaded files
rm mac.sh
