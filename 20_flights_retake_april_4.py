def flights(data):
    input_list = data.split(', ')
    catalogue = {}
    for n in range(len(input_list)):
        if input_list[n] == "'Finish'":
            break
        if n % 2 == 1:
            if input_list[n-1] not in catalogue:
                catalogue[input_list[n-1]] = int(input_list[n])
            else:
                catalogue[input_list[n-1]] += int(input_list[n])
    return catalogue


print(flights("'London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))"))


