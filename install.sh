#!/usr/bin/env bash

unameOut="$(uname -s)"
_uname="$(logname)"
case "${unameOut}" in
    Linux*)     machine=Linux;;
    Darwin*)    machine=Mac;;
    CYGWIN*)    machine=Cygwin;;
    MINGW*)     machine=MinGw;;
    *)          machine="UNKNOWN:${unameOut}"
esac

# configuration
if [[ "$machine" = "Mac" ]]; then
    readonly attendance_folder_path="/Users/$_uname/.attendance"
else
    readonly attendance_folder_path="/opt/attendance"
    readonly labtrac_service_path="/etc/systemd/system"
fi

# clone the repo
rm -rf attendance-tracker
git clone https://github.com/amfoss/attendance-tracker.git

# create attendance folder
sudo mkdir -p "$attendance_folder_path"
# remove all old contents if any
sudo rm -rf "$attendance_folder_path"/*
if [[ "$machine" != "Mac" ]]; then
    sudo rm -f "$labtrac_service_path"/labtrac.service
    sudo rm -f "$labtrac_service_path"/labtrac.timer
fi

sudo cp -r attendance-tracker/attendance/. "$attendance_folder_path"/.

sudo chmod +x "$attendance_folder_path"/config "$attendance_folder_path"/get_ssid_names.sh

# Activate the service
if [[ "$machine" != "Mac" ]]; then
    sudo cp -r attendance-tracker/system/. "$labtrac_service_path"/.
    sudo systemctl enable labtrac.timer
    sudo systemctl start labtrac.service
fi

if [[ "$machine" = "Mac" ]]; then
    sudo chmod u+x macinstall.sh
    sudo ./macinstall.sh $_uname
fi
# delete downloaded files
rm -rf attendance-tracker
rm install.sh

# fetch creds from user and store them
cd "$attendance_folder_path"
sudo python3 get_and_save_credentials.py
cd ~
