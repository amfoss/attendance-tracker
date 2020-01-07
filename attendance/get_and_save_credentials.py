import getpass
import json
import requests

def get_and_save_credentials():
    print("Enter your amFOSS CMS Username and Password.")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    data = {"username": username, "password": password}
    variables = json.dumps(data)
    url = 'https://api.amfoss.in/?'
    mutation = '''
    mutation TokenAuth($username: String!, $password: String!) {
        tokenAuth(username: $username, password: $password) {
            token
            refreshToken
        }
    }
    '''
    r = requests.post(url, json={'query': mutation, 'variables': variables})
    if str(r.json())[2:8] == "errors":
        print("Try again, please enter valid credentials")
        get_and_save_credentials()
    else:
        # Saves username and password
        with open('.credentials', 'w') as file:
            json.dump(data, file)
            print("Successfully saved, please run this script whenever you change your credentials.")


if __name__ == '__main__':
    get_and_save_credentials()