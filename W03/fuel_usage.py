# find fuel efficiency in miles per gallon (mpg)
def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.
    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    mpg = (end_miles - start_miles) / amount_gallons
    return mpg

# find fuel efficiency in liters per 100 kilometers (lp100k)
# based on mpg
def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.
    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    lp100k = 235.215 / mpg
    return lp100k

# MAIN
def main():
    # Get an odometer value in U.S. miles from the user.
    start_miles = float(input("Odometer start value (Miles): "))
    # Get another odometer value in U.S. miles from the user.
    end_miles = float(input("Odometer end value (Miles): "))
    # Get a fuel amount in U.S. gallons from the user.
    fuel_gallons = float(input("Fuel amount (Gallons): "))
    
    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.
    mpg = miles_per_gallon(start_miles, end_miles, fuel_gallons)
    
    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    lp100k = lp100k_from_mpg(mpg)

    # Round the miles per gallon to one digit after the decimal.
    mpg = round(mpg, 1)
    # Round the liters per 100 km to two digits after the decimal.
    lp100k = round(lp100k, 2)

    # Display the results for the user to see.
    print(f"mpg: {mpg}, lp100k: {lp100k}")

# run program
main()