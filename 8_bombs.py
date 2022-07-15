n = int(input())
matrix = []
for rows in range(n):
    line = [int(x) for x in input().split()]
    matrix.append(line)

alpha = -1
delta = -1
omega = 2
gama = 2

coordinates_list = input().split()
for i in range(len(coordinates_list)):
    r, c = [int(x) for x in (coordinates_list[i].split(','))]
    if r == 0:
        alpha = 0
    elif r == len(matrix) - 1:
        omega = 1
    if c == 0:
        delta = 0
    elif c == len(matrix) - 1:
        gama = 1

    for v in range(alpha, omega):
        for f in range(delta, gama):
            if v == 0 and f == 0:
                continue
            elif matrix[r+v][c+f] <= 0:
                continue
            matrix[r + v][c + f] -= matrix[r][c]

    alpha = -1
    delta = -1
    omega = 2
    gama = 2
    matrix[r][c] = 0

counter_cells = 0
sum_cells = 0
for row in matrix:
    for cell in row:
        if cell > 0:
            counter_cells += 1
            sum_cells += cell

print(f'Alive cells: {counter_cells}')
print(f'Sum: {sum_cells}')

for row in matrix:
    print(' '.join([str(x) for x in row]))

# judge: 90 /100

