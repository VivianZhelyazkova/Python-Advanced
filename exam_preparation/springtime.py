def start_spring(**kwargs):
    objects = {}
    result = ""
    for k, v in kwargs.items():
        if v not in objects:
            objects[v] = [k]
        else:
            objects[v].append(k)

    sorted_objects = dict(sorted(objects.items(), key=lambda x: (-len(x[1]), x[0])))
    for obj_type, objs in sorted_objects.items():
        result += f"{obj_type}:\n"
        for obj in sorted(objs):
            result += f"-{obj}\n"
    return result

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))