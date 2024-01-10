def find_capitals(word):
    word_split = word.split()
    capitals = ''

    for word in word_split:
        for char in word:
            if char.isupper():
                capitals += char

    return capitals

