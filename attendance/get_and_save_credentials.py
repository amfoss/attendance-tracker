import getpass
import json


def get_and_save_credentials():
    print("Enter your amFOSS CMS Username and Password.")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    data = {"username": username, "password": password}
    # Saves username and password
    with open('.credentials', 'w') as file:
        json.dump(data, file)
        print("Successfully saved, please run this script whenever you change your credentials.")


if __name__ == '__main__':
    get_and_save_credentials()