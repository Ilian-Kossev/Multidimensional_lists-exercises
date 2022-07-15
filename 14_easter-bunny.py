def check_up(index_row, index_column, collection):
    if index_row > 0:
        direction = 'up'
        sum_numbers = 0
        path = []
        for i in range(index_row - 1, -1, -1):
            step = []
            if not collection[i][index_column] == 'X':
                number = int(collection[i][index_column])
                sum_numbers += number
                step.append(i)
                step.append(index_column)
                path.append(step)
            else:
                break
        return direction, sum_numbers, path


def check_down(index_row, index_column, collection):
    if index_row < len(collection) - 1:
        direction = 'down'
        sum_numbers = 0
        path = []
        for i in range(index_row + 1, len(collection)):
            step = []
            if not collection[i][index_column] == 'X':
                number = int(collection[i][index_column])
                sum_numbers += number
                step.append(i)
                step.append(index_column)
                path.append(step)
            else:
                break
        return direction, sum_numbers, path


def check_left(index_row, index_column, collection):
    if index_column > 0:
        direction = 'left'
        sum_numbers = 0
        path = []
        for i in range(index_column - 1, -1, -1):
            step = []
            if not collection[index_row][i] == 'X':
                number = int(collection[index_row][i])
                sum_numbers += number
                step.append(index_row)
                step.append(i)
                path.append(step)
            else:
                break
        return direction, sum_numbers, path


def check_right(index_row, index_column, collection):
    if index_column < len(collection) - 1:
        direction = 'right'
        sum_numbers = 0
        path = []
        for i in range(index_column + 1, len(collection)):
            step = []
            if not collection[index_row][i] == 'X':
                number = int(collection[index_row][i])
                sum_numbers += number
                step.append(index_row)
                step.append(i)
                path.append(step)
            else:
                break
        return direction, sum_numbers, path


n = int(input())
matrix = []
for _ in range(n):
    line = input().split()
    matrix.append(line)

index_r = 0
index_c = 0
bunny_found = False
for r in range(n):
    for c in range(n):
        if matrix[r][c] == 'B':
            index_r = r
            index_c = c
            bunny_found = True
            break
    if bunny_found:
        break

list_max_sum_steps = []
catalogue = dict()

result_up = None
result_down = None
result_left = None
result_right = None
if check_up(index_r, index_c, matrix):
    result_up = check_up(index_r, index_c, matrix)
    list_max_sum_steps.append(result_up[1])
    catalogue[result_up[0]] = (result_up[1], result_up[2])
if check_down(index_r, index_c, matrix):
    result_down = check_down(index_r, index_c, matrix)
    list_max_sum_steps.append(result_down[1])
    catalogue[result_down[0]] = (result_down[1], result_down[2])
if check_left(index_r, index_c, matrix):
    result_left = check_left(index_r, index_c, matrix)
    list_max_sum_steps.append(result_left[1])
    catalogue[result_left[0]] = (result_left[1], result_left[2])
if check_right(index_r, index_c, matrix):
    result_right = check_right(index_r, index_c, matrix)
    list_max_sum_steps.append(result_right[1])
    catalogue[result_right[0]] = (result_right[1], result_right[2])

max_num = max(list_max_sum_steps)

for key, value in catalogue.items():
    if max_num == value[0]:
        print(key)
        for el in value[1]:
            print(el)
        print(value[0])






