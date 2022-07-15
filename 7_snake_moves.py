rows, cols = [int(x) for x in input().split()]
snake = input()
matrix = []
i = 0
for r in range(rows):
    lines = list()
    for c in range(cols):
        if i == len(snake):
            i = 0
        lines.append(snake[i])
        i += 1
    matrix.append(lines)


final_matrix = []
for row in range(len(matrix)):
    if row % 2 == 1:
        reversed_line = list(reversed(matrix[row]))
        final_matrix.append(reversed_line)
    else:
        final_matrix.append(matrix[row])
for row in final_matrix:
    print(''.join(row))


