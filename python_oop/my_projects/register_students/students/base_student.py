from abc import ABC


class BaseStudent(ABC):

    def __init__(self, name, surname, student_id):
        self.name = name
        self.surname = surname
        self.student_id = student_id

    def __str__(self):
        return (f"This is {self.name} {self.surname} and it's a {self.__class__.__name__} "
                f"with Student ID: {self.student_id}")
