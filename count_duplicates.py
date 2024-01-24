def count_duplicates(text):
    text = text.upper()
    text_count = {}

    for char in text:
        if char in text_count:
            text_count[char] += 1
        else:
            text_count[char] = 1

    duplicates = 0
    for count in text_count.values():
        if count > 1:
            duplicates += 1
    return duplicates
