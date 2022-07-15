rows, cols = [int(x) for x in input().split()]
index_r_p = 0
index_r_c = 0
matrix = []
for r in range(rows):
    line = [x for x in input()]
    matrix.append(line)
    for v in range(cols):
        if line[v] == 'P':
            index_r_p = r
            index_r_c = v

last_position_r = 0
last_position_c = 0
last_position_bunny_r = 0
last_position_bunny_c = 0
player_wins = False
player_hits_bunny = False
bunny_hits_player = False
command_line = input()
for s in range(len(command_line)):
    if player_hits_bunny:
        break
    elif player_wins:
        break
    command = command_line[s]
    if command == 'L':
        index_r_c -= 1
        if index_r_c < 0:
            player_wins = True
            matrix[index_r_p][index_r_c + 1] = '.'
            last_position_r = index_r_p
            last_position_c = index_r_c + 1
        elif matrix[index_r_p][index_r_c] == 'B':
            player_hits_bunny = True
            last_position_r = index_r_p
            last_position_c = index_r_c
        else:
            matrix[index_r_p][index_r_c] = 'P'
            matrix[index_r_p][index_r_c + 1] = '.'
    elif command == 'R':
        index_r_c += 1
        if index_r_c > cols - 1:
            player_wins = True
            matrix[index_r_p][index_r_c - 1] = '.'
            last_position_r = index_r_p
            last_position_c = index_r_c - 1
        elif matrix[index_r_p][index_r_c] == 'B':
            player_hits_bunny = True
            last_position_r = index_r_p
            last_position_c = index_r_c
        else:
            matrix[index_r_p][index_r_c] = 'P'
            matrix[index_r_p][index_r_c - 1] = '.'
    elif command == 'U':
        index_r_p -= 1
        if index_r_p < 0:
            player_wins = True
            matrix[index_r_p + 1][index_r_c] = '.'
            last_position_r = index_r_p + 1
            last_position_c = index_r_c
        elif matrix[index_r_p][index_r_c] == 'B':
            player_hits_bunny = True
            last_position_r = index_r_p
            last_position_c = index_r_c
        else:
            matrix[index_r_p][index_r_c] = 'P'
            matrix[index_r_p + 1][index_r_c] = '.'
    elif command == 'D':
        index_r_p += 1
        if index_r_p > rows - 1:
            player_wins = True
            matrix[index_r_p - 1][index_r_c] = '.'
            last_position_r = index_r_p - 1
            last_position_c = index_r_c
        elif matrix[index_r_p][index_r_c] == 'B':
            player_hits_bunny = True
            last_position_r = index_r_p
            last_position_c = index_r_c
        else:
            matrix[index_r_p][index_r_c] = 'P'
            matrix[index_r_p - 1][index_r_c] = '.'

    ignore_list = []
    for i in range(rows):
        for c in range(cols):
            coordinates = str(i) + str(c)
            if matrix[i][c] == 'B' and coordinates not in ignore_list:
                if i > 0 and (matrix[i - 1][c] == '.' or matrix[i - 1][c] == 'P'):
                    if matrix[i - 1][c] == 'P':
                        matrix[i - 1][c] = 'B'
                        bunny_hits_player = True
                        last_position_bunny_r = i - 1
                        last_position_bunny_c = c
                    else:
                        matrix[i-1][c] = 'B'
                if c > 0 and (matrix[i][c - 1] == '.' or matrix[i][c - 1] == 'P'):
                    if matrix[i][c - 1] == 'P':
                        matrix[i][c - 1] = 'B'
                        bunny_hits_player = True
                        last_position_bunny_r = i
                        last_position_bunny_c = c - 1
                    else:
                        matrix[i][c - 1] = 'B'
                if i < len(matrix) - 1 and (matrix[i + 1][c] == '.' or matrix[i + 1][c] == 'P'):
                    temp_coordinates = str(i + 1) + str(c)
                    if matrix[i + 1][c] == 'P':
                        matrix[i + 1][c] = 'B'
                        ignore_list.append(temp_coordinates)
                        bunny_hits_player = True
                        last_position_bunny_r = i + 1
                        last_position_bunny_c = c
                    else:
                        matrix[i + 1][c] = 'B'
                        ignore_list.append(temp_coordinates)
                if c < len(matrix) - 1 and (matrix[i][c + 1] == '.' or matrix[i][c + 1] == 'P'):
                    if matrix[i][c + 1] == 'P':
                        matrix[i][c + 1] = 'B'
                        bunny_hits_player = True
                        last_position_bunny_r = i
                        last_position_bunny_c = c + 1
                        break
                    else:
                        matrix[i][c + 1] = 'B'
                        break
for r in range(rows):
    print(''.join(x for x in matrix[r]))
if player_wins:
    print(f'won: {last_position_r} {last_position_c}')
elif player_hits_bunny:
    print(f'dead: {last_position_r} {last_position_c}')
elif bunny_hits_player:
    print(f'dead: {last_position_bunny_r} {last_position_bunny_c}')


#judge: 30/100


