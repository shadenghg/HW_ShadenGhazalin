prevStr = input("Please enter a string with at least 3 characters: ")

''' While: the user inserts a string with length less than 3 (indexes: 0 - 2)
    print the suitable message 
    Let the user insert again the string until he inserts the right string '''
while len(prevStr) < 3:
    print("ILLEGAL INPUT")
    prevStr = input("Please enter a string with at least 3 characters: ")

midIndex = len(prevStr)//2  # Calculate the middle index.

# Creating the new string as required
newStr = f"{prevStr[midIndex]}" \
         f"{prevStr[1 : midIndex]}" \
         f"{prevStr[-1]}" \
         f"{prevStr[midIndex + 1 : -1]}" \
         f"{prevStr[0]}"
print(f"{prevStr} -> {newStr}")
