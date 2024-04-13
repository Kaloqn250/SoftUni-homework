from my_projects.register_students.schools.base_school import BaseSchool


class University(BaseSchool):

    def get_school_info(self, students):
        result = f"This is University and the students are:\n"
        result += "\n".join([f'{s.name} {s.surname}: {s.student_id} with courses: {s.get_courses()}'
                             for s in students if s.__class__.__name__ == 'UniversityStudent'])

        return result
