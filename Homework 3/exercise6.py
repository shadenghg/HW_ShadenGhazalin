dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = {}   # Initialize an empty dictionary
# Go through all the given dictionary and update there values and keys in the 4th dictionary
for key in (dic1, dic2, dic3):
    dic4.update(key)
print(dic4)
