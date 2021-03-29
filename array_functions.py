import random

def index_setter(int_input):
    x = 1
    y = 1
    indexes = []
    
    while x <= int_input:
        indexes.append(y)
        x  += 1
        y += 1

    return indexes


def fill_int_aray(bot, top, number_of_obs):
    x = 0

    array = []

    while x < number_of_obs:
        y = random.randint(bot, top)
        array.append(y)

        x += 1

    return array

def fill_float_array(bot, top, number_of_obs):
    x = 0

    array = []

    while x < number_of_obs:
        y = random.uniform(bot, top)
        array.append(y)

        x += 1

    return array
