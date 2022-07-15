from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

gifts_dict = dict()
gemstone_and_sculpture_crafted = False
gold_and_jewellery_crafted = False
present_to_add = ''
while materials and magic_level:
    material = materials.pop()
    magic = magic_level.popleft()
    result = magic + material
    if result < 100 and result % 2 == 0:
        result = 2 * material + 3 * magic
    elif result < 100 and result % 2 == 1:
        result *= 2
    elif result > 499:
        result /= 2

    if result <= 100 or result > 500:
        continue
    elif 100 <= result < 200:
        present_to_add = 'Gemstone'
    elif 200 <= result < 300:
        present_to_add = 'Porcelain Sculpture'
    elif 300 <= result < 400:
        present_to_add = 'Gold'
    elif 400 <= result < 500:
        present_to_add = 'Diamond Jewellery'

    if present_to_add not in gifts_dict:
        gifts_dict[present_to_add] = 0
    gifts_dict[present_to_add] += 1

    if 'Gemstone' in gifts_dict and 'Porcelain Sculpture' in gifts_dict:
        gemstone_and_sculpture_crafted = True

    if 'Gold' in gifts_dict and 'Diamond Jewellery' in gifts_dict:
        gold_and_jewellery_crafted = True

if gemstone_and_sculpture_crafted or gold_and_jewellery_crafted:
    print("The wedding presents are made!")
if not gemstone_and_sculpture_crafted and not gold_and_jewellery_crafted:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")
sorted_dict = dict(sorted(gifts_dict.items(), key=lambda x: x[0]))
for key, value in sorted_dict.items():
    print(f'{key}: {value}')
# judge: 91/100





