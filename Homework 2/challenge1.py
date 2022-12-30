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
