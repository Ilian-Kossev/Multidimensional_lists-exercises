def swap_values(i_1, i_2, i_3, i_4, collection):
    collection[i_1][i_2], collection[i_3][i_4] = collection[i_3][i_4], collection[i_1][i_2]
    return collection


matrix = []
rows, columns = [int(x) for x in input().split()]

for _ in range(rows):
    lines = input().split(' ')
    matrix.append(lines)

command = input()
while not command == 'END':
    command_line = command.split()
    if not command.startswith('swap') and len(command_line) != 5:
        print('Invalid input!')
        command = input()
        continue
    command_line.pop(0)
    c_1, c_2, c_3, c_4 = [int(x) for x in command_line]
    if c_1 not in range(rows) or c_3 not in range(rows):
        print('Invalid input!')
        command = input()
        continue
    if c_2 not in range(columns) or c_4 not in range(columns):
        print('Invalid input!')
        command = input()
        continue
    swap_values(c_1, c_2, c_3, c_4, matrix)
    for rows in matrix:
        print(' '.join(str(x) for x in rows))
    command = input()

#Traceback (most recent call last):
#  File "C:/Users/usr/PycharmProjects/36_Multidimensional_lists_Ex/7_snake_moves.py", line 27, in <module>
#    if c_1 not in range(rows): or c_3 not in range(rows):
#TypeError: 'list' object cannot be interpreted as an integer

