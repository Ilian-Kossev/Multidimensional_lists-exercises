matrix = []
rows = int(input())
for _ in range(rows):
    lines = [int(x) for x in input().split(', ')]
    matrix.append(lines)

n = len(matrix)
main_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = [matrix[i][-i-1] for i in range(n)]

print(f"Primary diagonal: {', '.join(str(x) for x in main_diagonal)}. Sum: {sum(main_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")



