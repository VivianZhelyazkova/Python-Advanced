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
            f.write(content + "\n")

    elif "Replace" in command:
        cmd, file_name, old_string, new_string = command.split("-")

        file_path = os.path.join("resources", file_name)
        if os.path.exists(file_path):

            with open(file_path, "r+") as f:
                text = f.read()
                new_text = text.replace(old_string, new_string)
                f.seek(0)
                f.write(new_text)
                f.truncate()
        else:
            print("An error occurred")

    elif "Delete" in command:
        file_name = command.split("-")[1]
        file_path = os.path.join("resources", file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            print("An error occurred")

    command = input()
