import json
import pandas as pd

def new_json_txt(information, file):
    with open(file, 'w') as file:
        file.write(json.dumps(information, indent = 2))

def clear_txt(file):
    with open(file, 'w+') as file:
        file.write(json.dumps([]))

def store_dataframe(form, name, data):
    ## Have to build logic that differs between which datafromat is requested
    ## by the user.
    if form == "csv":
        data.to_csv(f"{name}.csv", index=False)

    elif form == "json":

        ## safes the indexes as a the first column. If I load the data it will be
        ## in the first column.
        information = data.to_json(orient='split', index=False)
        new_json_txt(information, f"{name}.txt")

    elif form == "stata":
        data.to_stata(f"{name}.dta", index=False)

    elif form == "excel":
        data.to_excel(f"{name}.xlsx", index=False)

    else:
        print("Invalid specifications.")

def load_dataframe(form, name):
    if form == "csv":
        dataframe = pd.read_csv(name)
        return dataframe

    elif form == "json":    
        ## Here there are problems loading the file
        ## ValueError("DataFrame constructor not properly called!")
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