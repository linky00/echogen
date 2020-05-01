import os
import moviepy.editor as editor
import random

INPUT_FOLDER = "media/prepared/video"
OUTPUT_FOLDER = "media/echoes/video"
CLIPS_PER_VIDEO = 3
MIN_LENGTH = 3.0
MAX_LENGTH = 7.0

for filename in os.listdir(INPUT_FOLDER):
    name, extension = os.path.splitext(filename)
    if extension in [".mp4", ".ogv", ".webm"]:
        for i in range(CLIPS_PER_VIDEO):
            clip = editor.VideoFileClip(INPUT_FOLDER + "/" + filename)
            desired_length = random.uniform(MIN_LENGTH, min(MAX_LENGTH, clip.duration))
            subclip_start = random.uniform(0.0, clip.duration - desired_length)
            subclip_end = subclip_start + desired_length
            print(f"file {filename}")
            print(f"clip {i}")
            print(f"length {desired_length}")
            print(f"start {subclip_start}")
            print(f"end {subclip_end}")
            subclip = clip.subclip(subclip_start, subclip_end)
            mp4_out = OUTPUT_FOLDER + "/TEMP.mp4" # BECAUSE APPARENTLY EVERYTHING COCKS UP OGV BUT HANDBRAKE
            actual_out = OUTPUT_FOLDER + "/" + name + "-" + str(i) + ".ogv" 
            subclip.write_videofile(mp4_out)
            os.system("ffmpeg -i " + mp4_out + " -q:v 10 " + actual_out)
            os.remove(mp4_out)
