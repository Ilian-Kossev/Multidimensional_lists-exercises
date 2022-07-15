def get_magic_triangle(n):
    triangle = []
    for _ in range(n):
        triangle.append([])
    for row_num in range(n):
        for digit_num in range(row_num + 1):
            if row_num <= 1:
                triangle[row_num].append(1)
            else:
                if digit_num == 0 or digit_num == row_num:
                    number = 1
                    triangle[row_num].append(number)
                else:
                    number_1 = triangle[row_num - 1][digit_num - 1]
                    number_2 = triangle[row_num - 1][digit_num]
                    number = number_1 + number_2
                    triangle[row_num].append(number)
    return print(triangle)


get_magic_triangle(5)

