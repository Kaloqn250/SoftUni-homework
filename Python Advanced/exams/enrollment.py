def gather_credits(needed_credits, *args):
    courses = []
    gathered_credits = 0
    result = ''

    for course, credits in args:
        if gathered_credits >= needed_credits:
            break

        if course not in courses:
            gathered_credits += credits
            courses.append(course)

    if gathered_credits >= needed_credits:
        result += f'Enrollment finished! Maximum credits: {gathered_credits}.\n'
    else:
        result += f'You need to enroll in more courses! You have to gather {needed_credits - gathered_credits} credits more.'
        return result

    sorted_courses = sorted(courses)

    result += f'Courses: {", ".join(sorted_courses)}'
    return result


print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

