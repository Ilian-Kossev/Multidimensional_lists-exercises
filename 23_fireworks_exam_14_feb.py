from collections import deque


fireworks_effect = deque([int(x) for x in input().split(', ')])
explosive_power = [int(x) for x in input().split(', ')]

palm_counter = 0
willow_counter = 0
crossette_counter = 0
enough_fireworks_made = False

while fireworks_effect and explosive_power and not enough_fireworks_made:
    firework = fireworks_effect.popleft()
    if firework <= 0:
        continue
    explosive = explosive_power.pop()
    if explosive <= 0:
        fireworks_effect.appendleft(firework)
        continue
    result = firework + explosive
    if result % 3 == 0 and not result % 5 == 0:
        palm_counter += 1
    elif not result % 3 == 0 and result % 5 == 0:
        willow_counter += 1
    elif result % 3 == 0 and result % 5 == 0:
        crossette_counter += 1
    else:
        firework -= 1
        fireworks_effect.append(firework)
        explosive_power.append(explosive)

    if palm_counter >= 3 and willow_counter >= 3 and crossette_counter >= 3:
        enough_fireworks_made = True


if not enough_fireworks_made:
    print("Sorry. You can't make the perfect firework show.")
else:
    print("Congrats! You made the perfect firework show!")
if len(fireworks_effect) > 0:
    print(f"Firework Effects left: {', '.join(str(x) for x in fireworks_effect)}")
if len(explosive_power) > 0:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}")
print(f'Palm Fireworks: {palm_counter}')
print(f'Willow Fireworks: {willow_counter}')
print(f'Crossette Fireworks: {crossette_counter}')







