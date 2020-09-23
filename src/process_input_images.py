import os
from src.extract_text import *


def process_images():
    input_file_directory = "C:\\Users\\ambarish.singh\\PycharmProjects\\HyperVergeAssignment\\input\\"
    output_file_directory = "C:\\Users\\ambarish.singh\\PycharmProjects\\HyperVergeAssignment\\output\\"
    input_file_name = input_file_directory + "inputFile.txt"
    output_file_name = output_file_directory + "outputFile.txt"
    if os.path.exists(output_file_name):
        os.remove(output_file_name)
    output_file = open(output_file_name, "a")
    output_file.write("filename,expected,predicted,correct/wrong\n")
    input_file = open(input_file_name, "r")
    lines = input_file.readlines()
    iter_lines = iter(lines)
    next(iter_lines)
    for line in iter_lines:
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
        # print(extract_text_from_image(image_name))
        print(image_name + "," + image_expected_value + "," + image_predicted_value + "," + result)
        output_file.write(image_name + "," + image_expected_value + "," + image_predicted_value + "," + result + "\n")
    input_file.close()
    output_file.close()