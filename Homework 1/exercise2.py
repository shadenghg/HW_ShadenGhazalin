inputStr = input("Please enter a string: ")  # Receiving input string from the user

''' While: the user inserts an empty string (The user can't insert a string with negative length)
    Or the user inserts a string with length less than 10 (indexes: 0 - 9) so we cant reach all the indexes 7,8,9
    print the suitable message 
    Let the user insert again the string until he inserts the right string '''
while len(inputStr) == 0 or len(inputStr) < 10:
    print("ERROR! You should enter a legal str")
    inputStr = input("Please enter a string: ")

# After receiving the right string from the user now we check as required
if inputStr[7] == "a" and inputStr[8] == "b" and inputStr[9] == "c":
    print(True)
else:
    print(False)
