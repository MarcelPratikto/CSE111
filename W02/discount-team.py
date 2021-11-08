from datetime import datetime

current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()

total_price = float()
sales_tax = float()
subtotal = float(input("Please enter the subtotal: "))
buy_more = float()
discount = float()

def price_math():
    global total_price
    global sales_tax
    global subtotal
    global buy_more
    global discount
    if day_of_week == 1 or 2:
        if subtotal >= 50:
            discount = subtotal * .1
            subtotal = subtotal * .9
            print(f"Your discount: {discount:.2f}$")
        else:
            buy_more = 50 - subtotal #stretch (get the amount remainder the user needs to buy to get the discount)
            print(f'You will need to purchase ${buy_more} to get the 10% discount')
    sales_tax = subtotal * .06
    total_price = sales_tax + subtotal
    
price_math()
print(f'Subtotal: {subtotal}')
print(f'Sales tax amount: {sales_tax:.2f}')
print(f'Total: {total_price:.2f}$')