from abc import ABC, abstractmethod


class BaseSchool(ABC):

    @abstractmethod
    def get_school_info(self, students):
        ...
