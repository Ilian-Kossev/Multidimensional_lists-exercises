def coordinates_valid(r, c, collection):
    return 0 <= r < len(collection) or 0 <= c < len(collection)


def sum_up(r, c, range_u, collection):
    sum_u = 0
    if range_u > 0:
        for n in range(1, range_u + 1):
            number = int(collection[r - n][c])
            sum_u += number
    return sum_u


def sum_down(r, c, range_d, collection):
    sum_d = 0
    if range_d <= 5:
        for n in range(1, range_d + 1):
            number = int(collection[r + n][c])
            sum_d += number
    return sum_d


matrix = []
for num in range(6):
    line = input().split()
    matrix.append(line)
total_sum = 0
list_coordinates = []
for n in range(3):
    coordinates = input().split()
    row = int(coordinates[0][1:-1])
    col = int(coordinates[1][:-1])

    if not coordinates_valid(row, col, matrix):
        continue
    if matrix[row][col] == 'B':
        t_coordinates = (row, col)
        if t_coordinates in list_coordinates:
            continue
        list_coordinates.append(t_coordinates)
        range_up = row
        range_down = 5 - row
        up_sum = sum_up(row, col, range_up, matrix)
        down_sum = sum_down(row, col, range_down, matrix)
        total_sum += (up_sum + down_sum)
if 100 <= total_sum < 200:
    prize = 'Football'
    print(f"Good job! You scored {total_sum} points, and you've won {prize}.")
elif 200 <= total_sum < 300:
    prize = 'Teddy Bear'
    print(f"Good job! You scored {total_sum} points, and you've won {prize}.")
elif total_sum >= 300:
    prize = 'Football'
    print(f"Good job! You scored {total_sum} points, and you've won {prize}.")
else:
    needed_points = 100 - total_sum
    print(f'Sorry! You need {needed_points} points more to win a prize.')
# judge: 50/100









