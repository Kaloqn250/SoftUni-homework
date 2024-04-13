from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.predatory_fish import PredatoryFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.divers.base_diver import BaseDiver


class NauticalCatchChallengeApp:
    DIVER_TYPES = {'FreeDiver': FreeDiver, 'ScubaDiver': ScubaDiver}
    FISH_TYPES = {'PredatoryFish': PredatoryFish, 'DeepSeaFish': DeepSeaFish}

    def __init__(self):
        self.divers = []
        self.fish_list = []

    def dive_into_competition(self, diver_type, diver_name):
        if diver_type not in self.DIVER_TYPES:
            return f"{diver_type} is not allowed in our competition."

        check_for_diver = self._get_diver(diver_name)
        if check_for_diver is not None:
            return f"{diver_name} is already a participant."

        new_diver_type = self.DIVER_TYPES.get(diver_type)
        new_diver = new_diver_type(diver_name)
        self.divers.append(new_diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type, fish_name, points):
        if fish_type not in self.FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."

        check_for_fish = self._get_fish(fish_name)
        if check_for_fish is not None:
            return f"{fish_name} is already permitted."

        new_fish = self.FISH_TYPES[fish_type](fish_name, points)
        self.fish_list.append(new_fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name, fish_name, is_lucky):
        diver = self._get_diver(diver_name)
        if diver is None:
            return f"{diver_name} is not registered for the competition."

        fish = self._get_fish(fish_name)
        if fish is None:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.oxygen_level <= 0:
            diver.has_health_issue = True

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.oxygen_level = 0
            diver.has_health_issue = True
            return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                if diver.oxygen_level == 0:
                    diver.has_health_issue = True
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            diver.has_health_issue = True
            return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        counter = 0

        for diver in self.divers:
            if diver.has_health_issue:
                counter += 1
                diver.update_health_status()
                diver.renew_oxy()

        return f"Divers recovered: {counter}"

    def diver_catch_report(self, diver_name):
        diver = self._get_diver(diver_name)
        result = f"**{diver_name} Catch Report**\n"
        result += '\n'.join([f.fish_details() for f in diver.catch])

        return result

    def competition_statistics(self):
        good_health_divers = [d for d in self.divers if not d.has_health_issue]
        sorted_divers = sorted(
            good_health_divers,
            key=lambda d: (-d.competition_points, -len(d.catch), d.name)
        )
        result = "**Nautical Catch Challenge Statistics**\n"
        result += "\n".join(str(d) for d in sorted_divers)

        return result

    def _get_diver(self, diver_name: str):
        diver = [d for d in self.divers if d.name == diver_name]
        return diver[0] if diver else None

    def _get_fish(self, fish_name: str):
        fish = [f for f in self.fish_list if f.name == fish_name]
        return fish[0] if fish else None