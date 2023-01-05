# page start
print()

# imports
# functions
# varables
age = 0
rate1 = 0
rate2 = 0
maxrate = 0

# main code
age = int(input("What is your age: "))
maxrate = 220 - age
rate1 = int(maxrate * .65)
rate2 = int(maxrate * .85)

# output
print(
    f"When you exercise to strengthen your heart, you should keep your heart rate between {rate1} and {rate2} beats per minute.")

# page end
print()
