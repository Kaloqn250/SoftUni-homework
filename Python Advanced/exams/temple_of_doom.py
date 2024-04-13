from collections import deque

tools = deque([int(el) for el in input().split()])
substances = [int(el) for el in input().split()]
challenges = [int(el) for el in input().split()]

while True:

    if not challenges:
        print(f'Harry found an ostracon, which is dated to the 6th century BCE.')
        break

    elif not (tools and substances):
        print(f'Harry is lost in the temple. Oblivion awaits him.')
        break

    current_tool = tools.popleft()
    current_substance = substances.pop()

    result = current_tool * current_substance

    for challenge in challenges:
        if result == challenge:
            challenges.remove(challenge)
            break
    else:
        tools.append(current_tool + 1)
        current_substance -= 1
        if not current_substance <= 0:
            substances.append(current_substance)

if tools:
    print(f'Tools: {", ".join([str(el) for el in tools])}')

if substances:
    print(f'Substances: {", ".join([str(el) for el in substances])}')

if challenges:
    print(f'Challenges: {", ".join([str(el) for el in challenges])}')


