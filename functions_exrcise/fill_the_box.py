def fill_the_box(height, length, width, *args):
    box_volume = height * length * width
    current_volume = box_volume
    numbers = args[:args.index("Finish")]
    total_cubes = sum(numbers)

    for index, cube in enumerate(numbers):

        if current_volume > cube:
            current_volume -= cube
        else:
            if current_volume > 0:
                return f"No more free space! You have {total_cubes - box_volume} more cubes."

    return f"There is free space in the box. You could put {box_volume - total_cubes} more cubes."

