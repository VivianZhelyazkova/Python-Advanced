number = int(input())
stack = []
for i in range(number):
    command = input()
    cmd_numer = command.split()[0]
    if cmd_numer == "1":
        number_to_push = int(command.split()[1])
        stack.append(number_to_push)
    elif cmd_numer == "2":
        stack.pop()
    elif cmd_numer == "3":
        print(max(stack))
    elif cmd_numer == "4":
        print(min(stack))

for number in range(len(stack)):
    print(stack.pop(), end=" ")
