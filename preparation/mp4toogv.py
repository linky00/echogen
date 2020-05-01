"""
Converts mp4 to ogv (needs ffmpeg)
"""

import os

INPUT_FOLDER = "media/1-original/video"
OUTPUT_FOLDER = "media/2-prepared/video"

for filename in os.listdir(INPUT_FOLDER):
    name, extension = os.path.splitext(filename)
    if extension == ".mp4":
        input_path = INPUT_FOLDER + "/" + filename
        output_path = OUTPUT_FOLDER + "/" + name + ".ogv"
        os.system("ffmpeg -i " + input_path + " -q:v 10 " + output_path)