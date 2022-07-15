from collections import deque
import sys
from io import StringIO


test_input_1 = '1333'

sys.stdin = StringIO(test_input_1)


def are_fireworks_enough(fireworks):
    # return fireworks['palm'] >= 3\
    #       and fireworks['willow'] >= 3\
    #       and fireworks['crossette'] >= 3
    return all(x >= 3 for x in fireworks.values())


def mix_fireworks(firework_effects, explosive_powers):
    firework_effects_queue = deque([x for x in firework_effects if x > 0])
    explosive_powers_stack = [x for x in explosive_powers if x > 0]

    fireworks = {
        'palm': 0,
        'willow': 0,
        'crossette': 0,
    }

    while firework_effects_queue \
            and explosive_powers_stack\
            and not are_fireworks_enough(fireworks):
        firework_effect = firework_effects_queue.popleft()
        explosive_power = explosive_powers_stack.pop()

        current_sum = firework_effect + explosive_power
        if current_sum % 3 == 0 and current_sum % 5 == 0:
            fireworks['crossette'] += 1
        elif current_sum % 3 == 0:
            fireworks['palm'] += 1
        elif current_sum % 5 == 0:
            fireworks['willow'] += 1
        else:
            firework_effects_queue.append(firework_effect - 1)
            explosive_powers_stack.append(explosive_power)
    return fireworks, firework_effects_queue, explosive_powers_stack

fe = [5, 6, 4, 16, 11, 5, 30, 2, 3, 27]
ep = [1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22]