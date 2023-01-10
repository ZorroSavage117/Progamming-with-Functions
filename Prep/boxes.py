# page start
import math
print()

# functions
# varables
num_items = 0
box_items = 0
num_boxs = 0

# main code
num_items = int(input("Enter the number of items: "))
box_items = int(input("Enter the number of items per box: "))

num_boxs = num_items / box_items
num_boxs = math.ceil(num_boxs)

print(f"\nFor {num_items} items, packing {box_items} items in each box, you will need {num_boxs} boxes.")

# page end
print()
