import os
import markovify

INPUT_FOLDER = "media/prepared/text"
OUTPUT_FOLDER = "media/echoes/text"
N = 1000
LENGTH = 200

for filename in os.listdir(INPUT_FOLDER):
    with open(INPUT_FOLDER + "/" + filename) as f:
        file_text = f.read()

    text_model = markovify.NewlineText(file_text, well_formed=False)

    with open(OUTPUT_FOLDER + "/" + filename, 'w') as output:
        for i in range(N):
            output.write(text_model.make_short_sentence(LENGTH) + ("\n" if i <= N - 1 else ""))