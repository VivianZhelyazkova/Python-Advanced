def team_lineup(*args):
    result = {}

    for player, country in args:
        if country not in result:
            result[country] = [player]
        else:
            result[country].append(player)

    sorted_result = dict(sorted(result.items(), key=lambda x: (-len(x[1]), x[0])))
    result_as_string = ""

    for country, players in sorted_result.items():
        result_as_string += f"{country}:\n"
        for player in players:
            result_as_string += f"  -{player}\n"
    return result_as_string.rstrip()

