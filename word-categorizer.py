"""
Program: Word Categorizer
Developer: Magg Lui
Last Modified: 2023-07-01
"""
import os

# Create a project folder if it does not already exist
currentDir = os.getcwd()
newDir = "word-categorizer"

if not os.path.exists(newDir):
    os.mkdir(newDir)
    print(f"Created \'{newDir}\' directory in \'{currentDir}\'.")
else:
    print(f"\'{newDir}\' directory already exists in \'{currentDir}\'.")

print("")                                          # print a blank line for higher readability


# Load the txt file and convert the content to a list
filepath = "18887916.txt"
with open(filepath, "r") as file:
    print(f"Loading file from \'{currentDir}\\{filepath}'.")
    text = file.read()                             # store the original text to a variable
    formatText = text                              # create another variable for formatting the contents

    while formatText.find("\n\n") != -1:           # first remove any blank lines
        formatText = formatText.replace("\n\n", "\n")
    formatText = formatText.replace("\n", " ")     # then replace all line breaks with a space
    content = formatText.split(" ")                # split the items by white space and return a list
    print("The file content is converted to a list.")
    print(f"Total Items in List: {len(content)}")  # print the no. of items in the list

    print("")                                      # print a blank line for higher readability

    # if the list item is alpha, add it to a txt file in the new directory created earlier
    # the file name will be the first letter of the word
    # each word will be added in a new line
    for word in content:
        if word.isalpha():
            with open(f"{newDir}\\{word[0].upper()}.txt", "a") as newFile:
                newFile.write(word + "\n")
    print("Creating text files with alphabet names.")

# Find the total number of txt files created
textFiles = os.listdir(newDir)
print("Total Text Files: " + str(len(textFiles)))

print("")                                          # print a blank line for higher readability


# Find the number of words in each txt file
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
fileDict = {key: 0 for key in alphabet}            # set the default values to be 0 in the dictionary
for fileName in textFiles:
    with open(f"{newDir}\\{fileName}", "r") as subFile:
        wordNum = len(subFile.readlines())         # the readlines method returns a list of all lines in the file
        fileDict[f"{fileName[0]}"] = wordNum       # update the dict values based on the first letter in the file name


# Print the word count for each file
# for simplicity, the word counts are concatenated into one single string for printing
output = ""
for letter in alphabet:
    output += f"{letter} : {fileDict[letter]:<10}" # {:<10} restricts the field to be left aligned with a width of 10
    if (alphabet.index(letter) + 1) % 6 == 0:      # add a line break every six letters for higher readability
        output += "\n"

print(output)
