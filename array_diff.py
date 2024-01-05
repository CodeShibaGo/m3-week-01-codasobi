def array_diff(list_a, list_b):
    list_diff = [x for x in list_a if x not in list_b]
    return list_diff
