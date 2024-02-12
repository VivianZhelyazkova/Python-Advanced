def forecast(*args):
    result = ""
    forecast = {
        "Sunny": [],
        "Cloudy": [],
        "Rainy": []
    }
    for location, weather in args:
        forecast[weather].append(location)

    for weather, locations in forecast.items():
        for location in sorted(locations):
            result += f"{location} - {weather}\n"
    return result

