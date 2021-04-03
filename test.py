import input_output_func as iof
options = input("""
Which of the following options do you want to select? 
Multiple can be selected
using the ; symbol
Options:
mean, median, min, max, mode, variance, standard deviation
>""")

options2 = options.replace(" ", "")
options_split = options2.split(";")

print(options)

print(options_split)

## options must be safed at least in the one session, write it to a txt file using json

iof.clear_txt("settings.txt")