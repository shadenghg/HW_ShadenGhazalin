# Function to insert a string in the space of original string.
def insertStringInSpace(originalStr, additionalStr):
    spaceIndex = originalStr.find(" ")
    return f"{originalStr[:spaceIndex + 1]}{additionalStr} {originalStr[spaceIndex + 1:]}"


original = input("Please insert a string contains space: ")

''' While: the user inserts a string that doesn't include a space " "
    print the suitable message 
    Let the user insert again the string until he inserts the right string '''
checkSpace = True  # A flag of finding a space.
while original.find(" ") == -1:
    checkSpace = False
    print("ILLEGAL INPUT")
    original = input("Please insert a string contains space: ")

# After receiving the Legal string.
additional = input("Please enter the new string: ")
print(insertStringInSpace(original, additional))  # Calling the function that we wrote.
