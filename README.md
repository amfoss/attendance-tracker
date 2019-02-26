# LabTrac
LabTrac by amFOSS is a advanced attendance recording system in-place for the members of FOSS@Amrita, while they are in FOSSLab. It runs a cron-job at regular intervals on client systems, and sends a set containing WiFi networks in range, which is matched with other clients, to confirm presence together and award attendance. 

## How it Works?
1. Installs a cron job script in your machine, at regular intervals.
2. During the installation, the member saves amFOSS CMS credentials on their machine, 
   which will be used for authenticating the user.
3. The list of WiFi Networks (BSSID) around you are recorded, along with the timestamp, 
   and your public IP Address.
4. All this data, along with the credentials are sent to amFOSS CMS server through API
   at regular intervals as AttendanceLogs.
5. At the end of the day, the server runs a cron job which will process the entire data,
   and determine whether you were in the lab, looking how much your wifi networks match
   with other members.

## Installation Instructions
1. Clone this repository
2. Run ```install.sh```
3. Enter your amFOSS CMS Credentials 
On doing this, a cron-job will be setup on your machine, which will be execting on regular intervals, and sending your attendance. 

#### Removing the Cron Job
```bash
$ sudo crontab -l > mycron || touch mycron
$ sudo rm mycron
```

## FAQ

##### What data is tracked?
1. Your Public IP Address
2. List of BSSID of WiFi Networks around you.

### Do I need to be connected to the Internet?
Yes.

##### Is the data logged forever?
No. All the attendance logs are processed by the server every night, and attendance
are marked for each member, after which, all the logs are deleted.

##### What happens if I sit in the corner of the lab?
If a person sits in the far corner of the lab, his/her device may have low matching 
of WiFi networks with the others in the lab. As a result, he/she may lose her attendance.
However, this may be rare case since the lab is pretty much covered by most WiFi Signals.

##### What if there are very few people in the lab?
When the server processes the logs, the algorithm shall find out that most members 
have very low matching with each other. However, for the few people in the lab, 
they would have very high matching, and this would mark them present.

##### What if many people club bunk lab and stay in their hostel?
When they are in the hostel, since they are in multiple rooms or locations,
they are likely going to have unmatching set of WiFi networks around them.

##### How far is it credible?
Since most processing and verification is done in the servers, there is no scope
for local manipulation of scripts. Also, since the system works on a decentralized
model where it depends on mutual verification by members, it cannot be easily be 
manipulated by one single person.

##### Will the server be logging attendance 24 hours?
The server will log attendance only during lab working hours defined 
(such as 4-11 during working days) and exclude requests send all other times.
This is to avoid huge log of data, and unnecessary processing. 


## Developers
* Original Developer - Chirath R.
* Python - [Ashwin S Shenoy](https://github.com/aswinshenoy)
* Bash Scripting - [Akhil K Gangadharan](https://github.com/akhilam512)
