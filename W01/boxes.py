import math

# the number of manufactured items
numManufacturedItems = int(input("Enter number of items: "))

# the number of items that the user will pack per box
numItemsPerBox = int(input("Enter number of items per box: "))

# compute and print the number of boxes necessary to hold the items.
# must be whole numbers!
numBoxes = math.ceil(numManufacturedItems / numItemsPerBox)
print(f"You will need {numBoxes} boxes.\n")