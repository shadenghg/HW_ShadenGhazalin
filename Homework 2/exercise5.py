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
