from project.services.base_service import BaseService


class SecondaryService(BaseService):

    def __init__(self, name):
        super().__init__(name, 15)

    def details(self):
        result = f"{self.name} Secondary Service:\n"
        result += 'Robots: '
        if self.robots:
            result += ' '.join([f'{r.name}' for r in self.robots])

        else:
            result += 'none'

        result += '\n'
        return result
