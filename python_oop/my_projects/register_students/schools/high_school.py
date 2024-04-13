from my_projects.register_students.schools.base_school import BaseSchool


class HighSchool(BaseSchool):

    def get_school_info(self, students):
        result = f"This is HighSchool and the students are:\n"
        result += "\n".join([f'{s.name} {s.surname}: {s.student_id}' for s in students if s.__class__.__name__ == 'SchoolStudent'])

        return result



