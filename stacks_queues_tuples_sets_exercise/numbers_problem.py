set_1 = set(int(x) for x in input().split())
set_2 = set(int(x) for x in input().split())

number = int(input())

for _ in range(number):

    command = input()

    if "Check" in command:
        print(set_1.issubset(set_2) or set_2.issubset(set_1))
        continue

    cmd_split = command.split()
    cmd_1 = cmd_split[0]
    cmd_2 = cmd_split[1]
    numbers = cmd_split[2:]

    numbers_list = list(int(x) for x in numbers)

    if cmd_1 == "Add":

        if cmd_2 == "First":
            set_1 = set_1.union(numbers_list)
        elif cmd_2 == "Second":
            set_2 = set_2.union(numbers_list)

    elif cmd_1 == "Remove":

        if cmd_2 == "First":
            set_1 = set_1 - set(numbers_list)
        elif cmd_2 == "Second":
            set_2 = set_2 - set(numbers_list)

sorted_1 = sorted(set_1)
sorted_2 = sorted(set_2)

print(*sorted_1, sep=", ")
print(*sorted_2, sep=", ")
