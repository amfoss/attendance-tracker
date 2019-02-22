# amFOSS Attendance Tracker


## How it Works?
1. Installs a cron job script in your machine, at regular intervals.
2. During the installation, the member saves amFOSS CMS credentials on their machine, 
   which will be used for authenticating the user.
3. The list of WiFi Networks (Physical Address) around you are recorded, along with the timestamp, 
   and your public IP Address.
4. All this data, along with the credentials are sent to amFOSS CMS server through API
   at regular intervals as AttendanceLogs.
5. At the end of the day, the server runs a cron job which will process the entire data,
   and determine whether you were in the lab, looking how much your wifi networks match
   with other members.

## FAQ

##### What data is tracked?
1. Your Public IP Address
2. List of Physical Addresses of WiFi Networks around you.

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
* Ashwin S Shenoy 