# n + (n-1) + (n-3) + (n-5) +...
def posSum(n):
    x = n - 1
    if x < 1:
        return 0
    return n + x + posSum(x - 2)


print(posSum(6))
print(posSum(10))
