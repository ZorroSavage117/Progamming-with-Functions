import datetime

# Get the current date and format it as a string
current_date = datetime.date.today().strftime("%Y-%m-%d")

# Create a dictionary with the current date as the key
my_dict = {current_date: "Some value"}

# Print the dictionary
print(my_dict)
