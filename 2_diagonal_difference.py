matrix = []
rows = int(input())
for _ in range(rows):
    lines = [int(x) for x in input().split(' ')]
    matrix.append(lines)

n = len(matrix)
main_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = [matrix[i][-i-1] for i in range(n)]
sum_main_diagonal = sum(main_diagonal)
sum_secondary_diagonal = sum(secondary_diagonal)
difference = abs(sum_main_diagonal - sum_secondary_diagonal)

print(difference)
