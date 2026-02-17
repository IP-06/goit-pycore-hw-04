# Task 2
import random

min = int(input("Enter min: "))
max = int(input("Enter max: "))
quantity = int(input("Enter score number: "))

def get_numbers_tiket(mi2n, max, quantity):
    numbers_tiket=[]
    if min > 0 and max < 1000 and min < max and  max - min >= quantity:
        numbers_tiket = random.sample(range(min, max), quantity)
    return sorted(numbers_tiket)
print(get_numbers_tiket(min, max, quantity))