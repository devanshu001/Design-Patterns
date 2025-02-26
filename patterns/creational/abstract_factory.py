from abc import ABC, abstractmethod

"""The idea is to abstract the creation of objects depending on business
logic, platform choice, etc. (here pet)"""
class Pet(ABC):

    @abstractmethod
    def make_noise(self):
        pass

    @abstractmethod
    def walk_speed(self):
        pass

class Dog(Pet):
    def make_noise(self):
        print('woof')

    def walk_speed(self):
        print('10')

class Cat(Pet):
    def make_noise(self):
        print('meow')

    def walk_speed(self):
        print('5')

# receives pet class
class PetShop():
    def __init__(self, pet_class:Pet):
        """pet_factory is our abstract factory.  We can set it at will.
        pet factory should be callable or an class
        """
        self.pet_factory = pet_class

    def buy_pet(self):
        return self.pet_factory()


if __name__== '__main__':
    dog1=PetShop(Dog).buy_pet()
    dog1.make_noise()

    cat1=PetShop(Cat).buy_pet()
    cat1.make_noise()
