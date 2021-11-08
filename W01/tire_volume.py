import math

pi = math.pi

# width of tire (in milimeters)
w = float(input("width of tire (mm): "))
# aspect ratio of the tire
a = float(input("aspect ratio of tire: "))
# diameter of the wheel (in inches)
d = float(input("diameter of the wheel (in): "))

# program to run
v = (pi * w ** 2 * a * (w * a + 2540 * d)) / 10000000000
print(f"The volume of the tire is {round(v, 2)} liters")