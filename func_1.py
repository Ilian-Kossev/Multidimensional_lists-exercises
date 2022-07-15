data = input().split()


def add_positives(nums):
    sum_positives = 0
    for n in nums:
        number = int(n)
        if number > 0:
            sum_positives += number
    return sum_positives


def add_negatives(nums):
    sum_negatives = 0
    for n in nums:
        number = int(n)
        if number < 0:
            sum_negatives += number

    return sum_negatives


print(add_negatives(data))
print(add_positives(data))
if add_positives(data) > abs(add_negatives(data)):
    print('The positives are stronger than the negatives')
elif add_positives(data) < abs(add_negatives(data)):
    print('The negatives are stronger than the positives')




