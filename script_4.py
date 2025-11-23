# Static Atrtibutes and Methods
class Dog:
    ## Static Attribute
    species = "Canis familiaris"  # Static attribute shared by all instances of Dog
    
    def __init__(self, name, breed, owner):
        ## Instance Attributes
        self.name = name
        self.breed = breed
        self.owner = owner
        pass
    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, newName):
        self.name = newName
        print(f"Owner updated to {self.name}")
    ## Static Method
    @staticmethod
    def info():
        return "Dogs are domesticated mammals, not natural wild animals."
    
    
dog1 = Dog("Buddy", "Golden Retriever", "Alice")
dog2 = Dog("Max", "Beagle", "Bob")
## Accessing the instanced attributes
print(dog1.name)
print(dog2.name)
dog1.name = "Charlie"

## Accessing the static attribute
print(Dog.species)
print(dog1.species)
print(dog2.species)
dog1.species = "Changed Species"
print(dog1.species)  # This will print "Changed Species"
print(dog2.species)  # This will still print "Canis familiaris"

## Changed for the every variable

class BankAccount:
    MIN_BALANCE = 100  # Static attribute representing minimum balance
    def  __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        pass
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")
    
    @staticmethod
    def bank_policy():
        return f"Minimum balance required is {BankAccount.MIN_BALANCE}"
    
    @staticmethod
    def calculate_interest(balance, rate, time):
        return balance * rate * time / 100
    