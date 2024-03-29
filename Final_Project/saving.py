import json
import datetime


def session_storage_update(storage_dict, roll_list, sides):
    dice_key = find_key(sides)
    storage_dict[dice_key].append(roll_list)

    return storage_dict


def session_start():
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


def session_save(storage_dist):
    try:
        with open("./Final_Project/saves.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    # Update the data with the new storage_dist dictionary
    data.update(storage_dist)

    with open("./Final_Project/saves.json", "w") as file:
        json.dump(data, file)


def load_saves():
    with open("./Final_Project/saves.json", "r") as file:
        data = json.load(file)

    return data


def find_key(sides):
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
    
    
# data = {
#     "d4": [],
#     "d6": [],
#     "d8": [],
#     "d10": [],
#     "d12": [],
#     "d20": [],
#     "d100": [],
#     "d?": []
# }
# roll_list = [1, 3, 2, 4]
# print(session_storage_update(data, roll_list, 4))
# roll_list = [1, 3, 2, 4]
# print(session_storage_update(data, roll_list, 4))
# roll_list = [1, 3, 2, 4]
# print(session_storage_update(data, roll_list, 4))

# session_save(data)

# saves = load_saves()
# print(f"saves: {saves}")