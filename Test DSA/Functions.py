import random

def max_min(numbers): 
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
            print("Minimum:", minimum)
    return minimum

def get_value(): 
    list = random.sample(range(1, 100), 10)
    list = [5, 4,3,2,1] 
    print("List:", list)
    max_min(list)
