dic1 = {'a': 100, 'b': 200, 'c': 300}
dic2 = {'a': 300, 'b': 200, 'd': 400}
dic3 = {}  # Initialize an empty dictionary
dictSet1 = set(dic1.keys())    # Returns a list containing the dict1's keys and convert it to set
dictSet2 = set(dic2.keys())    # Returns a list containing the dict2's keys and convert it to set
unionKeySet = dictSet1 | dictSet2   # Union the keys of the two dictionaries
# In the for loop, we loop through the Union KeySet to add all the keys in both dictionaries to the empty dictionary
for key in unionKeySet:
    # if the key exist in both dictionaries, then add its value and save it in the third dictionary
    if key in dic1 and key in dic2:
        dic3[key] = dic1[key] + dic2[key]
    # else if the key exist only in the dict1, update the dic3 with the key and value from dic1
    elif key in dic1:
        dic3[key] = dic1[key]
    # else, update the dic3 with the key and value from dic2
    else:
        dic3[key] = dic2[key]

print(dic3)
