from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.secondary_service import SecondaryService
from project.services.main_service import MainService


class RobotsManagingApp:
    ROBOTS_TYPES = {"FemaleRobot": FemaleRobot, "MaleRobot": MaleRobot}
    SERVICES_TYPES = {"MainService": MainService, "SecondaryService": SecondaryService}

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type, name):
        if service_type not in self.SERVICES_TYPES:
            raise Exception("Invalid service type!")

        new_service = self.SERVICES_TYPES[service_type](name)
        self.services.append(new_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type, name, kind, price):
        if robot_type not in self.ROBOTS_TYPES:
            raise Exception("Invalid robot type!")

        new_robot = self.ROBOTS_TYPES[robot_type](name, kind, price)
        self.robots.append(new_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name, service_name):
        robot = self._get_robot(robot_name)
        service = self._get_service(service_name)

        if not (
                (service.__class__.__name__ == 'SecondaryService' and robot.__class__.__name__ == 'FemaleRobot') or
                (service.__class__.__name__ == 'MainService' and robot.__class__.__name__ == 'MaleRobot')
        ):
            return "Unsuitable service."

        if not service.capacity > len(service.robots):
            raise Exception("Not enough capacity for this robot!")

        service.robots.append(robot)
        self.robots.remove(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name, service_name):
        service = self._get_service(service_name)
        service_robots_names = [r.name for r in service.robots]

        if robot_name not in service_robots_names:
            raise Exception("No such robot in this service!")

        robot = [r for r in service.robots if r.name == robot_name][0]
        service.robots.remove(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name):
        service = self._get_service(service_name)
        counter = 0

        for robot in service.robots:
            robot.eating()
            counter += 1

        return f"Robots fed: {counter}."

    def service_price(self, service_name):
        service = self._get_service(service_name)
        total_service_price = sum([r.price for r in service.robots])

        return f"The value of service {service_name} is {total_service_price:.2f}."

    def __str__(self):
        result = ''
        for service in self.services:
            result += f'{service.details()}'

        return result.strip()

    def _get_robot(self, robot_name):
        robot = [r for r in self.robots if r.name == robot_name]
        return robot[0] if robot else None

    def _get_service(self, service_name):
        service = [s for s in self.services if s.name == service_name]
        return service[0] if service else None
