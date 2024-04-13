from my_projects.register_students.students.base_student import BaseStudent


class UniversityStudent(BaseStudent):

    def __init__(self, name, surname, student_id):
        super().__init__(name, surname, student_id)
        self.courses = []

    def get_courses(self):
        courses = ', '.join([c for c in self.courses])
        return courses
