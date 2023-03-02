import csv

def read_dictionary(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    filepath = "./Resorses/" + filename
    data_dist = {}
    with open(filepath, "rt") as file_data:
        file = csv.reader(file_data)
        next(file)
        for line in file:
            if len(line) > 0:
                key = line[0]
                data_dist[key] = line
    
    return data_dist


def main():
    ID_NUM = 0
    NAME = 1
    cur_dict = read_dictionary("students.csv")
    # keys = cur_dict.keys()
    # print(keys)
    find_id = input("I-Number: ")

    id_fond = True
    for id in cur_dict:
        id_fond = find_id == id 
        if id_fond:
            break

    # print(id_fond)

    if id_fond:
        name_lt = cur_dict[find_id]
        name = name_lt[NAME]
    else:
        name = "I-Number not found"

    print(name)

if __name__ == "__main__":
    main()