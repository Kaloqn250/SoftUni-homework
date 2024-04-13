from my_projects.register_students.students.base_student import BaseStudent


class SchoolStudent(BaseStudent):

    def __init__(self, name, surname, student_id):
        super().__init__(name, surname, student_id)
        self._class = ''
