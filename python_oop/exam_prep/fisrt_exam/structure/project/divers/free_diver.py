from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):

    def __init__(self, name):
        super().__init__(name, 120)

    def miss(self, time_to_catch):
        if self.oxygen_level - time_to_catch * 0.6 > 0:

            self.oxygen_level = round(self.oxygen_level - time_to_catch * 0.6)

        else:
            self.oxygen_level = 0

    def renew_oxy(self):
        self.oxygen_level = 120

