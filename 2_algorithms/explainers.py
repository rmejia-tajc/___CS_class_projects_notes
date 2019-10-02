
####### binary search

####### log base 2

# 2 ** 1 = 2
# log2(2) = 1

# 2 ** 2 = 4
# log2(4) = 2

# 2 ** 3 = 8
# log2(8) = 3

# 2 ** 10 = 1024
# log2(1024) = 10

# 1024
# 512
# 256
# 128
# 64
# 32
# 16
# 8
# 4
# 2
# 1



########## insertion sorting



l = [ 5, 3, 1, 6 ]

i = 1  # everything left of  i  is sorted
temp = 3 # this is the number that we want to insert in the sorted list on the left
j = 0 # j keeps track of the sorted array’s length (on the left)


def insertion_sort(l):
# Separate the first element from the rest of the array. Think about it as a sorted list of one element.

    # For all other indices, beginning with [1]:
    for i in range( 1, len(l)):
    # a. Copy the item at that index into a temp variable
        temp = list[i]
    # b. Iterate to the left until you find the correct index in the "sorted" part of the array at which this element should be inserted
        j = i
        while j > 0 and temp < list[ j - 1 ]:
            # Shift items over to the right as you iterate
            list[j] = list [ j - 1 ]
            j -= 1
        # c. When the correct index is found, copy temp into this position
        list[j] = temp

    return list


# O(n*
    
    


