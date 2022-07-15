def even_odd(*args):
    list_string = [str(x) for x in args]
    list_nums = [int(x) for x in list_string if x.isnumeric()]
    if 'even' in args:
        list_even = [x for x in list_nums if x % 2 == 0]
        return list_even
    elif 'odd' in args:
        list_odd = [x for x in list_nums if x % 2 == 1]
        return list_odd


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

