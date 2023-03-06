import csv

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    filepath = "./Resorses/" + filename
    data_dist = {}
    with open(filepath, "rt") as file_data:
        file = csv.reader(file_data)
        next(file)
        for line in file:
            if len(line) > 0:
                key = line[key_column_index]
                data_dist[key] = line
    
    return data_dist


def main():
    prod_dist = read_dictionary("products.csv", 0)
    print("All products:")
    print(prod_dist)

    print("Requested items:")
    request = {}
    key = 1
    filepath = "./Resorses/request.csv"
    with open(filepath) as file_data:
        file = csv.reader(file_data)
        next(file)
        for line in file:
            request[key] = line
            key += 1

    for item in request:
        req_item_lt = request[item]
        amount = req_item_lt[1]
        item_key = req_item_lt[0]
        item_lt = prod_dist[item_key]
        item_name = item_lt[1]
        price = item_lt[2]
        print(f"{item_name}: {amount} @ {price}")
        # print(item_lt)

if __name__ == "__main__":
    main()