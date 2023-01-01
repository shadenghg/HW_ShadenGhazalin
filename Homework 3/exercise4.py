# function that receives a dictionary, key and value
def updateDict(inputDict, key, value):
    # update the input dictionary with
    inputDict.update({key: value})
    return inputDict


diction = {('name', 'LastName'): 'Shaden Ghazalin', 'Age': 23, 'Phone Number': '0505292383'}
print(updateDict(diction, 'Age', 25))
print(updateDict(diction, 'Height', 1.65))
