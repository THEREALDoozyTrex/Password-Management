import generate as gen
import save as save
import read as read
import accountManagement as am
#import clear as clear

# DAY ONE: 169 LINES OF CODE

def account():
    loginOrSignup = input("Do you want to login (L) or signup (S): ")
    if loginOrSignup.upper() == "L":
        def tryLogin():
            usernameInput = input("Type in the username: ")
            masterPassInput = input("Type in the master password: ")
            if am.login(usernameInput, masterPassInput) == usernameInput and masterPassInput:
                #reMe = input("Do you want to remember this password (Y/N): ")
                # TODO: REMEMBER ME
                # if reMe.upper() == "Y":
                    #rememberMe = True
                    #run()
                run()
            else:
                yayOrNay = input("Incorrect password. To try again type 'N' If you don't have an account, signup by typing 'S': ")
                if yayOrNay.upper() == "S":
                   account()
                else:
                    tryLogin()
        tryLogin()

    elif loginOrSignup.upper() == "S":
        usernameSignup = input("Type in the username: ")
        masterPassSignup = input("Type in a master password: ")
        am.signup(usernameSignup, masterPassSignup)
        run()

def run():
    main = input("New password 'N', read password(s) 'R', or clear 'C' your password(s): ")
    if main.upper() == "N":
        print("Answer with 'Y' for YES, and 'N' for no.")
        userLength = input("Length of password: ")
        userLowerLetters = input("What about lowercase letters in the password: ")
        userNumbers = input("Do you want numbers in the password: ")
        userChars = input("Do you want special charactors in the password?")
        newPassword = gen.generatePass(int(userLength), userLowerLetters.upper(), userNumbers.upper(), userChars.upper())
        print(newPassword)
        saveOrNot = input("Would you like to save the password: ")
        if saveOrNot.upper() == "Y":
            nameOfPassword = input("What is the passwords name?")
            save.save(nameOfPassword, newPassword)
            run()
        else:
            run()
    elif main.upper() == "R":
        read.read()
        run()
    '''elif main.upper() == "C":
        allOrOne = input("Clear all (ALL) passwords or one (ONE) (TYPE 'BACK' TO GO BACK): ")
        if allOrOne.upper() == "ALL":
            clear.clear("ALL")
        elif allOrOne.upper() == "ONE":
            clear.clear("ONE")
        elif allOrOne.upper() == "BACK":
            run()'''

account()
