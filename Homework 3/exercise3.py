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
