from sys import maxsize


matrix = []
rows, columns = [int(x) for x in input().split()]

max_sum = - maxsize

for _ in range(rows):
    lines = [int(x) for x in input().split(' ')]
    matrix.append(lines)

max_square = list()
for r in range(rows-2):
    for c in range(columns-2):
        sum_square = sum(matrix[r][c:c+3]) + sum(matrix[r+1][c:c+3]) + sum(matrix[r+2][c:c+3])
        if sum_square > max_sum:
            max_sum = sum_square
            max_square.clear()
            max_square.append(matrix[r][c:c+3])
            max_square.append((matrix[r+1][c:c+3]))
            max_square.append((matrix[r+2][c:c+3]))

print(f'Sum = {max_sum}')
for r in max_square:
    print(' '.join([str(x) for x in r]))


