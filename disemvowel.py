# 將一個字串中的所有母音字元（a、e、i、o、u）都移除，並返回新的字串
def disemvowel(old_word):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    new_word = ''
    for char in old_word:
        if char not in vowels:
            new_word += char

    return new_word
