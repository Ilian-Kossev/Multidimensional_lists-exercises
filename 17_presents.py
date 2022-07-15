def move_santa_up(index_r, index_c, collection):
    counter_presents = 0
    if index_r > 0:
        collection[index_r][index_c] = '-'
        index_r -= 1
        collection[index_r][index_c] = 'S'
        return index_r, index_c, collection


def move_santa_down(index_r, index_c, collection):
    if index_r < len(collection) - 1:
        collection[index_r][index_c] = '-'
        index_r += 1
        collection[index_r][index_c] = 'S'
        return index_r, index_c, collection


def move_santa_right(index_r, index_c, collection):
    if index_c < len(collection) - 1:
        collection[index_r][index_c] = '-'
        index_c += 1
        collection[index_r][index_c] = 'S'
        return index_r, index_c, collection


def move_santa_left(index_r, index_c, collection):
    if index_c > 0:
        collection[index_r][index_c] = '-'
        index_c -= 1
        collection[index_r][index_c] = 'S'
        return index_r, index_c, collection


def santa_eats_cookie(index_r, index_c, collection):
    indexes_with_presents = list()
    temp_list_1 = list()
    temp_list_1.append(index_r + 1)
    temp_list_1.append(index_c)
    indexes_with_presents.append(temp_list_1)
    collection[index_r + 1][index_c] = '-'
    temp_list_2 = list()
    temp_list_2.append(index_r - 1)
    temp_list_2.append(index_c)
    indexes_with_presents.append(temp_list_2)
    collection[index_r - 1][index_c] = '-'
    temp_list_3 = list()
    temp_list_3.append(index_r)
    temp_list_3.append(index_c + 1)
    indexes_with_presents.append(temp_list_3)
    collection[index_r][index_c + 1] = '-'
    temp_list_4 = list()
    temp_list_4.append(index_r)
    temp_list_4.append(index_c - 1)
    indexes_with_presents.append(temp_list_4)
    collection[index_r][index_c - 1] = '-'
    return indexes_with_presents, collection


presents_number = int(input())
matrix_range = int(input())
matrix = []
for _ in range(matrix_range):
    line = input().split()
    matrix.append(line)

index_santa_r = 0
index_santa_c = 0
list_coordinates_nice_kids = []
list_coordinates_naughty_kids = []
list_coordinates_cookies = []
for r in range(matrix_range):
    for c in range(matrix_range):
        if matrix[r][c] == 'S':
            index_santa_r = r
            index_santa_c = c
        if matrix[r][c] == 'V':
            coordinates_kids = list()
            coordinates_kids.append(r)
            coordinates_kids.append(c)
            list_coordinates_nice_kids.append(coordinates_kids)
        if matrix[r][c] == 'X':
            coordinates_kids = list()
            coordinates_kids.append(r)
            coordinates_kids.append(c)
            list_coordinates_naughty_kids.append(coordinates_kids)
        if matrix[r][c] == 'C':
            coordinates_cookies = list()
            coordinates_cookies.append(r)
            coordinates_cookies.append(c)
            list_coordinates_cookies.append(coordinates_cookies)


counter_present_to_nice_kids = 0
santa_out_of_presents = False
command = input()
while not command == 'Christmas morning':
    if command == 'up':
        index_santa_r, index_santa_c, matrix = move_santa_up(index_santa_r, index_santa_c, matrix)
    elif command == 'down':
        index_santa_r, index_santa_c, matrix = move_santa_down(index_santa_r, index_santa_c, matrix)
    elif command == 'left':
        index_santa_r, index_santa_c, matrix = move_santa_left(index_santa_r, index_santa_c, matrix)
    elif command == 'right':
        index_santa_r, index_santa_c, matrix = move_santa_right(index_santa_r, index_santa_c, matrix)
    index_to_check = [index_santa_r, index_santa_c]
    if index_to_check in list_coordinates_nice_kids:
        list_coordinates_nice_kids.remove(index_to_check)
        presents_number -= 1
        counter_present_to_nice_kids += 1
        if presents_number == 0:
            santa_out_of_presents = True
            break
    elif index_to_check in list_coordinates_naughty_kids:
        list_coordinates_naughty_kids.remove(index_to_check)
        command = input()
        continue
    elif index_to_check in list_coordinates_cookies:
        indexes_around_cookie, matrix = santa_eats_cookie(index_santa_r, index_santa_c, matrix)
        list_coordinates_cookies.remove(index_to_check)
        for el in indexes_around_cookie:
            if el in list_coordinates_nice_kids:
                presents_number -= 1
                counter_present_to_nice_kids += 1
                list_coordinates_nice_kids.remove(el)
                if presents_number == 0:
                    santa_out_of_presents = True
                    break
            elif el in list_coordinates_naughty_kids:
                presents_number -= 1
                list_coordinates_naughty_kids.remove(el)
                if presents_number == 0:
                    santa_out_of_presents = True
                    break
    if santa_out_of_presents:
        break

    command = input()

if santa_out_of_presents and len(list_coordinates_nice_kids) > 0:
    print("Santa ran out of presents!")
    for el in matrix:
        print(' '.join(x for x in el))
    print(f'No presents for {len(list_coordinates_nice_kids)} nice kid/s.')
if len(list_coordinates_nice_kids) == 0:
    for el in matrix:
        print(' '.join(x for x in el))
    print(f'Good job, Santa! {counter_present_to_nice_kids} happy nice kid/s.')
#judge: 83/100








