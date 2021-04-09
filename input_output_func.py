import json
import pandas as pd

# used to create a new .txt file with a json object in it.
def new_json_txt(information, file):
    with open(file, 'w') as file:
        file.write(json.dumps(information, indent = 2))

# clears a .txt file and enters a empty json object into it.
# The empty object is necessary, because otherwise if the programm tries
# to read the file using json an error will be thrown out. The programm has to 
# be able to a .txt file with an empty json object in case the user does not 
# want to have a descriptive statistics output.
def clear_txt(file):
    with open(file, 'w+') as file:
        file.write(json.dumps([]))

# stores the data in a file. The format and name are defined by the user.
# index=False is used to drop the indexes in the files. This is necessary cause 
# otherwise there would allways be doulbe index columns if the user opens
# the file using e.g. Excel.
# Orient has to be the same as in the load_dataframe otherwise the file can not
# be opened properly.
def store_dataframe(form, name, data):
    if form == "csv":
        data.to_csv(f"{name}.csv", index=False)

    elif form == "json":

        information = data.to_json(orient='split', index=False)
        new_json_txt(information, f"{name}.txt")

    elif form == "stata":
        data.to_stata(f"{name}.dta", write_index=False)

    elif form == "excel":
        data.to_excel(f"{name}.xlsx", index=False)

    else:
        print("Invalid specifications.")

# Loads a file specified by the user and returns the contents.
# Orient has to be the same as in the store_dataframe function otherwise the file
# can not be opened properly.

def load_dataframe(form, name):
    if form == "csv":
        dataframe = pd.read_csv(name)
        return dataframe

    elif form == "json":    
         with open (name, "r") as file:
            x = json.load(file)
            dataframe = pd.read_json(x, orient='split')

            return dataframe

    elif form == "stata":
        dataframe = pd.read_excel(name)
        return dataframe

    elif form == "excel":
        dataframe = pd.read_excel(name)
        return dataframe

    else:
        print("Invalid specifications.")