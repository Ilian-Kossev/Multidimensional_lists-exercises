n = int(input())
directions = input().split()
matrix = []
counter_coal = 0
for rows in range(n):
    line = input().split()
    matrix.append(line)
    for el in line:
        if el == 'c':
            counter_coal += 1

index_r = 0
index_c = 0

starting_position_found = False
for r in range(len(matrix)):
    for c in range(len(matrix)):
        if matrix[r][c] == 's':
            index_r = r
            index_c = c
            starting_position_found = True
            break
    if starting_position_found:
        break

collected_coal = 0
game_over = False
for index in range(len(directions)):
    command = directions[index]
    if command == 'left':
        if not index_c == 0:
            index_c -= 1
        else:
            continue
    elif command == 'right':
        if not index_c == len(matrix) - 1:
            index_c += 1
        else:
            continue
    elif command == 'up':
        if not index_r == 0:
            index_r -= 1
        else:
            continue
    elif command == 'down':
        if not index_r == len(matrix) - 1:
            index_r += 1
        else:
            continue
    if matrix[index_r][index_c] == 'c':
        matrix[index_r][index_c] = '*'
        collected_coal += 1
    elif matrix[index_r][index_c] == 'e':
        print(f'Game over! ({index_r}, {index_c})')
        game_over = True
        break
    if collected_coal == counter_coal:
        print(f'You collected all coal! ({index_r}, {index_c})')
        break
if collected_coal < counter_coal and not game_over:
    print(f'{counter_coal - collected_coal} pieces of coal left. ({index_r}, {index_c})')







