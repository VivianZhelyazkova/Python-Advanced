import os

words_path = os.path.join("files", "words.txt")
input_path = os.path.join("files", "input.txt")

with open(words_path, "w") as file:
    file.write("quick is fault")

with open(input_path, "w") as file:
    file.write("-I was quick to judge him, but it wasn't his fault.\n"
               "-Is this some kind of joke?! Is it?\n"
               "-Quick, hide here…It is safer.")


words = open(words_path)
