quantity = int(input())
days = int(input())

ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15

total_budget = 0
total_spirit = 0

for current_day in range(1, days + 1):
    if current_day % 11 == 0:
        quantity += 2
    if current_day % 2 == 0:
        total_budget += quantity * ornament_set
        total_spirit += 5
    if current_day % 3 == 0:
        total_budget += quantity * (tree_skirt + tree_garland)
        total_spirit += 13
    if current_day % 5 == 0:
        total_budget += quantity * tree_lights
        total_spirit += 17
        if current_day % 3 == 0:
            total_spirit += 30
    if current_day % 10 == 0:
        total_spirit -= 20
        total_budget += tree_lights + tree_skirt + tree_garland

if days % 10 == 0:
    total_spirit -= 30

print(f'Total cost: {total_budget}')
print(f'Total spirit: {total_spirit}')
