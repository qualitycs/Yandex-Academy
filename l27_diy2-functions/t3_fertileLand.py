def fertile_land(*args, **kwargs):
    quantity = 0
    match_tup = 0
    check_list = []
    if 'first_larger' in kwargs:
        value = kwargs['first_larger']
        check_list.append(lambda x, y: x > y + value)
    if 'even_odd' in kwargs:
        value = kwargs['even_odd']
        check_list.append(lambda x, y: x % value == 0 and y % value != 0)
    if 'last_digit' in kwargs:
        value = kwargs['last_digit']
        check_list.append(lambda x, y: y % 10 != value)
    if 'second_triple' in kwargs:
        value = kwargs['second_triple']
        check_list.append(lambda x, y: y > pow(10, value - 1))

    for a, b in args:
        for check in check_list:
            if not check(a, b):
                break
        else:
            quantity += pow(b - a, 2)
            match_tup += 1
    return quantity, match_tup
