import os

path = os.path.join("files", "text.txt")

try:
    open(path, "r")
    print("File found")

except FileNotFoundError:
    print("File not found")


