#!/bin/bash

# install pip, git and requests
sudo apt update
sudo apt install python3-pip git -y
sudo -H pip3 install requests

# clone the repo
git clone https://github.com/amfoss/join-foss.git
cd join-foss/

# Store configuration files
sudo rm /opt/attendance/ -rf
sudo mkdir /opt/attendance
sudo cp ./attendance/* -r /opt/attendance/
sudo chmod +x /opt/attendance/config /opt/attendance/attendance.py /opt/attendance/get_ssid_names.sh

# Add a new cron-job
# write out current crontab
sudo crontab -l > mycron || touch mycron
# echo new cron into cron file, run every 15 mins
echo "*/15 * * * * /opt/attendance/config" >> mycron
# install new cron file
sudo crontab mycron
rm mycron

cd ..
rm -rf join-foss

cd /opt/attendance/
sudo python3 get_and_save_auth_token.py
cd ~
