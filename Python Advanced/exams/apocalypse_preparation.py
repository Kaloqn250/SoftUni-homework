from collections import deque

textiles = deque([int(el) for el in input().split()])
medications = [int(el) for el in input().split()]

items = {
    30: 'Patch',
    40: 'Bandage',
    100: 'MedKit',
}
collected_items = {}

while textiles and medications:
    textile = textiles.popleft()
    medication = medications.pop()

    result = textile + medication

    if items.get(result):
        item = items.get(result)
        if item not in collected_items.keys():
            collected_items[item] = 0
        collected_items[item] += 1

    elif result > 100:
        collected_items['MedKit'] += 1
        result -= 100
        current_med = medications.pop()
        medications.append(current_med + result)
    else:
        medications.append(medication + 10)

if not medications and not textiles:
    print("Textiles and medicaments are both empty.")

elif not medications:
    print("Medicaments are empty.")

elif not textiles:
    print("Textiles are empty.")

sorted_dictionary = sorted(collected_items.items(), key=lambda x: (-x[1], x[0]))

for key, value in sorted_dictionary:
    print(f'{key} - {value}')

if medications:
    print(f"Medicaments left: {', '.join([str(el) for el in reversed(medications)])}")

if textiles:
    print(f"Textiles left: {', '.join([str(el) for el in textiles])}")
