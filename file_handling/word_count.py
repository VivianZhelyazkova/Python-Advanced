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
words_as_list = words.read().lower().split()
words_count = {}
inpt = open(input_path)
inpt_as_str = inpt.read().lower().split()

for word in words_as_list:
    words_count[word] = inpt_as_str.count(word)

words.close()
inpt.close()

sorted_words = sorted(words_count.items(), key=lambda x: -x[1])

print(sorted_words)
