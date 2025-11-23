#oops

# 1. Encapsulation
# 2. Abstraction
# 3. Inheritance
# 4. Polymorphism



#in dog.py

class Dog:
    legs: int = 4
    ears: int = 2
    type: str = "Goldendoodle"
    age: int = 5
    color: str = "Yellow"
    
#in main.py

from Dog import *

dog = Dog()    
dog.legs
dog.ears
dog.type
dog.age
dog.color

