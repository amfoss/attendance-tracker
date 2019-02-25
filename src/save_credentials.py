import getpass
import json
file_path = "/opt/attendance"

def get_and_save_auth_token():
    print("Enter your foss website username and password.")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    data = {"username": username, "password": password}

    with open('.credentials', 'w') as file:
        json.dump(data, file)
        print("Token successfully saved, please run this script whenever you change your credentials.")

if __name__ == '__main__':
    get_and_save_auth_token()
