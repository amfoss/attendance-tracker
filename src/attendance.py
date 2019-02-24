from urllib.request import urlopen
import sys
from subprocess import Popen, PIPE
from datetime import datetime
import json
import requests

file_path = "/opt/attendance/"

def check_internet_connection():
    try:
        status_code = urlopen('http://foss.amrita.ac.in').getcode()
        if status_code == 200:
            return True
    except:
        print("Internet error")
        return False

def get_public_ip():
    p = Popen([file_path + 'get_public_ip.sh'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    ip, err = p.communicate()
    ip = str(ip).split("\\n")[0]
    ip = ip.split("b'")[1]
    ip = bytes(str(ip), encoding='ascii').decode('unicode-escape')
    return ip

def get_wifi_list():
    ssid_list = []
    p = Popen([file_path + 'get_ssid_names.sh'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    output = str(output).split("\\n")

    for name in output:
        name = bytes(name, encoding='ascii').decode('unicode-escape')
        name = str(name).strip(" ")
        name = name.split('Address: ', 1)[-1]
        if name:
            ssid_list.append(name)
    return ssid_list

def get_credentials_token():
    credentials = ''
    try:
        with open('.credentials', 'r') as file:
            credentials = file.readline()

    except EnvironmentError:
        print("Token error, run 'python3 save_credentials.py'")
    return credentials


def send_attendance(wifi_ssid_list, credentials):
    timestamp = datetime.now().isoformat()
    ip = get_public_ip()
    data = {'username': credentials['username'], 'password': credentials['password'], 'timestamp': timestamp, 'ssids': wifi_ssid_list, 'ip': ip }
    variables = json.dumps(data)
    print(variables)

    url = 'http://127.0.0.1:8000/graphql/?'
    # url = 'https://amfoss.in/graphql/?'
    mutation = '''
        mutation($ssids: String!, $timestamp: DateTime!, $username: String!, $password: String!, $ip: String!)
        {
        
          LogAttendance(username: $username, password: $password, ssids: $ssids, timestamp: $timestamp, ip: $ip)
          {
            id
          }
        }
    '''
    r = requests.post(url, json={'query': mutation, 'variable': variables})


if __name__ == '__main__':
    if not check_internet_connection():
        sys.exit()

    wifi_ssid_list = get_wifi_list()

    if not wifi_ssid_list:
        sys.exit()

    credentials = json.loads(get_credentials_token())

    if not credentials:
        sys.exit()

    send_attendance(wifi_ssid_list, credentials)
