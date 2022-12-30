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
