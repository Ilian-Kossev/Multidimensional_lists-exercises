from collections import deque


def best_list_pureness(numbers_list, number):
    deque_list = deque(numbers_list)
    pureness_dict = {}
    for num in range(number):
        pureness = 0
        for numb in range(len(deque_list)):
            pureness += deque_list[numb] * numb
        if pureness not in pureness_dict:
            pureness_dict[pureness] = num
        deque_list.rotate()
    max_pureness, rotations_num = max(pureness_dict.items())
    return f'Best pureness {max_pureness} after {rotations_num} rotations'


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)

