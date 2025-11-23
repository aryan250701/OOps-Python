import datetime
  ## Python Getter and Setter Methods
class User:
    def __init__(self, name):
        self.name = name
        pass
    def set_email(self, new_email):
        if "@" not in new_email:
            raise ValueError("Invalid email address")
        else:
            self.email = new_email
            print("Email updated successfully")
    def setPassword(self, new_password):
        if len(new_password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        else:
            self.__password = new_password  # private attribute
            print("Password updated successfully")
    
user_1 = User("john_doe")
user_1.set_email("aryan.d@tcs.com")
print(user_1.email)
    
    
    ##Python Properties
    
class Rectangle:
    def __init__(self, name, width, height):
        self.name = name
        self._width = width
        self.height = height
        pass
    @property
    def getEmail(self):
        print(f"Accessing width at { datetime.datetime.now() }")
        return self._width
    def setWidth(self, new_width):
        if new_width <= 0:
            raise ValueError("Width must be positive")
        print(f"Updating width at { datetime.datetime.now() } to {new_width}")
        self._width = new_width

rect_1 = Rectangle("MyRectangle", 10, 5)
print(rect_1.getEmail)  # Accessing width using the property
rect_1.setWidth(15)  # Updating width using the setter method


class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self._owner = owner
        pass
    ##THIS PYTHON METHOD IS A ATTRIBUTE NOW
    @property
    def owner(self):
        return f"The owner of {self.name} is {self._owner}"
    
    @owner.setter
    def owner(self, new_owner):
        self._owner = new_owner
        print(f"the owner of {self.name} has been changed to {self._owner}") 
    
    
    ##THIS IS A PYTHON METHOD
    def bark(self):
        print(f"{self.name} said woof woof")

dog = Dog("Buddy", "Golden Retriever", "Alice")
print(dog.owner)  # Accessing owner using the property
dog.owner = "Bob"  # Updating owner using the setter method
print(dog.owner)  # Accessing updated owner using the property