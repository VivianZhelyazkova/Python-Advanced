def softuni_students(*args, **kwargs):
    students = {}
    invalid_students = []
    result = ""

    for student_id, username in args:
        if student_id not in kwargs:
            invalid_students.append(username)
        else:
            students[username] = kwargs[student_id]

    sorted_students = dict(sorted(students.items(), key=lambda x: x[0]))

    for user, course in sorted_students.items():
        result += f"*** A student with the username {user} has successfully finished the course {course}!\n"

    if invalid_students:
        result += f"!!! Invalid course students: {', '.join(sorted(invalid_students))}"

    return result.rstrip()

