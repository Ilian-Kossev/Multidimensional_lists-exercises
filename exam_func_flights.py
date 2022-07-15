def flights(*args):
    cat_destinations = {}
    for num in range(len(args)):
        if args[num] == 'Finish':
            return cat_destinations
        if num % 2 == 0:
            if args[num] not in cat_destinations:
                cat_destinations[args[num]] = args[num + 1]
            else:
                cat_destinations[args[num]] += args[num + 1]


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))

