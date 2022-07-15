def coordinates_are_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size


def sum_d_coordinates(row, col, collection):
    left_d = int(collection[row][0])
    right_d = int(collection[row][6])
    up_d = int(collection[0][col])
    down_d = int(collection[6][col])
    return 2 * (left_d + right_d + up_d + down_d)


def sum_t_coordinates(row, col, collection):
    left_d = int(collection[row][0])
    right_d = int(collection[row][6])
    up_d = int(collection[0][col])
    down_d = int(collection[6][col])
    return 3 * (left_d + right_d + up_d + down_d)


player_1, player_2 = [x for x in input().split(', ')]
matrix = []
for r in range(7):
    line = input().split()
    matrix.append(line)


points_player_1 = 501
points_player_2 = 501

counter_players = 0
counter_throws_player_1 = 0
counter_throws_player_2 = 0
player_1_won = False
player_2_won = False
while True:
    if counter_players % 2 == 0:
        counter_throws_player_1 += 1
    else:
        counter_throws_player_2 += 1
    current_score = 0
    coordinates = input()
    r, c = int(coordinates[1]), int(coordinates[4])
    if not coordinates_are_valid(r, c, 7):
        counter_players += 1
        continue
    else:
        if matrix[r][c] == 'D':
            current_score = sum_d_coordinates(r, c, matrix)
        elif matrix[r][c] == 'T':
            current_score = sum_t_coordinates(r, c, matrix)
        elif matrix[r][c] == 'B':
            if counter_players % 2 == 0:
                player_1_won = True
                break
            elif counter_players % 2 == 1:
                player_2_won = True
                break
        else:
            current_score = int(matrix[r][c])

    if counter_players % 2 == 0:
        points_player_1 -= current_score
        if points_player_1 <= 0:
            player_1_won = True
            break

    else:
        points_player_2 -= current_score
        if points_player_2 <= 0:
            player_2_won = True
            break
    current_score = 0
    counter_players += 1


if player_1_won:
    print(f'{player_1} won the game with {counter_throws_player_1} throws!')
else:
    print(f'{player_2} won the game with {counter_throws_player_2} throws!')

# judge: 71 /100 /two runtime errors/