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
    #list = [5, 4,3,2,1] 
    print("List:", list)
    result = max_min(list)
    print("Minimum value in the list:", result)
    #print(f"Start at index 2: {list[2:]}")#start at index 2 and go to the end of the list
    #print(f"Stop at index 3: {list[:3]}")#start at the beginning of the list and go to index 3 (exclusive)
    #list_a = list[1]
    #print("List_a:", list_a)   

get_value()