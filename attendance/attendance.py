#!/usr/bin/python3

import sys
import json

import requests
from urllib.request import urlopen
from subprocess import Popen, PIPE
from os.path import expanduser
from sys import platform as _platform


if _platform == "linux" or _platform == "linux2":
    file_path = "/opt/attendance/"
elif _platform == "darwin":
    home = expanduser("~")
    file_path = home+"/.amFOSS/"


def get_credentials():
    credentials = ''
    try:
        with open(file_path + '.credentials', 'r') as file:
            credentials = file.readline()
    except EnvironmentError:
        print("Credentials error, run 'python3 get_and_save_credentials.py'")
    return credentials


def check_internet_connection():
    try:
        status_code = urlopen('https://www.google.com/').getcode()
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
            ssid_list.append(name)
    return ssid_list


def fetch_relevant_ssid(wifi_ssid_list):
    relevant_ssid_list = []
    for ssid in wifi_ssid_list:
        if ssid.startswith('amFOSS'):
            relevant_ssid_list.append(ssid)
    return relevant_ssid_list


def mark_attendance(wifi_ssid_list, credentials):
    data = {'username': credentials['username'], 'password': credentials['password'], 'list': wifi_ssid_list}
    variables = json.dumps(data)
    url = 'https://api.amfoss.in/?'
    mutation = '''
    mutation logAttendance($username: String!, $password: String!, $list: [String]) {
        LogAttendance(username: $username, password: $password, list: $list)
        {
            id
        }
    }
    '''
    r = requests.post(url, json={'query': mutation, 'variables': variables})
    print(r.content)
    return False


if __name__ == '__main__':

    # check internet connection
    if not check_internet_connection():
        sys.exit()

    # get list of wifi ssid's
    wifi_ssid_list = get_wifi_list()

    # get relevent wifi ssid's
    wifi_ssid_list = fetch_relevant_ssid(wifi_ssid_list)
    if not wifi_ssid_list:
        sys.exit()

    credentials = json.loads(get_credentials())
    # Mark attendance
    mark_attendance(wifi_ssid_list, credentials)
