#!/bin/bash

# install pip, git and requests
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install python3
brew install python3
pip3 install requests

# clone the repo
git clone https://github.com/amfoss/join-foss.git -b osx
cd join-foss/macos/

# Store configuration files
mkdir ~/amfossbot
cp -r ./ ~/amfossbot
chmod +x ~/amfossbot/attendance/config ~/amfossbot/attendance/attendance.py ~/amfossbot/attendance/get_ssid_names.sh

# Add a new cron-job
# write out current crontab
sudo crontab -l > mycron || touch mycron
# echo new cron into cron file, run every 15 mins
echo "*/15 * * * * <YOUR ABSOULTE PATH HERE>/amfossbot/attendance/config" >> mycron
# install new cron file
sudo crontab mycron
rm mycron

cd ..
rm -rf join-foss

cd /opt/attendance/
sudo python3 get_and_save_auth_token.py
cd ~
