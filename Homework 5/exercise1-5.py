def id_file(file_Path):
    with open(file_Path + "my_id.txt", "w") as file:
        file.write("First name: Shaden\n")
        file.write("Last name: Ghazalin\n")
        file.write("Age: 23\n")
        file.write("Phone number: 0505292383\n")


def count_frequency_words(file_Path):
    count_dict = {}
    with open(file_Path, "r") as file:
        data = file.read().split()
    for word in data:
        count = count_dict.get(word, 0)
        count += 1
        count_dict[word] = count
    return count_dict


def read_n_lines(file_Path, n):
    with open(file_Path, "r") as file:
        try:
            assert len(file.readlines()) >= n, "The file does not have that many lines"
            file.seek(0)
            nLines = ""
            for line in file.readlines()[:n]:
                nLines += line
            return nLines
        except AssertionError as msg:
            return msg


def longest_word(file_Path):
    max_word = ""
    with open(file_Path, "r") as file:
        data = file.read().split()
    for word in data:
        if len(word) > len(max_word):
            max_word = word
    return max_word


def reverse_words(input_str):
    reversed_str = ""
    _list = input_str.split()
    for word in _list[::-1]:
        reversed_str += word + " "
    return reversed_str


print("Exercise 1")
id_file("./")
print("File opened")
print()
print("Exercise 2")
print(count_frequency_words("./my_id.txt"))
print()
print("Exercise 3")
print(read_n_lines("./my_id.txt", 3))
print(read_n_lines("./my_id.txt", 5))
print()
print("Exercise 4")
print(longest_word("./my_id.txt"))
print()
print("Exercise 5")
print(reverse_words("hello .py"))
print(reverse_words("python Class"))
