import os

command = input()

while command != "End":
    if "Create" in command:
        file_name = command.split("-")[1]
        file_path = os.path.join("resources", file_name)
        with open(file_path, "w") as f:
            pass

    elif "Add" in command:
        cmd, file_name, content = command.split("-")
        file_path = os.path.join("resources", file_name)
        with open(file_path, "a") as f:
            f.write(content)
            
    elif "Replace" in command:


    command = input()
