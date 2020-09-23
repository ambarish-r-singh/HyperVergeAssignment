import os
import re

_nsre = re.compile('([0-9]+)')


def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(_nsre, s)]


# Generate input File to write the extracted car number text
def generate_input_file():
    input_file_directory = "C:\\Users\\ambarish.singh\\PycharmProjects\\HyperVergeAssignment\\input\\"
    input_file_name = input_file_directory + "inputFile.txt"
    if os.path.exists(input_file_name):
        os.remove(input_file_name)
    input_file = open(input_file_name, "a")
    input_file.write("filename,expected\n")

    # Traverse through the directory containing the text files.
    directory = "C:\\Users\\ambarish.singh\\PycharmProjects\\HyperVergeAssignment\\input\\groundtruth\\"
    file_list = os.listdir(directory)
    file_list.sort(key=natural_sort_key)
    for filename in file_list:
        if filename.endswith(".txt"):
            f = open(directory + filename)
            lines = f.read()
            input_file.write(filename.replace(".txt", ".jpg") + "," + lines.strip() + "\n")


pass
