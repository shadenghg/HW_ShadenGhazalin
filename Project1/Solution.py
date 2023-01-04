import re


# PART 1:
# Function receives 2 lists, and merge them into a dictionary
# And returns the merged dictionary
def merge_Lists(list1, list2):
    dict3 = {}
    for key1, key2 in zip(list1, list2):
        dict3[key1] = key2
        dict3[key2] = key1
    return dict3


# Function receives input string
# And returns connection between the 4 common letters in the input text we received with ['e', 't', 'o', 'r']
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
    return merge_Lists(list(counter_Dic.keys()), ['e', 't', 'o', 'r'])


# PART 2: Functions receives a string as an input The function will go over the string text:
# if: The character will be found as a key in the dictionary that was created in part 1
# then the character will be replaced by its key value
# else: The character will stay the same.</li> The function returns the text after changing.
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
# Function receives a path
# And open the following text files:
def encryption_files(file_Path):
    # first text file in writing + reading mode
    # In this file we add the required text.
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

    # Second text file opened with writing mode
    # includes the decrypted and encrypted text
    with open(file_Path + "/Translated File.txt", "w") as translated_File:
        translated_File.write(data + '\n')
        translated_File.write("The encryption for the above text is:\n")
        translated_File.write(translated_txt)

    # Third text file opened with writing mode
    # includes the encrypted text only
    with open(file_Path + "/result.txt", "w") as results_file:
        results_file.write(translated_txt)


# PART 4:
# Function receives a file path and open it
# returns the longest word in the file
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


# Function receives a path of text file
# open it, and returns the number of lines in the file
def count_File_Lines(file_Path):
    with open(file_Path + "/result.txt", "r") as file:
        return len(file.readlines())


# Main function!
# In the main function we define the path of the file we want to open
def main():
    file_Path = "C:/Samana/HW_ShadenGhazalin/Project1"
    encryption_files(file_Path)
    # open the result file to write the longest word multiples of lines in the file.
    with open(file_Path + "/result.txt", "a") as file:
        file.write("\n")
        file.write((find_Longest_Word(file_Path).upper() + ' ') * count_File_Lines(file_Path) + " \n")
        # writing to the result file the cross pattern that means I'M DEAD
        for i in range(7):
            for j in range(7):
                if i == j or (6 - j) == i:
                    file.write('*')
                else:
                    file.write(' ')
            file.write('\n')


# Run the main.
if __name__ == "__main__":
    main()
