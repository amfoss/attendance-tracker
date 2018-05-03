#!/bin/bash

# install pip and wifi
sudo apt install python3-pip
sudo -H pip3 install wifi

# Store configuration files
mkdir ~/.attendance
cp ./attendance/* -r ~/.attendance/
chmod +x ~/.attendance/config ~/.attendance/attendance.py ~/.attendance/get_interface_name.sh

# Add a new cron-job
# write out current crontab
crontab -l > mycron
# echo new cron into cron file, run every 15 mins
echo "*/15 * * * * ~/.attendance/config" >> mycron
# install new cron file
crontab mycron
rm mycron
