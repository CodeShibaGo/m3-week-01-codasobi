def find_capitals(word):
    word_split = word.split()
    capitals = ''
    for word_split in word_split:
        capitals += word_split[0]
    return capitals

