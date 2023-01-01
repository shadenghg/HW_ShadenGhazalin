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
