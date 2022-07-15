input_data = input().split('|')
matrix = []
for n in range(len(input_data)-1, -1, -1):
    line = input_data[n].split()
    matrix.append(line)
flattened_matrix = [x for row in matrix for x in row]
print(' '.join(x for x in flattened_matrix))


