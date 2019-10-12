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
    readonly attendance_folder_path="/Users/$(logname)/.attendance"
else
    sudo apt install python3-pip git -y
    sudo -H pip3 install requests
    readonly attendance_folder_path="/opt/attendance"
fi

# clone the repo
cd
git clone https://github.com/amfoss/attendance-tracker.git

# create attendance folder
sudo mkdir -p "$attendance_folder_path"
# remove all old contents if any
sudo rm -rf "$attendance_folder_path"/*

sudo cp -r attendance-tracker/attendance/. "$attendance_folder_path"/.

sudo chmod +x "$attendance_folder_path"/config "$attendance_folder_path"/get_ssid_names.sh

# Add a new cron-job
username=$(logname)
croncmd="*/1 * * * * ${attendance_folder_path}/config $username"
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
cd "$attendance_folder_path"
sudo python3 get_and_save_credentials.py
cd ~
