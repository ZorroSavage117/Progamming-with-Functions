# page start
import math
from datetime import datetime
print()

# variables
vol = 0
pi = math.pi
wid = 0
asp = 0
dia = 0
date = "null"
name = "null"
phone = "null"
buy = "null"

# functions


def cal_volume(v, x, y, z):
    a = (v * (pow(x, 2)) * y * (x * y + (2540 * z))) / 10000000000
    return a


# main code
wid = int(input("Enter the width of the tire in mm (ex 205): "))
asp = int(input("Enter the aspect ratio of the tire (ex 60): "))
dia = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# calcutions
vol = cal_volume(pi, wid, asp, dia)
date = datetime.now()

# page set up
print()

# output
print(f"The approximate volume is {vol:.2f} liters")

# would like to buy?
buy = input("Would you like to buy these tires? ")

if buy.lower() == "yes" or buy.lower() == "y":
    name = input("Your first name for records: ")
    phone = input("Please enter a phone number [ex: (xxx)xxx-xxxx ]: ")

# file add
with open("./Resorses/volumes.txt", "at") as volumes_file:
    print(f"{date:%Y-%m-%d}, {wid}, {asp}, {dia}, {vol:.2f}, {name}, {phone}", file=volumes_file)

# page end
print()
