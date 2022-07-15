rows, cols = [int(x) for x in input().split()]

matrix = []
for r in range(rows):
    line = [x for x in input().split()]
    matrix.append(line)


command = input()
while not command == 'END':
    list_command = command.split()
    if not command.startswith('swap') or not len(list_command) == 5:
        print('Invalid input!')
        command = input()
        continue
    action = list_command.pop(0)
    r_1, c_1, r_2, c_2 = [int(x) for x in list_command]
    if r_1 not in range(rows) or c_1 not in range(cols) or r_2 not in range(rows) or c_2 not in range(cols):
        print('Invalid input!')
        command = input()
        continue
    if action == 'swap':
        matrix[r_1][c_1], matrix[r_2][c_2] = matrix[r_2][c_2], matrix[r_1][c_1]
    for row in matrix:
        print(' '.join(x for x in row))

    command = input()
