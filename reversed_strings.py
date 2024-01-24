# 寫一個函數，它接受一個字串作為輸入，並返回反轉後的字串。
def reverse_string(s):
    if isinstance(s, str):
        return s[::-1]
