def gather_credits(credits_needed: int, *courses):
    result = []
    credits_gathered = 0

    for course, credit in courses:
        if credits_gathered >= credits_needed:
            break
        if course not in result:
            result.append(course)
            credits_gathered += credit
    if credits_gathered >= credits_needed:
        return f"Enrollment finished! Maximum credits: {credits_gathered}.\nCourses: {', '.join(sorted(result))}"
    else:
        return f"You need to enroll in more courses! You have to gather {credits_needed - credits_gathered} credits more."

