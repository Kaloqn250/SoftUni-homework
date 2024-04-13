from project.player import Player


class Guild:

    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):

        if player.guild != "Unaffiliated":
            if player.guild == self.name:
                return f"Player {player.name} is already in the guild."

            return f"Player {player.name} is in another guild."

        player.guild = self.name
        self.players.append(player)
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        try:
            player = next(filter(lambda x: x.name == player_name, self.players))
        except StopIteration:
            return f"Player {player_name} is not in the guild."

        player.guild = "Unaffiliated"
        self.players.remove(player)
        return f"Player {player.name} has been removed from the guild."

    def guild_info(self):
        players_info = '\n'.join(f'{p.player_info()}' for p in self.players)

        return (f"Guild: {self.name}\n"
                f"{players_info}")
