#numbers = [1, 2, 3, 4, 5]
#print("Created list:", numbers)
#for i in range(4):
    #if numbers[i] < numbers[i + 1]:
       # print(f" {numbers[i]} is smaller than {numbers[i + 1]}")

#def convert_tuple_list():
    #"""Convert between tuple and list"""
    #numbers = (1, 2, 3)

    #numbers_list = list(numbers)
    #print("Tuple to list:", numbers_list)

    #numbers_list.append(4)

    #numbers_tuple = tuple(numbers_list)
    #print("List back to tuple:", numbers_tuple)

#convert_tuple_list()

#def remove_elements():
    #"""Remove elements from a list"""
    #numbers = [1, 2, 3, 4, 5]
    #print("List before removal:", numbers)
    #numbers.remove(3)  # remove specific value
    #print("After remove:", numbers)

    #popped = numbers.pop()  # remove last element
    #print("Popped element:", popped)
    #print("After pop:", numbers)

#remove_elements()

#def list_slicing():
    #"""Demonstrate slicing"""
    #numbers = [1, 2, 3, 4, 5]

    #print("First 3 elements:", numbers[:3])
    #print("Last 2 elements:", numbers[-2:])
    #print("Reversed list:", numbers[::-1])

#list_slicing()  

def check_membership():
    """Check if item exists in list"""
    fruits = ["apple", "banana", "cherry"]

    print("Is apple in list?", "apple" in fruits)
    print("Is mango in list?", "mango" in fruits)
    print("Is cherry in list?", "cherry" in fruits)

check_membership()