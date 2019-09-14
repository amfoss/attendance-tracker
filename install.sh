#!/usr/bin/env bash

unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)     machine=Linux;;
    Darwin*)    machine=Mac;;
    CYGWIN*)    machine=Cygwin;;
    MINGW*)     machine=MinGw;;
    *)          machine="UNKNOWN:${unameOut}"
esac
#echo ${machine}
if [[ "$machine" = "Mac" ]];then
    # # install pip, git and requests
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    brew install python3
    pip3 install requests

    # clone the repo
    cd
    git clone https://github.com/amfoss/attendance-tracker.git
    cd attendance-tracker/macos/attendance

    # Store configuration files
    mkdir ~/.amFOSS
    cp -r ./ ~/.amFOSS
    chmod +x ~/.amFOSS/config ~/.amFOSS/attendance.py ~/.amFOSS/get_ssid_names.sh

    # Add a new cron-job
    # write out current crontab
    sudo crontab -l > mycron || touch mycron
    # echo new cron into cron file, run every 1 min
    echo "*/1 * * * * /.amFOSS/config" >> mycron
    # install new cron file
    sudo crontab mycron
    rm mycron

    cd
    rm -rf attendance-tracker
    rm -rf install.sh

    cd ~/.amFOSS/
    sudo python3 get_and_save_credentials.py
    cd ~

else
    # install pip, git and requests
    sudo apt install python3-pip git -y
    sudo -H pip3 install requests

    # clone the repo
    git clone https://github.com/amfoss/attendance-tracker.git
    cd attendance-tracker/

    # Store configuration files
    sudo rm /opt/attendance/ -rf
    sudo mkdir /opt/attendance
    sudo cp ./attendance/* -r /opt/attendance/
    sudo chmod +x /opt/attendance/config /opt/attendance/attendance.py /opt/attendance/get_ssid_names.sh

    # Add a new cron-job
    # write out current crontab
    sudo crontab -l > mycron || touch mycron
    # echo new cron into cron file, run every 1 mins
    echo "*/1 * * * * /opt/attendance/config" >> mycron
    # install new cron file
    sudo crontab mycron
    rm mycron

    cd ..
    rm -rf attendance-tracker
    rm install.sh

    cd /opt/attendance/
    sudo python3 get_and_save_credentials.py
    cd ~
fi