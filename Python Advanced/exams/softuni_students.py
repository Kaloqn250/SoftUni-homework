def softuni_students(*students, **courses):
    result = []
    course_students = {}
    invalid_students = set()
    courses_ids = [id for id in courses.keys()]

    for student_id, name in students:
        if student_id in courses_ids:
            if courses[student_id] not in course_students.keys():
                course_students[courses[student_id]] = []
            course_students[courses[student_id]].append(name)
        else:
            invalid_students.add(name)

    sorted_students = sorted(course_students.items(), key=lambda x: x[1])

    for course, usernames in sorted_students:
        for username in sorted(usernames):
            result.append(f'*** A student with the username {username} has successfully finished the course {course}!')
    if invalid_students:
        result.append(f'!!! Invalid course students: {", ".join(sorted(invalid_students))}')

    return '\n'.join(result)


print(softuni_students(
    ('id_2', 'Alice'),
    ('id_1', 'John'),
    id_1='Course 1',
    id_2='Course 2',
))
