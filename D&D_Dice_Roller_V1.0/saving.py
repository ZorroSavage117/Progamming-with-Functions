import json
import datetime

def session_storage_update(storage_dict, roll_list, sides):
    """
    Updates the storage_dict with the new roll_list for the specified dice type (sides).
    Returns the updated storage_dict.
    """
    dice_key = find_key(sides)
    storage_dict[dice_key].append(roll_list)

    return storage_dict

def session_start():
    """
    Creates a new session dictionary with today's date as the key and empty lists for each dice type.
    Returns the new session dictionary.
    """
    current_date = datetime.date.today().strftime("%Y-%m-%d")

    session = {
        current_date: {
            "d4": [],
            "d6": [],
            "d8": [],
            "d10": [],
            "d12": [],
            "d20": [],
            "d100": [],
            "d?": []
        }
    }
    
    return session

def session_save(storage_dict):
    """
    Saves the storage_dict to a JSON file.
    """
    try:
        with open("./D&D_Dice_Roller_V1.0/saves.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    # Update the data with the new storage_dict dictionary
    data.update(storage_dict)

    with open("./D&D_Dice_Roller_V1.0/saves.json", "w") as file:
        json.dump(data, file)

def load_saves():
    """
    Loads the saved data from the JSON file and returns it as a dictionary.
    """
    with open("./D&D_Dice_Roller_V1.0/saves.json", "r") as file:
        data = json.load(file)

    return data

def find_key(sides):
    """
    Returns the appropriate key for the storage dictionary based on the specified number of sides.
    """
    if sides == 20:
        return "d20"
    elif sides == 6:
        return "d6"
    elif sides == 8:
        return "d8"
    elif sides == 4:
       return "d4"
    elif sides == 12:
        return "d12"
    elif sides == 10:
        return "d10"
    elif sides == 100:
        return "d100"
    else:
        return "d?"
