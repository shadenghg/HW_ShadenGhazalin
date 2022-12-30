"""The function: sorted(iterable, key=key, reverse=reverse)
    iterable: The data collection we want to sort (Required).
    key: The order we want to sort the data collection in, Default is None (Optional)
    reverse: A Boolean value, False will sort ascending, True will sort descending, Default is False (Optional) """


def lexicographicallySort(unsortedStr):
    return sorted(sorted(unsortedStr), key=str.upper)


unsortedString = input("Please enter a string: ")
print(f"The string after sorting: {lexicographicallySort(unsortedString)}")
