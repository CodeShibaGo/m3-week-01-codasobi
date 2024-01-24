from collections import OrderedDict
def distinct(seq):
    # if use set, might be different from the original order
    return list(OrderedDict.fromkeys(seq))
