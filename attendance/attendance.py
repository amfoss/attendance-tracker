# created by Chirath R <chirath.02@gmail.com>
import json
import wifi


def search():
    wifi_list = []

    cells = wifi.Cell.all('wlo1')

    for cell in cells:
        wifi_list.append(str(cell.ssid))

    return wifi_list


def fetch_latest_ssid_match():
    data = json.load(open('data/ssid.json'))

    return data["ssid"]


ssid_list = search()
print ssid_list

for i in ssid_list:
    if fetch_latest_ssid_match() in i:
        print i


