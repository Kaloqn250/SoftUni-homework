from collections import deque

worms = [int(w) for w in input().split()]
holes = deque(int(h) for h in input().split())

matches_count = 0
worms_count = len(worms)

while worms and holes:
    worm = worms.pop()
    hole = holes.popleft()

    if worm == hole:
        matches_count += 1
    else:
        worm -= 3
        if not worm <= 0:
            worms.append(worm)


print(f'Matches: {matches_count}' if matches_count else 'There are no matches.')

if worms_count == matches_count:
    print("Every worm found a suitable hole!")
else:
    print(f'Worms left: {", ".join([str(w) for w in worms])}' if worms else 'Worms left: none')

print(f'Holes left: {", ".join([str(h) for h in holes])}' if holes else 'Holes left: none')

