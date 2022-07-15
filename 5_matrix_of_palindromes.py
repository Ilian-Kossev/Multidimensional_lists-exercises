rows, columns = [int(x) for x in input().split()]

matrix = []
for r in range(rows):
    line = []
    for c in range(r, columns+r):
        palindrome = (chr(r+97) + chr(c+97) + chr(r+97))
        line.append(palindrome)
    matrix.append(line)


for line in matrix:
    print(' '.join(line))