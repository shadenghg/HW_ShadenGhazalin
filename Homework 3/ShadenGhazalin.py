print("Q.1:")
# Prints my identification information (the phone number is a string because the int can't start with 0
print({('name', 'LastName'): 'Shaden Ghazalin', 'Age': 23, 'Phone Number': '0505292383'})
print()

print("Q.2:")


# function that receives a list
def replaceFifthIndex(inputList):
    # Try to replace the fifth index
    try:
        inputList[5] = '@'
    # if the fifth index doesn't exist return the indexError exception
    except IndexError:
        return "The list is too short"
    # if there is no exception return the updated list
    else:
        return inputList


print(replaceFifthIndex([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(replaceFifthIndex([1, 2, 3, 4, 5]))
print()

print("Q.3:")


# function that receives a list
def replaceFifthIndexAssert(inputList):
    try:
        # if the length of the input list is shorter than 6 then print "The list is too Short"
        # else replace the fifth index and return the updated list
        assert len(inputList) >= 6, "The list is too short"
        inputList[5] = '@'
        return inputList
    # return the message of the assertion error
    except AssertionError as msg:
        return msg


print(replaceFifthIndexAssert([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(replaceFifthIndexAssert([1, 2, 3, 4, 5]))
print()

print("Q.4:")


# function that receives a dictionary, key and value
def updateDict(inputDict, inputKey, value):
    # update the input dictionary with
    inputDict.update({inputKey: value})
    return inputDict


diction = {('name', 'LastName'): 'Shaden Ghazalin', 'Age': 23, 'Phone Number': '0505292383'}
print(updateDict(diction, 'Age', 25))
print(updateDict(diction, 'Height', 1.65))
print()

print("Q.5:")
n = 5
diction = {}  # Initialize an empty dictionary
# Filling the dictionary x for the key and x + 3 for its value
for x in range(1, n + 1):
    diction[x] = x + 3
print(diction)
print()

print("Q.6:")
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = {}  # Initialize an empty dictionary
# Go through all the given dictionary and update there values and keys in the 4th dictionary
for key in (dic1, dic2, dic3):
    dic4.update(key)
print(dic4)
print()

print("Q.7:")


def appearancesCounter(inputString):
    # Converts the string into upper case to consider the upper and lower char the same
    inputString = inputString.upper()
    dic = {}  # Initialize an empty dictionary
    # if the char exist as a key in the dictionary, give the count it's value, else give it 0
    for char in inputString:
        count = dic.get(char, 0)
        count += 1
        dic[char] = count  # Update the value of the key char
    return dic


print(appearancesCounter("HANNA"))
print(appearancesCounter("HAnNA"))
print()

print("Q.8:")
dic1 = {'a': 100, 'b': 200, 'c': 300}
dic2 = {'a': 300, 'b': 200, 'd': 400}
dic3 = {}  # Initialize an empty dictionary
dictSet1 = set(dic1.keys())  # Returns a list containing the dict1's keys and convert it to set
dictSet2 = set(dic2.keys())  # Returns a list containing the dict2's keys and convert it to set
unionKeySet = dictSet1 | dictSet2  # Union the keys of the two dictionaries
# In the for loop, we loop through the Union KeySet to add all the keys in both dictionaries to the empty dictionary
for key in unionKeySet:
    # if the key exist in both dictionaries, then add its value and save it in the third dictionary
    if key in dic1 and key in dic2:
        dic3[key] = dic1[key] + dic2[key]
    # else if the key exist only in the dict1, update the dic3 with the key and value from dic1
    elif key in dic1:
        dic3[key] = dic1[key]
    # else, update the dic3 with the key and value from dic2
    else:
        dic3[key] = dic2[key]

print(dic3)
print()

print("Q.9:")


def factorial(num):
    # stop conditions:
    if num == 0:
        return 1
    try:
        assert num > 0, 'The input should be a positive number :) '
        return num * factorial(num - 1)
    # return the message of the assertion error
    except AssertionError as msg:
        return msg


print(f"Input a number to compute the factorial: {factorial(5)}")
print(factorial(-7))
print(factorial(0))
print()

print("Q.10:")


# n + (n-1) + (n-3) + (n-5) +...
def posSum(n):
    x = n - 1
    if x < 1:
        return 0
    return n + x + posSum(x - 2)


print(posSum(6))
print(posSum(10))
print()

print('Q.11:')


def power(a, b):
    if b == 1:
        return a
    elif b == 0:
        return 1
    elif a == 0:
        return 0
    return a * power(a, b - 1)


print(power(3, 2))
