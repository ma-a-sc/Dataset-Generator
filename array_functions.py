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

def fill_string_array(list_of_choices, number_of_obs):

    array = random.choices(list_of_choices, k=number_of_obs)

    return array


def choices_loop():

    how_many_choices = int(input("How many different possibilities should the variable have?"))
    x = 0
    list_of_choices = []
    while x < how_many_choices:
        new_choice = input("Please name the possibility:\n>")
        list_of_choices.append(new_choice)
        x += 1

        print(list_of_choices)

    return list_of_choices


