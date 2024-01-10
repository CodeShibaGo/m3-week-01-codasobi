def count_sheep(sheeps):
    sleep_sheeps = 0
    for sheep in sheeps:
        if sheep == True:
            sleep_sheeps += 1
    return sleep_sheeps
