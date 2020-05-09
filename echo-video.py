import sys
import os
import moviepy.editor as editor
import random

CLIPS_PER_MINOR_VIDEO = 3
CLIPS_PER_MAJOR_VIDEO = 8
MIN_LENGTH = 3.0
MAX_LENGTH = 7.0
HEIGHT = 144

minor_input_folder = sys.argv[1] + "/prepared/video/minor"
major_input_folder = sys.argv[1] + "/prepared/video/major"
output_folder = sys.argv[1] + "/echoes/video"

def echo_folder(input_folder, clips):
    for filename in os.listdir(input_folder):
        name, extension = os.path.splitext(filename)
        if extension in [".mp4", ".ogv", ".webm"]:
            examine_clip = editor.VideoFileClip(input_folder + "/" + filename)
            small_size = (HEIGHT, int(examine_clip.w / examine_clip.h * HEIGHT))
            for i in range(clips):
                clip = editor.VideoFileClip(input_folder + "/" + filename, target_resolution=small_size)
                if clip.rotation in [90, 270]:
                    clip = clip.resize(clip.size[::-1])
                    clip.rotation = 0
                desired_length = random.uniform(min(MIN_LENGTH, clip.duration), min(MAX_LENGTH, clip.duration))
                subclip_start = random.uniform(0.0, clip.duration - desired_length)
                subclip_end = subclip_start + desired_length
                subclip = clip.subclip(subclip_start, subclip_end)
                mp4_out = output_folder + "/TEMP.mp4"
                actual_out = output_folder + "/" + name + "-" + str(i) + ".ogv" 
                subclip.write_videofile(mp4_out)
                os.system("ffmpeg -i " + mp4_out + " -q:v 10 \"" + actual_out + "\"")
                os.remove(mp4_out)

echo_folder(minor_input_folder, CLIPS_PER_MINOR_VIDEO)
echo_folder(major_input_folder, CLIPS_PER_MAJOR_VIDEO)