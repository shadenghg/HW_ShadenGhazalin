def appearancesCounter(inputString):
    # Converts the string into upper case to consider the upper and lower char the same
    inputString = inputString.upper()
    dic = {}    # Initialize an empty dictionary
    # if the char exist as a key in the dictionary, give the count it's value, else give it 0
    for char in inputString:
        count = dic.get(char, 0)
        count += 1
        dic[char] = count   # Update the value of the key char
    return dic


print(appearancesCounter("HANNA"))
print(appearancesCounter("HAnNA"))
