
import json


filename = "masterpass.txt"

def login(username, password):
    contents = ''
    try:
        with open(filename, "r") as masterPass:
            contents = json.loads(masterPass.read())
    except FileNotFoundError:
        print("Sorry, there was an error finding the required file for the application. Please try again!")
    return contents[username] == password

def signup(username, password):
    try:
        with open(filename, "a") as masterPass:
            masterPass.write(json.dumps({username : password}))
    except FileNotFoundError:
        msg = "Something went wrong while trying to find the file. Please try again."
        print(msg)