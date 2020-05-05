import sys
import os
import codecs
import markovify

N = 1000
LENGTH = 200

input_folder = sys.argv[1] + "/prepared/text"
output_folder = sys.argv[1] + "/echoes/text"

for filename in os.listdir(input_folder):
    with codecs.open(input_folder + "/" + filename, encoding='utf-8', errors='ignore') as f:
        file_text = f.read()
    text_model = markovify.NewlineText(file_text, well_formed=False)
    with open(output_folder + "/" + filename, 'w') as output:
        for i in range(N):
            output.write(text_model.make_short_sentence(LENGTH) + ("\n" if i <= N - 1 else ""))