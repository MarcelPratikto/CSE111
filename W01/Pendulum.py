"""
The time in seconds that a pendulum takes to swing
back and forth once is given by this formula:
             ____
            / n
    t = 2π / ----
          √  9.81

where t is the time in seconds,
π is PI the ratio of the circumference divided by
    the diameter of a circle (use math.pi), and
n is the length of the pendulum in meters.

Write a program that prompts a user to enter the length of a
pendulum in meters and then computes and prints the time in
seconds that it takes for that pendulum to swing back and forth.
"""

import math

pi = math.pi

n = float(input("Length of pendulum (in meters): ")) # length of pendulum in meters

t = 2 * pi * math.sqrt(n / 9.81)

print(f"The time it takes for the pendulum to swing back and forth is {t:.2f} seconds")