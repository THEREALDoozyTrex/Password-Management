
filename = "passwords.py"

def clear(allOrOnePass):
    if allOrOnePass.upper() == "ALL":
        try:
            with open(filename, "w") as userPasswords:
                userPasswords.write("")
        except FileNotFoundError:
            msg = "Something went wrong while trying to find the file. Please try again."
            print(msg)
    elif allOrOnePass.upper() == "ONE":
        try:
            with open(filename, "r") as userPasswords:
                lines = userPasswords.readlines()
                for line in lines:
                    print(line.rstrip())
        except FileNotFoundError:
            msg = "Something went wrong while trying to find the file. Please try again."
            print(msg)