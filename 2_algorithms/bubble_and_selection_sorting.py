

########### bubble sort #########


import random

arr = list(range(10))
random.shuffle(arr)



def bubble_sort(arr):
    has_swapped = True
    #when no swaps have occurred, return
    while has_swapped:
        print(arr)
        has_swapped = False
        #walk through each elements in the array
        for i in range(0, len(arr) - 1):
            #if the element is out of order from the neighbor...
            if arr[i] > arr[i+1]:
                #swap
                arr[i], arr[i+1] = arr[i+1], arr[i]
                has_swapped = True
    return arr





############ selection sort #########


# l = [1,3,5,6,2,8,4]




# def selection_sort(arr):
#     #divide the array into sorted and unsorted
#     #loop through each element
#     for i in range(len(arr)-1):
#         current_index = i
#         smallest_index = current_index
#         #find the smallest element in the unsorted list
#         for j in range(current_index, len(arr)):
#     #put the smallest element at the end of the sorted list
#     #swap the first element of unsorted with the smallest element







##### from instructor

def insertion_sort(list):
    # Separate the first element from the rest of the array.
    # Think about it as a sorted list of one element.
    # For all other indices, beginning with [1]:
    for i in range(1, len(list)):
        print(arr)
        # a. Copy the item at that index into a temp variable
        temp = list[i]
        # b. Iterate to the left until you find the correct index in the "sorted"
        # part of the array at which this element should be inserted
        j = i
        while j > 0 and temp < list[j - 1]:
            # Shift items over to the right as you iterate
            list[j] = list[j - 1]
            j -= 1
        # c. When the correct index is found, copy temp into this position
        list[j] = temp
    return list
import random
arr = list(range(20))
random.shuffle(arr)
def bubble_sort(arr):
    has_swapped = True
    # When no swaps have occurred, return
    while has_swapped:
        has_swapped = False
        # Walk through each element in the array
        for i in range(0, len(arr) - 1):
            # If the element is out of order from the neighbor...
            if arr[i] > arr[i+1]:
                # Swap
                arr[i], arr[i+1] = arr[i+1], arr[i]
                has_swapped = True
    return arr
smallest_value = 5
l = [1, 2, 3, 4, 5, 6, 8]
l = [1, 2,        3, 4, 5]
def selection_sort(arr):
    # Divide the array into sorted and unsorted
    # loop through each element
    for i in range(len(arr) - 1):
        print(arr)
        current_index = i
        smallest_index = current_index
        # Find the smallest element in the unsorted
        for j in range(current_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # Put the smallest element at the end of the sorted
        # Swap the first element of unsorted with the smallest element
        arr[smallest_index], arr[current_index] = arr[current_index], arr[smallest_index]
    return arr
