def factorial(num):
    # stop conditions:
    if num == 0:
        return 1
    try:
        assert num > 0, 'The input should be a positive number :) '
        return num * factorial(num-1)
    # return the message of the assertion error
    except AssertionError as msg:
        return msg


print(f"Input a number to compute the factorial: {factorial(5)}")
print(factorial(-7))
print(factorial(0))
