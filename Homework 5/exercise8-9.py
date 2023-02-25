def is_Valid(input_Str):
    parentheses = {"(": ")", "{": "}", "[": "]"}
    brackets_List = []
    for brackets in input_Str:
        if brackets in parentheses:
            brackets_List.append(brackets)
        elif len(brackets_List) == 0 or parentheses[brackets_List.pop()] != brackets:
            return False
    return len(brackets_List) == 0


def subsets_func(number_set):
    # Base case
    if len(number_set) == 0:
        return [[]]

    subset = []
    first_element = number_set[0]
    rest_set = number_set[1:]
    rest_subset = subsets_func(rest_set)
    # Generate subsets including first element
    for sublist in rest_subset:
        subset.append([first_element] + sublist)
    # Generate subsets excluding first element
    subset.extend(rest_subset)
    return subset


print(is_Valid("(){}[]"))
print(is_Valid("({[)]"))
print(is_Valid("{{{"))
print(is_Valid("({[}])"))

print(subsets_func([4, 5, 6, 7, 8]))
