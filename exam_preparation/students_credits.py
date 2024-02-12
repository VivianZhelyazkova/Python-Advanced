def students_credits(*args):
    diyans_credits = {}
    diploma = 240
    result = ""
    for info in args:
        course, credits, max_points, diyans_points = info.split("-")
        percent_achieved = int(diyans_points) / int(max_points)
        credits_earned = int(credits) * percent_achieved
        diyans_credits[course] = credits_earned

    total_credits = sum(diyans_credits.values())
    if total_credits >= diploma:
        result += f"Diyan gets a diploma with {total_credits: .1f} credits.\n"
    else:
        result += f"Diyan needs {diploma - total_credits: .1f} credits more for a diploma.\n"

    sorted_credits = dict(sorted(diyans_credits.items(), key=lambda x: -x[1]))
    for course_name, diyans_credits in sorted_credits.items():
        result += f"{course_name} - {diyans_credits: .1f}\n"
    return result
