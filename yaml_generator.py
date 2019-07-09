import os
import yaml

def room():
    return {"description": None}

def stats():
    return {
        "attack": None,
        "weight": None,
        "amount": None,
        "strength": None,
        "equipable": None
    }

def item():
    return {
        "name": None,
        "description": None,
        "stats": stats()
    }

def player():
    return {
        "name": None,
        "description": None,
        "items": item()
    }

def yaml_writer(types, num):
    file_name = "./generic_" + types.__name__ + "s.yml"
    with open(file_name, "w") as save_file:
        yaml.dump(
            {i:types() for i in range(num)},
            save_file,
            default_flow_style=False
        )

yaml_writer(room, 100)
yaml_writer(player, 20)
yaml_writer(item, 50)
