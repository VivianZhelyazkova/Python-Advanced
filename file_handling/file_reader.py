import os

path = os.path.join("files", "numbers.txt")

text_wrapper = open(path)
file_contents = (text_wrapper.read()).split("\n")

print(sum(int(n) for n in file_contents))
