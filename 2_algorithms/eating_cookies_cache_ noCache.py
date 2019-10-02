# counting steps



#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution


################  with cache #################################

def eating_cookies(n, cache=None):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            cache = { i: 0 for i in range(n+1)}
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
        return cache[n]


################  with no cache #################################


def eating_cookies2(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


print(eating_cookies(1))
print(eating_cookies(2))
print(eating_cookies(3))
print(eating_cookies(4))
print(eating_cookies(5))
print(eating_cookies(6))
print(eating_cookies(7))
print(eating_cookies(8))



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')



"""

0
---------
0


1
---------
1


2
---------
1,1
2


3
---------
1,1,1
1,2
2,1
3


4
---------
1,1,1,1
1,1,2
1,2,1
2,1,1
2,2
1,3
3,1


1,1,1,1,1
  1,1,1,2
    1,1,3
      2,3

"""


# look at the ways to eat (n-1) cookies, then eat one more
# look at the ways to eat (n-2) cookies, then eat 2 at once
# look at the ways to eat (n-3) cookies, then eat 3 at once