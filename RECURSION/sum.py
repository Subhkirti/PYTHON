def sum_list(list):
    if len(list)==1:
        return list[0]
    return list[0] + sum_list(list[1:])
print(sum_list([1, 4, 7, 10]))
                            