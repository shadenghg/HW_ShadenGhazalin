# Function accepts a string
def upperAndLowerCase(inputString):
    # upper and lower chars counters
    upperCharCount, loweCharCount = 0, 0
    # Loop to count the upper and lower chars
    for char in inputString:
        # Checks if the chars are upper case
        if char.islower():
            loweCharCount += 1
        # Checks if the chars are lower case
        elif char.isupper():
            upperCharCount += 1
    print("Original string : ", inputString)
    print("No. of Upper case characters : ", upperCharCount)
    print("No. of lower case characters : ", loweCharCount)


upperAndLowerCase("Shaden Ghazalin")
