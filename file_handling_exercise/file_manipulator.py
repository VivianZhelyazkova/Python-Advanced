import os

command = input()

while command != "End":
    cmd, *info = command.split("-")
    file_name = info[0]
    file_path = os.path.join("resources", file_name)

    if cmd == "Create":
        with open(file_path, "w") as f:
            pass

    elif cmd == "Add":
        content = info[1]
        with open(file_path, "a") as f:
            f.write(content + "\n")

    elif "Replace" in command:
        old_string, new_string = info[1], info[2]
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
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            print("An error occurred")

    command = input()
