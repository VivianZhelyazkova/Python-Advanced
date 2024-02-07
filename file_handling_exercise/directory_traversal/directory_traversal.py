import os

searched_dir = input("Select a directory: ")


def get_extensions(some_dir, depth_counter):

    directory = os.listdir(some_dir)

    for file_name in directory:

        file_path = os.path.join(some_dir, file_name)

        if os.path.isfile(file_path):
            extension = os.path.splitext(file_name)[1]
            if extension in extensions:
                extensions[extension].append(file_name)
            else:
                extensions[extension] = [file_name]

        elif os.path.isdir(file_path):
            if depth_counter == 0:
                return
            get_extensions(file_path, depth_counter - 1)


extensions = {}
report = []

try:
    get_extensions(searched_dir, 1)
except FileNotFoundError:
    print("Directory not found")

extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, names in extensions:
    report.append(f"{extension}")
    for name in sorted(names):
        report.append(f"- - - {name}")

with open("report.txt", 'w') as f:
    f.write("\n".join(report))

print(f"Report file has been generated at {os.path.dirname(os.path.abspath(__file__))} as report.txt")
