class Dog:
    #Class is analogus to a blueprint (eg String, List, Dictionary etc)
    # Method to make the dog bark
    # Methods are functions defined inside a class eg(.upper(), .append() etc)
    def __init__(self, name:str, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
        pass
    
    def bark(self):
        print("woof woof")
 
class Owner:
    def __init__(self,name, address, contact_number):
        self.name = name
        self.address = address
        ## these names can be different from the parameter names
        self.phone_number = contact_number
        pass
    
# dog1 = Dog()
# dog1.bark()

#Equivalent to String
name = "Aryan"
# this is basically short hand notation for 
# name = str("Aryan")
# print(name.upper())  # Calling the .upper() method on the string object 'name'

# Summary

# User-defined class → you call it like Dog()s

# Built-in class → Python has literal shortcuts, but they still create objects.

# Once we add def __init__ method to the class, we need to provide arguments while creating an object of that class.

#hence dog_1 = Dog() will throw an error now

# dog_1 = Dog("Buddy", "Golden Retriever")
# dog_1.bark()  # Calling the bark method on the dog_1 object
# print(dog_1.name)  # Accessing the name attribute of dog_1

owner_1 = Owner("Alice", "123 Main St", "555-1234")
dog_1 = Dog(1, "Golden Retriever", owner_1)
print(dog_1.owner.name)  # Accessing the owner's name through the dog_1 object

## Making an Object private
## Method _1: Single underscore prefix
## Method _2: Double underscore prefix
class Cat:
    def __init__(self, cat_name, age, password, secret_code):
        self.cat_name = cat_name
        self.age = age
        self._password = password  # single underscore prefix (can still be accessed but indicates it's private)
        self.__secret_code = secret_code  # double underscore prefix (makes it harder to access from outside)
        pass
    
cat_1 = Cat("snowy",3,"1234","ABC")
print(cat_1.cat_name)  # Accessing public attribute
print(cat_1._password)  # Accessing "private" attribute with single underscore (not recommended)
# print(cat_1.__secret_code)  # This will raise an AttributeError