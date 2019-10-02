


def foo(n):
    """
    Returnprints out numbers n to 1
    """
    #iterative:

    # while n > 0:
    #     print(n)
    #     n -= 1

    # recursive:

    print(n)
    if n>1:
        foo(n-1)

# foo(10)



######## fibonacci #################


# fib(0) = 0
# fib(1) = 1


# fib(2) = fib(1) + fib(0)
# fib(3) = fib(2) + fib(1)
# fib(4) = fib(3) + fib(2)

# fib(n) = fib(n-1) + fib(n-2)



def fib(n):
    if n < 0:
        print("ERROR")
        return 0
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

# print(fib(35))



############### with cache #########

cache = {0:0, 1:1}

def fib_cache(n):
    if n < 0:
        print("ERROR")
        return 0
        
    elif n in cache:
        # else check if the result is in the cache
        # if it is, return the cache result
        return cache[n]

    else:
        # else, run the calculation and store result in the cache
        result = fib(n - 1) + fib(n - 2)
        cache[n] = result
        return result

def add_and_print(n):
    n+= 1
    print(n)


x=100
add_and_print(x)

print(x)
