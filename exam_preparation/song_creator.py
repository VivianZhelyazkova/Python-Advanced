def add_songs(*args):
    songs = {}
    result = ""
    for name, text in args:
        if name not in songs:
            songs[name] = text
        else:
            songs[name].extend(text)

    for song, lyrics in songs.items():
        result += f"- {song}\n"
        for line in lyrics:
            result += f"{line}\n"
    return result

