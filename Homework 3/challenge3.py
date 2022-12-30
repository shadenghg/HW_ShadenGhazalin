def power(a, b):
    if b == 1:
        return a
    elif b == 0:
        return 1
    elif a == 0:
        return 0
    return a * power(a, b - 1)


print(power(3, 2))
