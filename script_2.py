class Dog:
    #Class is analogus to a blueprint (eg String, List, Dictionary etc)
    # Method to make the dog bark
    # Methods are functions defined inside a class eg(.upper(), .append() etc)
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        pass
    
    def bark(self):
        print("woof woof")
    
# dog1 = Dog()
# dog1.bark()

#Equivalent to String
name = "Aryan"
# this is basically short hand notation for 
# name = str("Aryan")
print(name.upper())  # Calling the .upper() method on the string object 'name'

# Summary

# User-defined class → you call it like Dog()s

# Built-in class → Python has literal shortcuts, but they still create objects.

# Once we add def __init__ method to the class, we need to provide arguments while creating an object of that class.

#hence dog_1 = Dog() will throw an error now

dog_1 = Dog("Buddy", "Golden Retriever")
dog_1.bark()  # Calling the bark method on the dog_1 object
print(dog_1.name)  # Accessing the name attribute of dog_1