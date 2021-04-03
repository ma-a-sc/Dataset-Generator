import json

def new_json_txt(information):
    with open("settings.txt", 'w') as file:
        file.write(json.dumps(information, indent = 2))

def clear_txt(txt_file):
    with open(txt_file, 'w+') as file:
        file.truncate()