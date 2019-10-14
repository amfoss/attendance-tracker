#!/usr/bin/env bash

unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)     machine=Linux;;
    Darwin*)    machine=Mac;;
    CYGWIN*)    machine=Cygwin;;
    MINGW*)     machine=MinGw;;
    *)          machine="UNKNOWN:${unameOut}"
esac

# install pip, git and requests
if [[ "$machine" = "Mac" ]]; then
    if [[ $(command -v brew) == "" ]]; then
        /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    fi
    brew install python3
    pip3 install requests
    readonly ATTENDANCE_FOLDER_PATH="/Users/$(logname)/.attendance"
else

    if [ -f /etc/os-release ]; then
      # freedesktop.org and systemd
      . /etc/os-release
      OS=$NAME
      VER=$VERSION_ID
    elif type lsb_release >/dev/null 2>&1; then
        # linuxbase.org
        OS=$(lsb_release -si)
        VER=$(lsb_release -sr)
    elif [ -f /etc/lsb-release ]; then
        # For some versions of Debian/Ubuntu without lsb_release command
        . /etc/lsb-release
        OS=$DISTRIB_ID
        VER=$DISTRIB_RELEASE
    elif [ -f /etc/debian_version ]; then
        # Older Debian/Ubuntu/etc.
        OS=Debian
        VER=$(cat /etc/debian_version)
    fi

    case $OS in
    "Ubuntu")
        sudo apt install -y python3-pip git
        ;;
    "Arch Linux")
        sudo pacman -S -y python-pip git
        ;;
    *)
        echo "You have unsupported OS"
        exit 1
        ;;
    esac

    sudo -H pip3 install requests
    readonly ATTENDANCE_FOLDER_PATH="/opt/attendance"
fi

# clone the repo
cd
git clone https://github.com/amfoss/attendance-tracker.git

# create attendance folder
sudo mkdir -p "$ATTENDANCE_FOLDER_PATH"
# remove all old contents if any
sudo rm -rf "$ATTENDANCE_FOLDER_PATH"/*

sudo cp -r attendance-tracker/attendance/. "$ATTENDANCE_FOLDER_PATH"/.

sudo chmod +x "$ATTENDANCE_FOLDER_PATH"/config "$ATTENDANCE_FOLDER_PATH"/get_ssid_names.sh

# Add a new cron-job
username=$(logname)
croncmd="*/1 * * * * ${ATTENDANCE_FOLDER_PATH}/config $username"
# write out current crontab
sudo crontab -l > mycron || touch mycron
# echo new cron into cron file if it does not exist,
# to run every 1 min
if ! grep -Fxq "$croncmd" mycron; then
    echo "$croncmd" >> mycron
    # install new cron file
    sudo crontab mycron
fi

# delete downloaded files
rm mycron
rm -rf attendance-tracker
rm install.sh

# fetch creds from user and store them
cd "$ATTENDANCE_FOLDER_PATH"
sudo python3 get_and_save_credentials.py
cd ~
