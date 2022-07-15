def check_knight(ind_r, ind_c, collection):
    knight_found = 0
    if (ind_r - 2) in range(len(collection)) and (ind_c + 1) in range(len(collection)) and collection[ind_r-2][ind_c+1] == 'K':
        knight_found += 1
    if (ind_r - 1) in range(len(collection)) and (ind_c + 2) in range(len(collection)) and collection[ind_r - 1][ind_c + 2] == 'K':
        knight_found += 1
    if (ind_r - 2) in range(len(collection)) and (ind_c - 1) in range(len(collection)) and collection[ind_r - 2][ind_c - 1] == 'K':
        knight_found += 1
    if (ind_r - 1) in range(len(collection)) and (ind_c - 2) in range(len(collection)) and collection[ind_r - 1][ind_c - 2] == 'K':
        knight_found += 1
    if (ind_r + 2) in range(len(collection)) and (ind_c + 1) in range(len(collection)) and collection[ind_r + 2][ind_c + 1] == 'K':
        knight_found += 1
    if (ind_r + 1) in range(len(collection)) and (ind_c + 2) in range(len(collection)) and collection[ind_r+1][ind_c+2] == 'K':
        knight_found += 1
    if (ind_r + 2) in range(len(collection)) and (ind_c - 1) in range(len(collection)) and collection[ind_r+2][ind_c-1] == 'K':
        knight_found += 1
    if (ind_r + 1) in range(len(collection)) and (ind_c - 2) in range(len(collection)) and collection[ind_r+1][ind_c-2] == 'K':
        knight_found += 1
    return knight_found


n = int(input())
matrix = []
for num in range(n):
    line = [x for x in input()]
    matrix.append(line)

catalogue = dict()
counter_removed_knights = 0

while True:
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'K':
                hits = check_knight(r, c, matrix)
                catalogue[(r, c)] = hits

    max_value = 0
    for num in catalogue.values():
        if num > max_value:
            max_value = num
    if max_value == 0:
        break

    index_r = 0
    index_c = 0
    for key, value in catalogue.items():
        if value == max_value:
            index_r, index_c = key

    catalogue.clear()
    matrix[index_r][index_c] = '0'
    counter_removed_knights += 1
print(counter_removed_knights)
#judge: 20/100













