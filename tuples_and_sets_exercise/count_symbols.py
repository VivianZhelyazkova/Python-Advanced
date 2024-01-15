text = list(sorted(input()))
my_dict = {}

for char in text:

    my_dict[char] = text.count(char)

for char in my_dict:
    print(f"{char}: {my_dict[char]} time/s")
