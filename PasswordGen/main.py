import random
import sys

def getAlphaChar():
    chars = "abcdefghijklmnopqrstuvwxyz"
    char = ""
    for i in range(9):
        char = chars[random.randint(0,len(chars)-1)]
    return char
def getNumChar():
    chars = "1234567890"
    char = ""
    # randomize 9 times to help not get repeating chars
    for i in range(9):
        char = chars[random.randint(0,len(chars)-1)]
    return char
def getSpecChar():
    chars = "!@#$%^&*-"
    char = ""
    for i in range(9):
        char = chars[random.randint(0,len(chars)-1)]
    return char
def getWord():
    with open("./english-words-master/words_alpha.txt", "r") as file:
        words = file.read()
        wordList = list(map(str,words.split()))
    return random.choice(wordList)

def genPass(length,complexity):
    pwdLen = length
    pwd = ""
    complexity -= 1
    if complexity:
        for i in range(3):
            pwd += getWord()
            if i == 2:              
                words = pwd.split(sep="-")
                num = getNumChar()
                selector = random.randint(0,2)
                temp = words[selector] + str(num)
                words[selector] = temp
                pwd = "-"
                pwd = pwd.join(words)
            else:
                pwd += "-"
    else:
        while pwdLen:
            select = random.randint(0,2)
            match select:
                case 0:
                    pwd += getAlphaChar()
                case 1:
                    pwd += getNumChar()
                case 2:
                    pwd += getSpecChar()
                case _:
                    print("Something went horribly wrong")
            pwdLen-=1




    print("########################\n")
    print(f"Your password is: {pwd}\n")
    print("########################")

if __name__ == "__main__":

    length = input("Length of password (must exceed 8): ")
    complexity = input("Password Complexity:\n\t1. Random letters, numbers, and special characters\n\t2. 3 random words with a number appended (Length does not apply)\n\t>> ")
    genPass(int(length),int(complexity))

