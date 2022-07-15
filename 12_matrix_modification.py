rows = int(input())
matrix = []
for n in range(rows):
    row_matrix = [int(x) for x in input().split()]
    matrix.append(row_matrix)

command = input()
while not command == 'END':
    line = command.split()
    action, row, col, value = line
    r = int(row)
    c = int(col)
    v = int(value)
    if r not in range(len(matrix)) or c not in range(len(matrix[r])):
        print('Invalid coordinates')
        command = input()
        continue
    if action == 'Add':
        matrix[r][c] += v
    elif action == 'Subtract':
        matrix[r][c] -= v
    command = input()
for n in range(rows):
    print(' '.join(str(x) for x in matrix[n]))

