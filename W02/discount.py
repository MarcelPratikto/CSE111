from datetime import date
import calendar

# current day of the week
# date.today() outputs a number, with 0 being Monday and 6 being Sunday
day = calendar.day_name[date.today().weekday()]
print(day)

# customer's subtotal
subtotal = float(input("What is your subtotal? "))

