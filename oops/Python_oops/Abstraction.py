from abc import ABC, abstractmethod

class Car(ABC):  # Abstract class
    def __init__(self, brand):
        self.brand = brand  # Common attribute

    @abstractmethod
    def start_engine(self):
        """Abstract method that forces subclasses to implement it"""
        pass
    
    def display_brand(self):
        """Concrete method that can be called directly"""
        print(f"This car is a {self.brand}.")

class Tesla(Car):
    def start_engine(self):
        print(f"{self.brand}: Electric engine started silently with a button press.")

class BMW(Car):
    def start_engine(self):
        print(f"{self.brand}: Petrol engine roars to life with a key start.")

# Creating objects of the subclasses
my_tesla = Tesla("Tesla Model S")
my_bmw = BMW("BMW M5")

# Calling the common method
my_tesla.display_brand()  
my_tesla.start_engine()

my_bmw.display_brand()
my_bmw.start_engine()




#Or let's take display_brand also as abstract_method

from abc import ABC, abstractmethod

class Car(ABC):  # Abstract class
    def __init__(self, brand):
        self.brand = brand  # Common attribute

    @abstractmethod
    def start_engine(self):
        """Abstract method that forces subclasses to implement it"""
        pass

    @abstractmethod
    def display_brand(self):
        """Abstract method - must be implemented in subclasses"""
        pass

class Tesla(Car):
    def start_engine(self):
        print(f"{self.brand}: Electric engine started silently with a button press.")

    def display_brand(self):
        print(f"This is a Tesla: {self.brand}")

class BMW(Car):
    def start_engine(self):
        print(f"{self.brand}: Petrol engine roars to life with a key start.")

    def display_brand(self):
        print(f"This is a BMW: {self.brand}")

# Creating objects of the subclasses
my_tesla = Tesla("Tesla Model S")
my_bmw = BMW("BMW M5")

# Calling methods
my_tesla.display_brand()  
my_tesla.start_engine()

my_bmw.display_brand()
my_bmw.start_engine()
