import json

def guardar(data):
    with open("data.json", "w") as f:
        json.dump(data, f)

def cargar():
    try:
        with open("data.json") as f:
            return json.load(f)
    except:
        return {}
