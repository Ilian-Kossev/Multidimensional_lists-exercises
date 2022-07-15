def shoot(ind_r_shooter, ind_c_shooter, direction, collection):
    target_hit = list()
    if direction == 'up':
        if ind_r_shooter > 0:
            shooting_range = ind_r_shooter - 1
            for row in range(shooting_range):
                if collection[ind_r_shooter - row - 1][ind_c_shooter] == 'x':
                    target_hit.append(ind_r_shooter - row - 1)
                    target_hit.append(ind_c_shooter)
                    collection[ind_r_shooter - row - 1][ind_c_shooter] = '.'
                    break
    elif direction == 'down':
        if ind_r_shooter < 4:
            shooting_range = len(collection) - ind_r_shooter - 1
            for row in range(shooting_range):
                if collection[ind_r_shooter + row + 1][ind_c_shooter] == 'x':
                    target_hit.append(ind_r_shooter + row + 1)
                    target_hit.append(ind_c_shooter)
                    collection[ind_r_shooter + row + 1][ind_c_shooter] = '.'
                    break
    elif direction == 'right':
        if ind_c_shooter < 4:
            shooting_range = len(collection) - ind_c_shooter - 1
            for col in range(shooting_range):
                if collection[ind_r_shooter][ind_c_shooter + col + 1] == 'x':
                    target_hit.append(ind_r_shooter)
                    target_hit.append(ind_c_shooter + col + 1)
                    collection[ind_r_shooter][ind_c_shooter + col + 1] = '.'
                    break
    elif direction == 'left':
        if ind_c_shooter > 0:
            shooting_range = ind_c_shooter - 1
            for col in range(shooting_range):
                if collection[ind_r_shooter][ind_c_shooter - col - 1] == 'x':
                    target_hit.append(ind_r_shooter)
                    target_hit.append(ind_c_shooter - col - 1)
                    collection[ind_r_shooter][ind_c_shooter - col - 1] = '.'
                    break
    return target_hit, collection


def move(ind_r_shooter, ind_c_shooter, direction, number_steps, collection):
    if direction == 'up':
        moving_range = number_steps
        if ind_r_shooter - number_steps >= 0 and collection[ind_r_shooter - 1][ind_c_shooter] == '.':
            collection[ind_r_shooter][ind_c_shooter] = '.'
            for _ in range(moving_range):
                if collection[ind_r_shooter - 1][ind_c_shooter] == '.':
                    ind_r_shooter -= 1
                else:
                    break
            collection[ind_r_shooter][ind_c_shooter] = 'A'

    elif direction == 'down':
        moving_range = number_steps
        if ind_r_shooter + number_steps < len(collection) and collection[ind_r_shooter + 1][ind_c_shooter] == '.':
            collection[ind_r_shooter][ind_c_shooter] = '.'
            for _ in range(moving_range):
                if collection[ind_r_shooter + 1][ind_c_shooter] == '.':
                    ind_r_shooter += 1
                else:
                    break
            collection[ind_r_shooter][ind_c_shooter] = 'A'

    elif direction == 'right':
        moving_range = number_steps
        if ind_c_shooter + number_steps < len(collection) and collection[ind_r_shooter][ind_c_shooter + 1] == '.':
            collection[ind_r_shooter][ind_c_shooter] = '.'
            for _ in range(moving_range):
                if collection[ind_r_shooter][ind_c_shooter + 1] == '.':
                    ind_c_shooter += 1
                else:
                    break
            collection[ind_r_shooter][ind_c_shooter] = 'A'
    elif direction == 'left':
        moving_range = number_steps
        if ind_c_shooter - number_steps >= 0 and collection[ind_r_shooter][ind_c_shooter - 1] == '.':
            collection[ind_r_shooter][ind_c_shooter] = '.'
            for _ in range(moving_range):
                if collection[ind_r_shooter][ind_c_shooter - 1] == '.':
                    ind_c_shooter -= 1
                else:
                    break
            collection[ind_r_shooter][ind_c_shooter] = 'A'
    return collection, ind_r_shooter, ind_c_shooter


matrix = []
for r in range(5):
    line = input().split()
    matrix.append(line)

shooter_index_r = 0
shooter_index_c = 0
counter_targets = 0
for r in range(5):
    for c in range(5):
        if matrix[r][c] == 'A':
            shooter_index_r = r
            shooter_index_c = c
        if matrix[r][c] == 'x':
            counter_targets += 1


targets_hit = []
all_targets_hit = False
number_of_commands = int(input())
for _ in range(number_of_commands):
    command = input()
    if command.startswith('shoot'):
        shoot_direction = command.split()[1]
        temp_res = shoot(shooter_index_r, shooter_index_c, shoot_direction, matrix)
        matrix = temp_res[1]
        if len(temp_res[0]) > 0:
            targets_hit.append(temp_res[0])
    elif command.startswith('move'):
        move_direction = command.split()[1]
        steps = int(command.split()[2])
        temp_res = move(shooter_index_r, shooter_index_c, move_direction, steps, matrix)
        matrix = temp_res[0]
        shooter_index_r = temp_res[1]
        shooter_index_c = temp_res[2]
    if counter_targets == len(targets_hit):
        all_targets_hit = True
        break
if all_targets_hit:
    print(f'Training completed! All {counter_targets} targets hit.')
else:
    targets_left = counter_targets - len(targets_hit)
    print(f'Training not completed! {targets_left} targets left.')
for el in targets_hit:
    print(el)


#judge: 54/100