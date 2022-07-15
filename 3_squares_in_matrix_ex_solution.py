matrix = []
rows, columns = [int(x) for x in input().split()]

for _ in range(rows):
    matrix.append(input().split())


counter_squares = 0
for r in range(rows-1):
    for c in range(columns-1):
        if matrix[r][c] == matrix[r][c+1] == matrix[r+1][c] == matrix[r+1][c+1]:

            counter_squares += 1
print(counter_squares)
