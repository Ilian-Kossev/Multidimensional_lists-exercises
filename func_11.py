def fill_the_box(*args):
    height, width, length, *rest = args
    volume = height * width * length
    index = 0
    while rest:
        volume_to_add = rest[index]
        rest.remove(volume_to_add)
        index -= 1
        if volume_to_add == 'Finish':
            break
        free_volume = volume - volume_to_add
        if free_volume >= 0:
            volume -= volume_to_add
        else:
            extra_volume = volume_to_add - volume
            rest.append(extra_volume)
            list_left_cubes_str = [str(x) for x in rest]
            list_left_cubes_int = [int(x) for x in list_left_cubes_str if x.isdigit()]
            sum_cubes = sum(list_left_cubes_int)
            return f'No more free space! You have {sum_cubes} more cubes.'
        index += 1
    return f'There is free space in the box. You could put {volume} more cubes.'


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
