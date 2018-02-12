# created by Chirath R <chirath.02@gmail.com>
import json
import time
import sys
import wifi
from subprocess import Popen, PIPE
import urllib
from uuid import getnode as get_mac


def check_internet_connection():
    try:
        status_code = urllib.urlopen('http://foss.amrita.ac.in').getcode()
        if status_code == 200:
            return True
    except:
        return False
    return False


def get_interface_name():
    p = Popen(['./get_interface_name.sh'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    return output


def get_mac_address():
    mac = get_mac()
    return ':'.join(("%012X" % mac)[i:i + 2] for i in range(0, 12, 2))


def get_wifi_list(interface_name):
    wifi_list = []
    try:
        cells = wifi.Cell.all(interface_name)
    except wifi.exceptions.InterfaceError:
        # no wifi found, so restart
        return None

    for cell in cells:
        wifi_list.append(str(cell.ssid))

    return wifi_list


def fetch_latest_ssid():
    data = json.load(open('data/ssid.json'))
    return data["ssid"]


def check_wifi_ssid_found(ssid_list, ssid):
    if ssid in ssid_list:
        return True
    return False


def send_data(data):

    print (data)

    return True


if __name__ == '__main__':
    sleep_time = 15 * 20
    sleep = False

    while True:

        # sleep for sleep_time in case of an error or exception
        if sleep:
            time.sleep(sleep_time)
            sleep = False

        # check internet connection
        if not check_internet_connection():
            sleep = True
            continue

        # get wifi interface name
        wifi_interface_name = get_interface_name()

        # check if connected wifi
        if wifi_interface_name[0] != 'w':
            sleep = True
            continue

        # get list of wifi ssid's
        wifi_ssid_list = get_wifi_list(wifi_interface_name)

        if wifi_ssid_list is None:
            sleep = True
            continue

        # get new ssid from server
        fetched_ssid = fetch_latest_ssid()

        if fetched_ssid is None:
            sleep = True
            continue

        ssid_found = check_wifi_ssid_found(wifi_ssid_list, fetched_ssid)
        data_send = send_data(get_mac_address())

        if not ssid_found and not data_send:
            sleep = True
            continue

        # sleep for and query after sometime
        sleep = True
