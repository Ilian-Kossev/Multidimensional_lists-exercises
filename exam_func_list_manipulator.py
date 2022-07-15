from collections import deque


def list_manipulator(numbers_list, *args):
    list_numbers = deque(numbers_list)
    param_1, param_2, *rest = args
    if param_1 == 'add':
        if param_2 == 'beginning':
            for item in rest[::-1]:
                list_numbers.appendleft(item)
        else:
            for item in rest:
                list_numbers.append(item)
    else:
        if param_2 == 'beginning':
            if rest:
                for _ in range(rest[0]):
                    list_numbers.popleft()
            else:
                list_numbers.popleft()
        else:
            if rest:
                for _ in range(rest[0]):
                    list_numbers.pop()
            else:
                list_numbers.pop()
    result = [x for x in list_numbers]
    return result


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))


