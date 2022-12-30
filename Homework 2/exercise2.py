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
