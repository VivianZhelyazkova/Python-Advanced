def rectangle(length, width):
    if not type(length) is int or not isinstance(width, int):
        return "Enter valid values!"

    def area():
        return width * length

    def perimeter():
        return 2 * width + 2 * length

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"


print(rectangle(2, 10))
