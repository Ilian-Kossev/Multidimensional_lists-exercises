def func_executor(*args):
    result_list = []
    for item in args:
        func, tupple = item
        result = func(*tupple)
        result_list.append(result)
    return result_list


def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))