import os
from src.extract_text import *

inputFileDirectory = "C:\\Users\\ambarish.singh\\PycharmProjects\\HyperVergeAssignment\\input\\"
outputFileDirectory = "C:\\Users\\ambarish.singh\\PycharmProjects\\HyperVergeAssignment\\output\\"
inputFileName = inputFileDirectory + "inputFile.txt"
outputFileName = outputFileDirectory + "outputFile.txt"

if os.path.exists(outputFileName):
    os.remove(outputFileName)

outputFile = open(outputFileName, "a")
outputFile.write("filename,expected,predicted,correct/wrong\n")
inputFile = open(inputFileName, "r")

lines = inputFile.readlines()

iterLines = iter(lines)
next(iterLines)

for line in iterLines:
    line = line.strip()
    row = line.split(',')  # separates line into a list of items.  ',' tells it to split the lines at the commas
    image_name = row[0]
    image_expected_value = row[1]
    image_predicted_value = extract_text_from_image(image_name)
    if image_expected_value != image_predicted_value:
        result = "wrong"
    else:
        result = "correct"
    # print(image_name + "\t" + image_expected_value)
    #print(extract_text_from_image(image_name))
    print(image_name + "," + image_expected_value + "," + image_predicted_value + "," + result)
    outputFile.write(image_name + "," + image_expected_value + "," + image_predicted_value + "," + result+"\n")

inputFile.close()
outputFile.close()