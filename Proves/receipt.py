import csv
from datetime import datetime

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
    try:
        with open(filepath, "rt") as file_data:
            file = csv.reader(file_data)
            next(file)
            for line in file:
                if len(line) > 0:
                    key = line[key_column_index]
                    data_dist[key] = line
    except FileNotFoundError:
        print("Error: missing file")
        print(f"[Errno 2] No such file or directory: \'{filename}")
    except PermissionError:
        print("Error: missing file")
        print(f"[Errno 1] You do not have access to: \'{filename}")
    
    return data_dist


def compute_tax(subtotal):
    tax = .06
    tax_amount = subtotal * tax
    return tax_amount


def main():
    prod_dist = read_dictionary("products.csv", 0)
    # print("All products:")
    # print(prod_dist)

    print("Inkom Emporium")
    print()

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

    total_items = 0
    subtotal = 0
    for item in request:
        req_item_lt = request[item]
        amount = req_item_lt[1]
        total_items += int(amount)
        item_key = req_item_lt[0]
        try:
            item_lt = prod_dist[item_key]
        except KeyError:
            print("Error: unknown product ID in the request.csv file")
            print(f"\"{item_key}\"")
        item_name = item_lt[1]
        price = item_lt[2]
        subtotal += float(price) * int(amount)
        print(f"{item_name}: {amount} @ {price}")
        # print(item_lt)
        
    print()
    tax = compute_tax(subtotal)
    print(f"Number of Items: {total_items}")
    print(f"Subtotal: {round(subtotal, 2)}")
    print(f"Sales Tax: {round(tax, 2)}")
    print(f"Total: {round((subtotal + tax), 2)}")
    print()

    current_date_and_time = datetime.now()
    print("Thank you for shopping at the Inkom Emporium.")
    print(f"{current_date_and_time:%a %b:%d %X %Y}")

if __name__ == "__main__":
    main()