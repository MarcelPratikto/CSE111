import math
# import the datetime class from the datetime module
from datetime import datetime

pi = math.pi
# width of tire (in milimeters)
w = float(input("width of tire (mm): "))
# aspect ratio of the tire
a = float(input("aspect ratio of tire: "))
# diameter of the wheel (in inches)
d = float(input("diameter of the wheel (in): "))

# volume of tire
v = (pi * w ** 2 * a * (w * a + 2540 * d)) / 10000000000
v = round(v, 2)
print(f"The volume of the tire is {v} liters")

# Stretch Challenge 1
# Find tire prices for four or more tire sizes online.
# 105, 70, 14 = $55     volume = 10.4
# 275, 75, 16 = $231    109.17
# 295, 70, 18 = $302    127.02
# 295, 65, 20 = $385    124.35
# Based on above, diameter of wheel is more expensive than ratio
# $5.29 per volume
# $2.12 per volume
# $2.38 per volume      ($2.12+$2.38)/2 = $2.25
# $3.10 per volume
# Add a set of if … elif … else statements in your program that use 
# the tire width, tire aspect ratio, and wheel diameter that 
# the user enters to find a price and then print the price.
price = 0.0
if d <= 14:
    price = 5.29 * v
elif d > 14 and d < 20:
    price = 2.25 * v
elif d >= 20:
    price = 3.10 * v
else:
    print(f"Unknown error while calculating price")
price = round(price, 2)
print(f"Estimated price of a tire of your choice: ${price}")

# gets current date & time from computer's clock
current_date_time = datetime.now()
# extract just the date
date = f"{current_date_time:%Y-%m-%d}"
print(f"Current date: {date}")

# opens volumes.txt for appending
with open("volumes.txt", mode="at") as volumes_txt:
    # appends to the end of volumes.txt with five values:
    # current date
    # width of tire
    # aspect ratio of tire
    # diameter of wheel
    # volume of tire
    values = f"{date}, {w}, {a}, {d}, {v}"
    print(f"values to append: {values}")
    print(values, file = volumes_txt)

# Stretch Challenge 2
# After your program prints the tire volume to the terminal, 
# your program should ask the user if she wants to buy tires 
# with the dimensions that she entered. 
# If the user answers "yes", 
# your program should ask for her phone number and 
# store her phone number in the volumes.txt file.
    want_to_buy = input("Do you want to buy tires with the following dimensions?: ").lower()
    if want_to_buy == "yes":
        phone = input("What is your phone number? ")
        print(f"Phone number: {phone}", file = volumes_txt)