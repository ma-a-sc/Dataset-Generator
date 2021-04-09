import random
# Generates the index used to create the dataframe.
def index_setter(int_input):
    x = 1
    y = 1
    indexes = []
    
    while x <= int_input:
        indexes.append(y)
        x  += 1
        y += 1

    return indexes

# fills a list with random integers with min=bot and max=top. How many are
# base on the number_of_obs.
# Returns the list.

def fill_int_aray(bot, top, number_of_obs):
    x = 0

    list_obs = []

    while x < number_of_obs:
        y = random.randint(bot, top)
        list_obs.append(y)

        x += 1

    return list_obs

# Same as fill_int_array just that the numbers are floatpoint numbers.

def fill_float_array(bot, top, number_of_obs):
    x = 0

    list_obs = []

    while x < number_of_obs:
        y = random.uniform(bot, top)
        list_obs.append(y)

        x += 1

    return list_obs

# Fills the list of observation based on the different possibilities (list_of_
# choices) and the length of the list is determined by number_of_obs.

def fill_string_array(list_of_choices, number_of_obs):

    list_obs = random.choices(list_of_choices, k=number_of_obs)

    return list_obs

# This loop lets the user specify the different posibilites the variable can 
# have.

def choices_loop():

    how_many_choices = int(input("How many different possibilities should the variable have?\n>"))
    x = 0
    list_of_choices = []
    while x < how_many_choices:
        new_choice = input("\nPlease name the possibility:\n>")
        list_of_choices.append(new_choice)
        x += 1

        print(list_of_choices)

    return list_of_choices