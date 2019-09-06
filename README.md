# Lab Trac

LabTrac by amFOSS is a advanced attendance recording system in-place for the members of FOSS@Amrita.

## How it Works?

1. Runs a cron job script in your machine, at regular intervals.
2. During the installation, the member saves amFOSS CMS credentials on their machine, which will be used for authenticating the user.
3. NodeMCU creates a random WiFi Network for every 5 mins which looks like amFOSS_XXXXXXXXXXX.
4. Your Machine searches for amFOSS WiFi network in list of WiFi Networks (BSSID) around you.
5. All this data, along with the credentials are sent to amFOSS CMS server through API at regular intervals as AttendanceLogs.

## Installation Instructions

1. Run the command in your terminal and enter your amFOSS CMS Credentials
```bash
wget https://raw.githubusercontent.com/amfoss/attendance-tracker/master/install.sh ; bash -e install.sh
```

## Update Your Credentials

This should be done whenever you change your password.

```bash
sudo python3 /opt/attendance/get_and_save_credentials.py
```

## FAQ

##### What data is tracked ?

1. List of amFOSS WiFi networks around you.

##### Do I need to connect to Internet ?
Yes

##### How far is it credible?
Since most processing and verification is done in the Server and NodeMCU, there is no scope
for local manipulation of scripts.