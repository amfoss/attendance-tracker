# Join FOSS


## Installation

```bash
wget https://raw.githubusercontent.com/amfoss/join-foss/master/install.sh ; bash -e install.sh
sudo /opt/attendance/config
```

Check your attendance at:

```
https://amfoss.in/attendance/year/mon/day/
```

## Update your api key

This should be done after every 6 months

```bash
sudo python3 /opt/attendance/get_and_save_auth_token.py
```
