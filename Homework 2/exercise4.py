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
