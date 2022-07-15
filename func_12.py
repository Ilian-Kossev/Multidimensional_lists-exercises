def math_operations(*args, **kwargs):
    args_num = [x for x in args]
    kwargs_count = 0
    elements_list_count = 1
    idx_args_list_count = 0
    while elements_list_count <= len(args_num):
        if kwargs_count == 0:
            kwargs['a'] += args_num[idx_args_list_count]
        elif kwargs_count == 1:
            kwargs['s'] -= args_num[idx_args_list_count]
        elif kwargs_count == 2:
            if args_num[idx_args_list_count] == 0:
                args_num.remove(args_num[idx_args_list_count])
                kwargs_count += 1
                continue
            kwargs['d'] /= args_num[idx_args_list_count]
        elif kwargs_count == 3:
            kwargs['m'] *= args_num[idx_args_list_count]
        if kwargs_count == 3:
            kwargs_count = -1
        elements_list_count += 1
        kwargs_count += 1
        idx_args_list_count += 1
    return kwargs


#print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))

