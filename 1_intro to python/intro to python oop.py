"""
Spec: write a program that holds product and department information about a
store.  User should be able to enter a department number and get a list of
products in that department.
Product info is:
    * quantity, int
    * price
    * dept
    * name, string
You'll get product list later.
Department info:
    * name, string
Questions:
* How many products?
Under 1,000,000
* How to present data
Standard output
* How many customers?
Under 100 requests per second.
* Vendor accounts?
No.
* Can depts change?
No.
* Can a product be in more than one department?
Yes.
* Which depts hold what?
TBD
* How is info added?
Out of scope
* Product location?
No
* Sale info?
No
"""

class Store:
    def __init__(self, name, depts):    # Constructor  # self == this (in javascript)
        self.name = name # "has-a" relationship
        self.depts = depts

    def __str__(self):
        return f"Store: {self.name}"

    def __repr__(self):
        return f'Store("' + self.name + '")'
        
    # def __repr__(self):
    #     return f'Store({repr(self.name)})'

class Dept:
    def __init__(self, name):    # Constructor  # self == this (in javascript)
        self.name = name

    def __str__(self):
        return f"Dept: {self.name}"

    def __repr__(self):
        return f'Dept("' + self.name + '")'
        
    # def __repr__(self):
    #     return f'Dept({repr(self.name)})'

depts = [
    Dept("Department 1"),
    Dept("Department 2"),
    Dept("Department 3"),
]


print("A")
my_store = Store("Rudy's store", depts)    # Create a new Store object
print(my_store)
print(repr(my_store))
my_store.name = "another store"
print(repr(my_store))
print("B")



print(depts)
print(repr(depts))