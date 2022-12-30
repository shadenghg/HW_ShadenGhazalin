# Define a function that receives a list and returns the number of the odd number and even numbers
def evenOddFun(evenOddList):
    evenCounter, oddCounter, index = 0, 0, 0    # Counters to the odd and even numbers
    # Loop to go through the list
    for value in evenOddList:
        # if we found a value with string type we stop the loop and print it's a string
        if type(value) == str:
            print("It's a string!!")
            break
        # else if all the elements in the list are numbers so we count the odd numbers and teh even numbers.
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
