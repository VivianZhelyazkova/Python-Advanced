set_1 = set(int(x) for x in input().split())
set_2 = set(int(x) for x in input().split())

number = int(input())


for _ in range(number):
    command = input()
    if "Check" in command:


    cmd1, cmd2, numbers = command.split()
    numbers_list = (int(x) for x in numbers.split())

    if cmd1 == "Add":

        if cmd2 == "First":
            set_1.union(numbers_list)
        elif cmd2 == "Second":
            set_2.union(numbers_list)

    elif cmd1 == "Remove":

        if cmd2 == "First":
            set_1.difference_update(numbers_list)
        elif cmd2 == "Second":
            set_2 - set(numbers_list)
