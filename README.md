# Lab Trac

LabTrac is an advanced Attendance Recording System designed by and for the members of amFOSS. Tracks list of amFOSS WiFi networks near you.

## How it Works?

1. Runs a cron job script on the member's machine, at regular intervals.
2. During the installation, the member will have to save the amFOSS CMS credentials on their machine, which will be then, used for authenticating the user.
3. NodeMCU creates a random WiFi Network for every 5 mins (akin to something like, 'amFOSS_XXXXXXXXXXX').
4. The member's machine will search for the amFOSS WiFi network in list of WiFi Networks (BSSID) around it.
5. All this data, along with the credentials will be sent to amFOSS CMS server through API at regular intervals as AttendanceLogs.

## Dependencies Guide

Read the [guide](dependencies/README_dependencies.md) for distro-specific instructions to install dependencies.

## Installation Instructions

Run the following command in your terminal and then, enter your amFOSS CMS Credentials

```bash
cd ~ && sudo wget https://raw.githubusercontent.com/amfoss/attendance-tracker/master/install.sh -O install.sh && sudo bash -e install.sh
```

## Update Your Credentials
This should be done whenever you change your password.

### For Linux

```bash
sudo python3 /opt/attendance/get_and_save_credentials.py
```

### For Mac

```bash
sudo python3 ~/.attendance/get_and_save_credentials.py
```
