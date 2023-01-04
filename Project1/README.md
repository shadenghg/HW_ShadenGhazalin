# PROJECT 1:
## CREATOR: SHADEN GHAZALIN
___
## REQUIREMENTS:
### PART 1:
#### Input:
The function in this part receives text (String) from the user (Or in the rest of the code).
#### Output:
The function returns a dictionary that saves the connection between the 4 common letters in the input text we received with ['e', 't', 'o', 'r'].<br> 
The expected output dictionary is: {'h': 'e', 'e': 'h', 'k': 't', 't': 'k', 'm': 'o', 'o': 'm', 'u': 'r', 'r': 'u'}.

### PART 2:
#### Input:
The function in this part receives a string text.
#### Output:
The function will go over the string text:
    <li> If: The character will be found as a key in the dictionary that was created in part 1 then the character will be replaced by its key value.</li>
    <li> Else: The character will stay the same.</li>
The function returns the text after changing.

### PART 3:
#### Input:
The function in this part receives a path to text file as input.
#### Output:
Creates 3 Files using the path we received:
    <li>Original text file: with the encrypted text.</li>
    <li>Translated text file: includes the encrypted and decrypted text.</li>
    <li>Result file: includes the decrypted text.</li>

### PART 4:
#### Input:
The two functions receive a path to text file.
#### Output:
The functions return:
    <li>The first function returns the longest world in the text file.</li>
    <li>The second function returns the number of lines</li>

### Main():
In the main func we add to the result file the longest world multiples of lines in the file.<br>
And print cross pattern at the end of the result text file.

>Runs the main functions using:<br>
> if __name__ = "__main__":<br>
> main()

___
## DESIGN:
### START
    Run the main
    Open Original.txt file.
    Read the datat from the Original.txt and returns the requried dictionary
    Trsndlste the test.
    Add the tests (Original + Dicrypted) into the files.
    Returns the longest word.
    Returns the number of lines in result.txt
    Add to the result text file the longest world multiples of lines in the file.
    Add to the result text file cross patterns.
### END