number = int(input())

students = {}

for _ in range(number):
    name, grade = input().split()
    if name not in students:
        students[name] = [float(grade)]
    else:
        students[name].append(float(grade))

for student, grades in students.items():
    average = sum(grades) / len(grades)
    str_grades = [f"{grade:.2f}" for grade in grades]
    joined_grades = ' '.join(str_grades)
    print(f"{student} -> {joined_grades} (avg: {average:.2f})")
