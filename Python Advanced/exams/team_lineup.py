def team_lineup(*args):
    dictionary = {}
    for name, country in args:
        if country not in dictionary.keys():
            dictionary[country] = []
        dictionary[country].append(name)

    sorted_dict = sorted(dictionary.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ''
    for country, players in sorted_dict:
        result += f'{country}:\n'
        for player in players:
            result += f'  -{player}\n'

    return result


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))
