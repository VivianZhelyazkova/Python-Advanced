import os
import re

words_path = os.path.join("files", "words.txt")
input_path = os.path.join("files", "input.txt")
output_path = os.path.join("files", "output.txt")

with open(words_path, "w") as file:
    file.write("quick is fault")

with open(input_path, "w") as file:
    file.write("-I was quick to judge him, but it wasn't his fault.\n"
               "-Is this some kind of joke?! Is it?\n"
               "-Quick, hide here…It is safer.")

words_count = {}

words = open(words_path)
words_as_list = words.read().lower().split()

inpt = open(input_path)
inpt_as_str = inpt.read().lower()

for word in words_as_list:
    regex = re.compile(rf"\b{word}\b")
    matches = regex.findall(inpt_as_str)
    words_count[word] = len(matches)

words.close()
inpt.close()

sorted_words = dict(sorted(words_count.items(), key=lambda x: -x[1]))

with open(output_path, "w") as file:
    for word, count in sorted_words.items():
        file.write(f"{word} - {count}\n")

