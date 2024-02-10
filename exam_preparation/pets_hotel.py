def accommodate_new_pets(capacity: int, weight: float, *args):
    pets = {}
    result = ""

    for pet_type, pet_weight in args:

        if not capacity:
            result += "You did not manage to accommodate all pets!\n"
            break
        if pet_weight <= weight:
            capacity -= 1
            if pet_type not in pets:
                pets[pet_type] = 1
            else:
                pets[pet_type] += 1
    else:
        result += f"All pets are accommodated! Available capacity: {capacity}.\n"

    result += "Accommodated pets:\n"
    for pet, count in sorted(pets.items()):
        result += f"{pet}: {count}\n"

    return result.rstrip()

