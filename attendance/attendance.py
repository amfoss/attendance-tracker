# created by Chirath R <chirath.02@gmail.com>

import datetime
import sys
from urllib.request import urlopen
from subprocess import Popen, PIPE
file_path = "./"


def check_internet_connection():
    try:
        status_code = urlopen('http://foss.amrita.ac.in').getcode()
        if status_code == 200:
            return True
    except:
        print("Internet error")
        return False
    return False


def get_interface_name():
    p = Popen([file_path + 'get_interface_name.sh'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    return str(output).replace("\\n", "")


def get_wifi_list(interface_name):
    ssid_list = []
    p = Popen([file_path + 'get_ssid_names.sh', interface_name], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    output = str(output).split("\\n")

    for name in output:
        name = bytes(name, encoding='ascii').decode('unicode-escape')
        name = str(name).strip(" ")
        name = name.strip()[6:].strip("\"").strip().strip("ESSID:").strip("\"")
        if name:
            ssid_list.append(name.lower())
    return ssid_list


def fetch_latest_ssid():
    ssid = "k4"
    return ssid.strip().lower()


def check_wifi_ssid_found(ssid_list, ssid):
    if ssid in ssid_list:
        return True
    return False


def send_data(data):

    return True


if __name__ == '__main__':

    # check internet connection
    if not check_internet_connection():
        sys.exit()

    # get wifi interface name
    wifi_interface_name = str(get_interface_name())

    # get list of wifi ssid's
    wifi_ssid_list = get_wifi_list(wifi_interface_name)

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
    data_send = send_data(fetched_ssid)

    if not data_send:
        sys.exit()

    # successful
    print(fetched_ssid + " " + str(datetime.datetime.now()))
