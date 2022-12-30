print("Q.1:")
# 1:
# Define a list with my name, last name, age and phone number information
myIdList = ['Shaden', 'Ghazalin', '23', '0505292383']
# for loop to go through all the id list and prints its value.
for value in myIdList:
    print(value)
print()

print("Q.2:")
# 2:
try:
    list1 = [1, 2, 3, 4, 5]
    list2 = [5, 4, 3, 2, 1]
    list3 = []
    # if the 2 lists in the same time so the code will run as required
    # else will print the suitable message.
    assert len(list1) == len(list2), "THE TWO LISTS MUST BE THE SAME LENGTH"
    # Go through all the 2 lists values that exist in index i
    for i in range(len(list1)):
        if list1[i] >= list2[i]:
            list3.append(list1[i])
        else:
            list3.append(list2[i])
    print(list3)
# if the 2 lists aren't the same length, will print the suitable time
# and exit with exit code 0
except AssertionError as msg:
    print(msg)
print()

print("Q.3:")


# 3:
# Define a function that receives a list and returns the number of the odd number and even numbers
def evenOddFun(evenOddList):
    evenCounter, oddCounter, index = 0, 0, 0  # Counters to the odd and even numbers
    # Loop to go through the list
    for value in evenOddList:
        # if we found a value with string type we stop the loop and print it's a string
        if type(value) == str:
            print("It's a string!!")
            break
        # else if all the elements in the list are numbers, so we count the odd numbers and teh even numbers.
        elif value % 2 == 0:
            evenCounter += 1
        else:
            oddCounter += 1
        index += 1
    # checks if we have reached the end of the list.
    if index == len(evenOddList):
        print(f"Number of even numbers: {evenCounter}")
        print(f"Number of odd numbers: {oddCounter}")


evenOddFun([1, 2, 3, 4, 5, 6, 7, 8, 9])
evenOddFun([1, 2, 3, 4, "Oops", 6, 7, 8, 9])
print()

print("Q.4:")


# 4:
# function that receives a list with integer values as it's input
def sumOfList(intList):
    listSum = 0
    # try to calculate the sum of list value
    for value in intList:
        try:
            assert type(value) == int, "INPUT ERROR! THE LIST SHOULD CONTAIN ONLY INTS"
            listSum += value
        except AssertionError as msg:
            return msg
    return listSum


print(sumOfList([1, 2, 3, 4]))
print(sumOfList([1, 'a', 3, 4]))
print()

print("Q.5:")


# 5:
# function that receives a list with integer values as it's input
def multOfList(intList):
    listMult = 1
    # try to calculate the multiply of list value
    for value in intList:
        try:
            assert type(value) == int, "INPUT ERROR! THE LIST SHOULD CONTAIN ONLY INTS"
            listMult *= value
        except AssertionError as msg:
            return msg
    return listMult


print(multOfList([1, 2, 3, 4]))
print(multOfList([1, 'a', 3, 4]))
print()

print("Q.6:")


# 6:
# function that receives a list with integer values as it's input
def minimumOfList(intList):
    minValue = None
    # try to find the minimal value in the list
    for value in intList:
        try:
            assert type(value) == int, "INPUT ERROR! THE LIST SHOULD CONTAIN ONLY INTS"
            if minValue is None or value < minValue:
                minValue = value
        except AssertionError as msg:
            return msg
    return minValue


print(minimumOfList([4, 2, 3, 7]))
print(minimumOfList([1, 'a', 3, 4]))
print()

print("Q.7:")


# 7:
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
print()

# CHALLENGES:
print("Q.8:")


# function receives a list and returns the unique elements
def uniqueList(inputList):
    # Define a empty list
    uniqueListOP = []
    for value in inputList:
        # checks if the element had appeared or not
        if value not in uniqueListOP:
            uniqueListOP.append(value)
    return uniqueListOP


print(uniqueList([1, 2, 3, 3, 3, 3, 4, 5]))

print("Q.9:")
num = 8
for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
print()

print("Q.10:")
# I don't know how to print this using loops ^^
print('****')
print('*')
print('*')
print(' ***')
print('    *')
print('    *')
print('****')
