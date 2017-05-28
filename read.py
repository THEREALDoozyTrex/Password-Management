filename = "passwords.txt"
def read():
    try:
        with open(filename, "r") as passwords:
            contents = passwords.read()
            print(contents)
    except FileNotFoundError:
        print("No passwords yet! Create a password to get started.")