prevStr = input("Please enter the string: ")
spaceIndex = prevStr.find(" ")
newStr = f"{prevStr[spaceIndex + 1 : spaceIndex + 3]}" \
         f"{prevStr[2 : spaceIndex + 1]}" \
         f"{prevStr[:2]}{prevStr[spaceIndex + 3:]}"
print(newStr)

