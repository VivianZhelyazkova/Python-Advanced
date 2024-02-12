def add_songs(*args):
    songs = {}
    result = ""
    for name, text in args:
        if name not in songs:
            songs[name] = text
        else:
            
            songs[name].append(text)
    for song, lyrics in songs.items():
        result += f"-{song}\n"
        if len(lyrics) > 0:
            for line in lyrics:
                result += f"{line}\n"
    return result


print(add_songs(
    ("Beat It", []),
    ("Beat It",
     ["Just beat it (beat it), beat it (beat it)",
      "No one wants to be defeated"]),
    ("Beat It", []),
    ("Beat It",
     ["Showin' how funky and strong is your fight",
      "It doesn't matter who's wrong or right"]),
))