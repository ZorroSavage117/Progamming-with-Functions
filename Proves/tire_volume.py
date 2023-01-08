# page start
import math
print()

# functions
# variables
vol = 0
pi = math.pi
wid = 0
asp = 0
dia = 0

# main code
wid = int(input("Enter the width of the tire in mm (ex 205): "))
asp = int(input("Enter the aspect ratio of the tire (ex 60): "))
dia = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# calcutions
vol = (pi * (pow(wid, 2)) * asp * (wid * asp + (2540 * dia))) / 10000000000

# page set up
print()

# output
print(f"The approximate volume is {vol:.2f} liters")

# page end
print()
