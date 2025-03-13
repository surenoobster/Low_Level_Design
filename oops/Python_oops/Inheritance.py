class Animal:
    def eat(self):
        print("Animal is eating...")

class Dog(Animal):
    def bark(self):
        print("Dog is barking...")

my_dog = Dog()
my_dog.eat()  # Inherited from Animal
my_dog.bark()
