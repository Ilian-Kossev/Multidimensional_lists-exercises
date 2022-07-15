n = int(input())
matrix = []
for r in range(n):
    data = input().split()
    line = []
    for el in data:
        if el not in 'AR.':
            x = int(el)
            line.append(x)
        else:
            line.append(el)
    matrix.append(line)

index_Alice_r = 0
index_Alice_c = 0
for row in range(n):
    for col in range(n):
        if matrix[row][col] == 'A':
            index_Alice_r = row
            index_Alice_c = col


def collect_tea_bags(ind_r, ind_c, collection):
    teabags_num = 0
    teabags_num += collection[ind_r][ind_c]
    return teabags_num


teabags = 0
command = input()
while True:
    matrix[index_Alice_r][index_Alice_c] = '*'
    index_out_of_range = False
    fell_in_hole = False
    teabags_collected = False
    if command == 'down':
        index_Alice_r += 1
        if index_Alice_r in range(n):
            if type(matrix[index_Alice_r][index_Alice_c]) == int:
                teabags += collect_tea_bags(index_Alice_r, index_Alice_c, matrix)
                matrix[index_Alice_r][index_Alice_c] = '*'
            elif matrix[index_Alice_r][index_Alice_c].isalpha():
                matrix[index_Alice_r][index_Alice_c] = '*'
                fell_in_hole = True
                break
            else:
                matrix[index_Alice_r][index_Alice_c] = '*'
        else:
            index_out_of_range = True
            break
    elif command == 'up':
        index_Alice_r -= 1
        if index_Alice_r in range(n):
            if type(matrix[index_Alice_r][index_Alice_c]) == int:
                teabags += collect_tea_bags(index_Alice_r, index_Alice_c, matrix)
                matrix[index_Alice_r][index_Alice_c] = '*'
            elif matrix[index_Alice_r][index_Alice_c].isalpha():
                matrix[index_Alice_r][index_Alice_c] = '*'
                fell_in_hole = True
                break
            else:
                matrix[index_Alice_r][index_Alice_c] = '*'
        else:
            index_out_of_range = True
            break
    elif command == 'left':
        index_Alice_c -= 1
        if index_Alice_c in range(n):
            if type(matrix[index_Alice_r][index_Alice_c]) == int:
                teabags += collect_tea_bags(index_Alice_r, index_Alice_c, matrix)
                matrix[index_Alice_r][index_Alice_c] = '*'
            elif matrix[index_Alice_r][index_Alice_c].isalpha():
                matrix[index_Alice_r][index_Alice_c] = '*'
                fell_in_hole = True
                break
            else:
                matrix[index_Alice_r][index_Alice_c] = '*'
        else:
            index_out_of_range = True
            break
    if command == 'right':
        index_Alice_c += 1
        if index_Alice_c in range(n):
            if type(matrix[index_Alice_r][index_Alice_c]) == int:
                teabags += collect_tea_bags(index_Alice_r, index_Alice_c, matrix)
                matrix[index_Alice_r][index_Alice_c] = '*'
            elif matrix[index_Alice_r][index_Alice_c].isalpha():
                matrix[index_Alice_r][index_Alice_c] = '*'
                fell_in_hole = True
                break
            else:
                matrix[index_Alice_r][index_Alice_c] = '*'
        else:
            index_out_of_range = True
            break
    if teabags >= 10:
        teabags_collected = True
        break
    command = input()

if teabags_collected:
    print('She did it! She went to the party.')
elif fell_in_hole or index_out_of_range:
    print("Alice didn't make it to the tea party.")
for row in matrix:
    print(' '.join(str(x) for x in row))









