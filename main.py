from src.generate_input_file import *
from src.process_input_images import *

#consolidate all the image names and their predicted results in a single input file

generate_input_file()

#iterate through the input file to make api calls to Microsoft Vision API to extract text from images

process_images()
