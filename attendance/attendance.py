#!/usr/bin/python3
# created by Chirath R <chirath.02@gmail.com>

import datetime
import sys
import json

import requests
from urllib.request import urlopen
from subprocess import Popen, PIPE


file_path = "/opt/attendance/"
base_url = "https://amfoss.in/api/"


def check_internet_connection():
    try:
        status_code = urlopen('http://foss.amrita.ac.in').getcode()
        if status_code == 200:
            return True
    except:
        print("Internet error")
        return False
    return False


def get_wifi_list():
    ssid_list = []
    p = Popen([file_path + 'get_ssid_names.sh'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    output = str(output).split("\\n")

    for name in output:
        name = bytes(name, encoding='ascii').decode('unicode-escape')
        name = str(name).strip(" ")
        name = name.strip()[6:].strip("\"").strip().strip("ESSID:").strip("\"")
        if name:
            ssid_list.append(name.lower())
    return ssid_list


def get_auth_token():
    token = ''
    try:
        with open('/opt/attendance/.token', 'r') as file:
            token = file.readline()
    except EnvironmentError:
        print("Token error, run 'python3 get_and_save_auth_token.py'")
    return token


def fetch_latest_ssid():
    # curl -H "Authorization: JWT <your_token>" https://amfoss.in/api/ssid-name/

    url = base_url + "ssid-name/"

    headers = {"Authorization": "JWT " + get_auth_token()}
    response = requests.get(url=url, headers=headers)
    data = json.loads(response.text)

    if 'name' not in data.keys():
        print("Authentication token error")
        print(data)
        sys.exit()

    ssid = data['name']
    return ssid.strip().lower()


def check_wifi_ssid_found(ssid_list, ssid):
    if ssid in ssid_list:
        return True
    return False


def mark_attendance(ssid_name):
    url = base_url + "attendance/mark/"
    data = {'name': ssid_name}
    headers = {"Authorization": "JWT " + get_auth_token()}

    response = requests.post(url=url, data=data, headers=headers)
    data = json.loads(response.text)
    if 'status' in data.keys() and data['status'] == 'success':
        print(ssid_name + " " + str(datetime.datetime.now()))
        print(data)
        return True
    print("Error marking attendance: ", data)
    return False


if __name__ == '__main__':

    # check internet connection
    if not check_internet_connection():
        sys.exit()

    # get list of wifi ssid's
    wifi_ssid_list = get_wifi_list()

    if not wifi_ssid_list:
        sys.exit()

    # get new ssid from server
    fetched_ssid = fetch_latest_ssid()
    
    if not fetched_ssid:
        sys.exit()

    ssid_found = check_wifi_ssid_found(wifi_ssid_list, fetched_ssid)

    if not ssid_found:
        sys.exit()

    # Mark attendance
    mark_attendance(fetched_ssid)