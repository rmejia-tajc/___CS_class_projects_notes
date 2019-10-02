
# recursion - function that calls itself


# factorial(5) -> 5*4*3*2*1 = 120
# factorial(4) ->   4*3*2*1 = 24
# factorial(3) ->     3*2*1 = 6
# factorial(2) ->       2*1 = 2
# factorial(1) ->         1 = 1

# factorial(5) -> 5 * factorial(4)





### iterative

def factorial(num):
    total = 1
    for n in range(2, num + 1):
        total *= n
    return total


### recursive

def fatorial(num):
    # print(num)
    if num <= 1:
        return 1
    return num * factorial(num - 1)


########### quick sort

def partition(data):
    left = []
    pivot = data[0]
    right = []
    for v in data[1:]:
        if v <= pivot:
            left.append(v)
        else:
            right.append(v)
    return left, pivot, right
def quicksort(data):
    if data == []:
        return data
    left, pivot, right = partition(data)
    return quicksort(left) + [pivot] + quicksort(right)







def quick_sort_A( books, low, high ):
    print(books)
    # base case
    if low >= high:
        return books
        # recursive case
    else:
        # divide
        pivot_index = low
        # for each element in subarray
        for i in range(low, high):
            if books[i] < books[pivot_index]:
                # double swap to move smaller elements to correct index
                # move current element to the right of pivot
                temp = books[pivot_index+1]
                books[pivot_index+1] = books[i]
                books[i] = temp
                # swap pivot with element on its right
                temp = books[pivot_index]
                books[pivot_index] = books[pivot_index+1]
                books[pivot_index+1] = temp
                pivot_index += 1
        # conquer
        # Quick Sort everything left of the pivot
        books = quick_sort_A(books, low, pivot_index)
        # Quick Sort everything right of the pivot
        books = quick_sort_A(books, pivot_index+1, high)
        return books


