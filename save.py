# Saves password to file

filename = "passwords.txt"

def save(nameOfPassword, password):
    try:
        with open(filename, "a") as userPasswords:
            userPasswords.write(nameOfPassword + ": " + password + "\n")
    except FileNotFoundError:
        msg = "Something went wrong while trying to find the file. Please try again."
        print(msg)