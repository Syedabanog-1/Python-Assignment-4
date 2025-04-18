# random_numbers.py
# Author: Syeda Gulzar Bano - Age: 23 - GIAIC Student

import random

print("🎲 Random Number Generator")
low = int(input("Enter lower bound: "))
high = int(input("Enter upper bound: "))
how_many = int(input("How many numbers to generate? "))

print(f"Generating {how_many} numbers between {low} and {high}:")
for _ in range(how_many):
    print(random.randint(low, high))