from my_projects.register_students.schools.base_school import BaseSchool
from my_projects.register_students.schools.high_school import HighSchool
from my_projects.register_students.schools.univesity import University
from my_projects.register_students.students.school_student import SchoolStudent
from my_projects.register_students.students.university_student import UniversityStudent


class Register:
    VALID_STUDENT = {"UniversityStudent": UniversityStudent, "SchoolStudent": SchoolStudent}
    VALID_SCHOOL = {"University": University, "HighSchool": HighSchool}

    def __init__(self):
        self.registered_students = []
        self.schools = {}

    def register_student(self, student_type, school_type, name, surname, student_id):

        if student_type not in self.VALID_STUDENT:
            return f"That student type {student_type} is not valid!"

        if school_type not in self.VALID_SCHOOL:
            return "Student can't be registered in not valid school type!"

        if not ((student_type == "UniversityStudent" and school_type == "University") or (
                student_type == "SchoolStudent" and school_type == "HighSchool")):
            return f"This {student_type} can't study in {school_type}!"

        student = self._get_student(student_id)

        if student is not None:
            return f"There is already student in {school_type} with this ID"

        new_student = self.VALID_STUDENT[student_type](name, surname, student_id)
        school = self.VALID_SCHOOL[school_type]
        self.registered_students.append(new_student)

        if school not in self.schools.keys():
            self.schools[school] = []
        self.schools[school].append(new_student)
        return f"{str(new_student)} has been registered"

    def add_courses(self, student_id, courses):
        student = self._get_student(student_id)

        if student is None:
            return f"There isn't a student with this ID"

        if student.__class__.__name__ != 'UniversityStudent':
            return "HighSchool student can't have courses"

        student.courses.append(courses)
        return f'{student.name} has joined {", ".join(courses)}; courses'

    def add_class(self, student_id, _class):
        student = self._get_student(student_id)

        if student is None:
            return f"There isn't a student with this ID"

        if student.__class__.__name__ != 'SchoolStudent':
            return "University student can't have class"

        if student._class == _class:
            return f'{student.name} is already in "{_class}" class'

        student._class = _class
        return f'{student.name} has joined "{_class}" class'

    def change_courses(self, student_id, old_course, new_course):
        student = self._get_student(student_id)

        if student is None:
            return f"There isn't a student with this ID"

        if student.__class__.__name__ != 'UniversityStudent':
            return f"School student doesn't have a courses"

        if old_course not in student.courses:
            return "Can't change a not existing course"

        if old_course == new_course:
            return "Can't change a new course with the same old course"

        student.courses.remove(old_course)
        student.courses.append(new_course)
        return f"{student.name} {student.surname} changed from {old_course} to {new_course}"

    def change_classes(self, student_id, old_class, new_class):
        student = self._get_student(student_id)

        if student is None:
            return f"There isn't a student with this ID"

        if student.__class__.__name__ != 'SchoolStudent':
            return f"University student doesn't have a class"

        if student._class != old_class:
            return f"{student.name} is not from this class"

        if old_class == new_class:
            return f"{student.name} is already in this class"

        student._class = new_class
        return f'{student.name} {student.surname} changed class'

    def eject_student(self, student_id):
        student = self._get_student(student_id)

        if student is None:
            return f"There isn't a student with this ID"

        self.registered_students.remove(student)
        return f'{student.name} {student.surname} was ejected'

    def get_info(self, school_type):
        school = self.VALID_SCHOOL[school_type]()
        return school.get_school_info(self.registered_students)

    def _get_student(self, student_id):
        student = [s for s in self.registered_students if s.student_id == student_id]
        return student[0] if student else None
