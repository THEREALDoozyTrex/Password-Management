# Generates Password

import random

def generatePass(length, lettersLower, numbers, specialChars):
    # Generator Nums, Letters, and Chars
    alpha = ["A", "B", "C", "D", "E", "F", "G"]
    alphaLower = ["a", "b", "c", "d", "e", "f", "g"]
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    specialCharactors = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*"]

    password = ""
    chars = alpha

    # Check for user input and make the password customized
    used = 0
    if lettersLower == "Y":
        chars.extend(alphaLower)
        password += alphaLower[random.randint(0, alphaLower.__len__() - 1)]
        used += 1

    if numbers == "Y":
        chars.extend(nums)
        password += nums[random.randint(0, nums.__len__() - 1)]
        used += 1

    if specialChars == "Y":
        chars.extend(specialCharactors)
        password += specialCharactors[random.randint(0, specialCharactors.__len__() - 1)]
        used += 1

    for x in range(0, length - used):
        rand = random.randint(0, chars.__len__() - 1)
        password += chars[rand]

    # Shuffle password string so it's not in order like, LETTERS, LOWER LETTERS, NUMBERS, and SPECIAL CHARACTERS
    pw = list(password)
    random.shuffle(pw)
    password = ''.join(pw)
    return password