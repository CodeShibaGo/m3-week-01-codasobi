def unique_in_order(iterable):
    list = []
    prev_char = ''

    for char in iterable:
        if char != prev_char:
            list.append(char)
            prev_char = char

    return list
