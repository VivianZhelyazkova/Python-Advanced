def movie_organizer(*args):
    collection = {}
    result = ""
    for movie, genre in args:
        if genre not in collection:
            collection[genre] = [movie]
        else:
            collection[genre].append(movie)
    sorted_collection = dict(sorted(collection.items(), key=lambda x: (-len(x[1]), x[0])))

    for genre, movies in sorted_collection.items():
        result += f"{genre} - {len(movies)}\n"
        for movie in sorted(movies):
            result += f"* {movie}\n"
    return result


