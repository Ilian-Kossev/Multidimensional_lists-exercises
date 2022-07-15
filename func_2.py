def process_odd(nums):
    odd_nums = [x for x in nums if x % 2 == 1]
    sum_odd = sum(odd_nums)
    result = sum_odd * len(nums)
    return result


def process_even(nums):
    even_nums = [x for x in nums if x % 2 == 0]
    sum_even = sum(even_nums)
    result = sum_even * len(nums)
    return result


command = input()
numbers = [int(x) for x in input().split()]

if command == 'Odd':
    print(process_odd(numbers))
else:
    print(process_even(numbers))
