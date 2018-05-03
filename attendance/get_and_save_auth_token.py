import getpass
import json
import sys

import requests


def get_and_save_auth_token():
    # curl -X POST -d "username=chirath&password=password" https://amfoss.in/api/auth/token/

    post_url = "http://localhost:8000/api/auth/token/"
    print("Enter your foss website username and password.")
    username = input("username: ")
    password = getpass.getpass("Password: ")
    data = {"username": username, "password": password}
    response = requests.post(url=post_url, data=data)

    data = json.loads(response.text)

    if 'token' not in data.keys():
        print("Cannot get token.")
        print(data)
        sys.exit()

    token = data['token']

    with open('.token', 'w') as file:
        file.write(token)
        print("Token successfully saved, please run this script again in 180 days.")


if __name__ == '__main__':
    get_and_save_auth_token()
