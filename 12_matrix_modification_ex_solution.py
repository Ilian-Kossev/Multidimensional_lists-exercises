def is_invalid_poistion(size, row, col):
    if row >= size or row < 0 or col >= size or col < 0:
        return True
    else:
        return False


size = int(input())
matrix = []
for _ in range(size):
    matrix.append([int(x) for x in input().split()])

while True:
    line = input()
    if line == 'END':
        break
    args = line.split()
    command = args[0]
    row, col, value = [int(x) for x in args[1:]]
    if is_invalid_poistion(size, row, col):
        print('Invalid coordinates')
        continue
    if command == 'Add':
        matrix[row][col] += value
    else:
        matrix[row][col] -= value

for row_elements in matrix:
    print(' '.join([str(x) for x in row_elements]))

