from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Dog says: Woof Woof!")

my_dog = Dog()
my_dog.make_sound()
