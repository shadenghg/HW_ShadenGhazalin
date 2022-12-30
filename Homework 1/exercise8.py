"""
=> In this question we used the format method.
S.format(*args, **kwargs) -> str
Return a formatted version of S, using substitutions from args and kwargs.
The substitutions are identified by braces ('{' and '}').
"""
x = 3.1415926
y = 12.9999
print(f"Original Number: {x}")
print("Formatted Number: "+"{:.2f}".format(x))
print("Original Number: ", y)
print("Formatted Number: "+"{:.2f}".format(y))
