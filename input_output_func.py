import json
import pandas as pd

def new_json_txt(information, file):
    with open(file, 'w') as file:
        file.write(json.dumps(information, indent = 2))

def clear_txt(file):
    with open(file, 'w+') as file:
        file.truncate()

def store_dataframe(form, name, data):
    ## Have to build logic that differs between which datafromat is requested
    ## by the user.
    if form == "csv":
        data.to_csv(f"{name}.csv")

    elif form == "json":
        information = data.to_json()
        ## only converts to a json string have to add the code to write it to a 
        ## txt file.
        new_json_txt(information, f"{name}.txt")

    elif form == "stata":
        data.to_stata(f"{name}.dta")

    elif form == "excel":
        data.to_excel(f"{name}.xlsx")

    else:
        print("Invalid specifications.")

def load_dataframe(form, name):
    if form == "csv":
        dataframe = pd.read_csv(name)
        return dataframe

    elif form == "json":    
        ## Here there are problems loading the file
        ## ValueError("DataFrame constructor not properly called!")
        dataframe = pd.read_json(name)
        return dataframe

    elif form == "stata":
        dataframe = pd.read_excel(name)
        return dataframe

    elif form == "excel":
        dataframe = pd.read_excel(name)
        return dataframe

    else:
        print("Invalid specifications.")