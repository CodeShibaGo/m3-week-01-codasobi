def categorize_new_member(data):
    categorize = lambda x: 'Senior' if x[0] >= 55 and x[1] > 7 else 'Open'
    member_category = list(map(categorize, data))

    return member_category
