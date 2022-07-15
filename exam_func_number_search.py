from collections import deque


def numbers_searching(*args):
    result = []
    duplicate_list = []
    numbers_list = deque(args)
    elements_number = len(numbers_list)
    for num in range(elements_number):
        x = numbers_list.popleft()
        if x not in numbers_list:
            numbers_list.append(x)
        else:
            if x not in duplicate_list:
                duplicate_list.append(x)

    min_value = min(numbers_list)
    digits_number = len(numbers_list)
    max_value = min_value + digits_number
    for num in range(min_value, max_value + 1):
        if num not in numbers_list:
            missing_num = num
            result.append(missing_num)
            result.append(sorted(duplicate_list))
    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))








