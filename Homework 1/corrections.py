# Q.3:
prevStr = "abc xyz"
spaceIndex = prevStr.find(" ")
newStr = f"{prevStr[spaceIndex + 1: spaceIndex + 3]}" \
         f"{prevStr[2: spaceIndex + 1]}" \
         f"{prevStr[:2]}{prevStr[spaceIndex + 3:]}"
print(newStr)
print()

# Q.4:
def ingFunc(inputStr):
    if len(inputStr) >= 3:
        if inputStr[-3:] == "ing":
            inputStr += "ly"
            print(inputStr)
        else:
            inputStr += "ing"
            print(inputStr)
    else:
        print(inputStr)


ingFunc("string")
ingFunc("str")
ingFunc("aa")
