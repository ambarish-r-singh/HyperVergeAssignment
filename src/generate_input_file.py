import os
import re

_nsre = re.compile('([0-9]+)')


def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(_nsre, s)]


# Generate input File to write the extracted car number text
inputFileDirectory = "C:\\Users\\ambarish.singh\\PycharmProjects\\HyperVergeAssignment\\input\\"
inputFileName = inputFileDirectory + "inputFile.txt"
if os.path.exists(inputFileName):
    os.remove(inputFileName)
inputFile = open(inputFileName, "a")
inputFile.write("filename,expected\n")

# Traverse through the directory containing the text files.
directory = "C:\\Users\\ambarish.singh\\PycharmProjects\\HyperVergeAssignment\\input\\groundtruth\\"
fileList = os.listdir(directory)
fileList.sort(key=natural_sort_key)
for filename in fileList:
    if filename.endswith(".txt"):
        f = open(directory + filename)
        lines = f.read()
        inputFile.write(filename.replace(".txt", ".jpg") + "," + lines.strip() + "\n")
