# 1705 --> 18
# 1900 --> 19
# 1601 --> 17
# 2000 --> 20

def century(year):
    str_year = str(year)
    if str_year[2] + str_year [3] == '00':
        return int(str_year[0] + str_year[1])
    else:
        return int(str_year[0] + str_year[1]) + 1

century(2321)
