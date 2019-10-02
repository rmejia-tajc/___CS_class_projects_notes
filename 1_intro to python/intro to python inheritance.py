# Inheritance in OOP

class Animal: # "Base class"

    def __init__(self, name):
        self.name = name
    
    def call(self):
        print(f"{self.name}: generic animal sound")

class Vertebrate(Animal): # Vertebrate is an Animal, "is-a" relationship
    pass # has no effect. Python requires an indent inside classes or it breaks

    def call(self): # Override the parent (aka the "super") class's call method
        print(f"{self.name}: generic vertebrate sound")

class Mammal(Vertebrate):
    pass

class Cat(Mammal):

    def __init__(self, name, evil):
        # self.name = name # wrong - instead call super() to inherit parent ?properties?
        super().__init__(name)
        self.evil = evil

    def call(self):
        print(f'{self.name} ({"evil" if self.evil else "not evil"}): Meow')

class Invertebrate(Animal): # Invertebrate is an Animal, "is-a" relationship
    pass # has no effect. Python requires an indent inside classes or it breaks

# a = Animal()
# a.call()

# v = Vertebrate()
# v.call()

# iv = Invertebrate()
# iv.call()

animals = [
    Animal("animal 1"),
    Vertebrate("vert 1"),
    Invertebrate("invert 1"),
    Cat("cat 1", False),
    Mammal("mammal 1"),
]

for a in animals:
    a.call()