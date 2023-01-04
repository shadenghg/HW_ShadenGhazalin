import re


# PART 1:
def swipKeys(list1, list2):
    dict3 = {}
    for key1, key2 in zip(list1, list2):
        dict3[key1] = key2
        dict3[key2] = key1
    return dict3


def common_Letters(input_Str):
    dic = {}
    for _value in input_Str:
        for char in _value:
            if char.isalpha():
                char = char.lower()
                count = dic.get(char, 0)
                count += 1
                dic[char] = count  # Update the value of the key char
    counter_Dic = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True)[:4])
    return swipKeys(list(counter_Dic.keys()), ['e', 't', 'o', 'r'])


# PART 2:
def replace_Letters(input_Str):
    common_Letters_Dic = common_Letters(input_Str)
    replaced_txt = ''
    for char in input_Str:
        char = char.lower()
        if char in list(common_Letters_Dic.keys()):
            char = common_Letters_Dic[char]
        replaced_txt = replaced_txt + char
    return replaced_txt


# PART 3:
def encryption_files(file_Path):
    with open(file_Path + "/Original.txt", "w+") as input_file:
        input_file.write("'Puackich, hvhnkrally oaths phufhck. All ymr nhhd is Pykemn.'\n")
        input_file.write('J.U.U.U Kmltin.\n')
        input_file.write('mmps iks nmk eio; ---> hkmu\n')
        input_file.seek(0)
        data = input_file.read()
        translated_txt = ''
        for char1, char2 in zip(data, replace_Letters(data)):
            if char1.isupper():
                char2 = char2.upper()
            translated_txt = translated_txt + char2

    with open(file_Path + "/Translated File.txt", "w") as translated_File:
        translated_File.write(data + '\n')
        translated_File.write("The encryption for the above text is:\n")
        translated_File.write(translated_txt)

    with open(file_Path + "/result.txt", "w") as results_file:
        results_file.write(translated_txt)


# PART 4:
def find_Longest_Word(file_Path):
    with open(file_Path + "/result.txt", "r") as file:
        data = file.read()
    regex = re.compile('[^a-zA-Z]')
    max_word = ''
    words_List = regex.sub(' ', data)
    words_List = words_List.split()
    for index in range(len(words_List)):
        if len(words_List[index]) > len(max_word):
            max_word = words_List[index]
    return max_word


def count_File_Lines(file_Path):
    with open(file_Path + "/result.txt", "r") as file:
        return len(file.readlines())


def main():
    file_Path = "C:/Samana/HW_ShadenGhazalin/Project1"
    encryption_files(file_Path)
    with open(file_Path + "/result.txt", "a") as file:
        file.write("\n")
        file.write((find_Longest_Word(file_Path).upper() + ' ') * count_File_Lines(file_Path) + " \n")
        for i in range(7):
            for j in range(7):
                if i == j or (6 - j) == i:
                    file.write('*')
                else:
                    file.write(' ')
            file.write('\n')


if __name__ == "__main__":
    main()
