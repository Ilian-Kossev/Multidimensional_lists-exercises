from collections import deque

orders_row = deque([int(x) for x in input().split(', ')])
workers_row = [int(x) for x in input().split(', ')]

number_pizzas_made = 0
number_pizzas_left = 0
while orders_row and workers_row and number_pizzas_left == 0:
    order = orders_row.popleft()
    worker = workers_row.pop()
    if (order <= 0 or order > 10) and number_pizzas_left == 0:
        workers_row.append(worker)
        continue
    if not number_pizzas_left == 0:
        orders_row.appendleft(order)
        process_order = worker - number_pizzas_left
        if process_order >= 0:
            number_pizzas_made += number_pizzas_left
            number_pizzas_left = 0
            continue
        else:
            number_pizzas_left = abs(process_order)
            number_pizzas_made += worker
            continue

    process_order = worker - order
    if process_order >= 0:
        number_pizzas_made += order
        continue
    else:
        number_pizzas_left = abs(process_order)
        number_pizzas_made += worker
        continue

if len(orders_row) == 0 and number_pizzas_left == 0:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {number_pizzas_made}')
    print(f"Employees: {', '.join(str(x) for x in workers_row)}")
else:
    print('Not all orders are completed.')
    if number_pizzas_left == 0:
        print(f"Orders left: {', '.join(str(x) for x in orders_row)}")
    else:
        print(f"Orders left: {number_pizzas_left}, {', '.join(str(x) for x in orders_row)}")

# judge: 66/100