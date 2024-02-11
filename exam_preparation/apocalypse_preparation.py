from collections import deque

textiles = deque([int(x) for x in input().split()])
medicaments = deque([int(x) for x in input().split()])

items = {
    30: "Patch",
    40: "Bandage",
    100: "MedKit"
}

created_items = {
    "Patch": 0,
    "Bandage": 0,
    "MedKit": 0
}

while True:
    if not textiles and not medicaments:
        print("Textiles and medicaments are both empty.")
        break
    elif not textiles:
        print("Textiles are empty.")
        break
    elif not medicaments:
        print("Medicaments are empty.")
        break
    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()
    result = current_medicament + current_textile

    if result in items:
        created_item = items[result]
        created_items[created_item] += 1
    elif result > 100:
        created_items["MedKit"] += 1
        resources_left = result - 100
        medicaments[-1] += resources_left
    else:
        current_medicament += 10
        medicaments.append(current_medicament)

sorted_items = dict(sorted(created_items.items(), key=lambda x: (-x[1], x[0])))
for item, count in sorted_items.items():
    if count:
        print(f"{item} - {count}")

if medicaments:
    print(f"Medicaments left: {', '.join(str(x) for x in reversed(medicaments))}")
if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")

