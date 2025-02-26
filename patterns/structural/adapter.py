
class Dog:
    def __init__(self) -> None:
        self.name = "Dog"

    def bark(self) -> str:
        return "woof!"


class Human:
    def __init__(self) -> None:
        self.name = "Human"

    def speak(self) -> str:
        return "'hello'"

class Adapter:
    def __init__(self,obj, **adapted_methods) -> None:
        self.obj = obj
        obj.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object."""
        return getattr(self.obj, attr)

    def original_dict(self):
        """Print original object dict."""
        return self.obj.__dict__

# alternatively we can create a adapter class specific for modifying a class behaviour
class DogAdapter(Dog):
    def __init__(self) -> None:
        super().__init__()

    def make_noise(self):
        return self.bark()

if __name__ == '__main__':
    human=Human()
    dog=Dog()
    adapted_dog=Adapter(dog, make_noise=dog.bark)
    adapted_human=Adapter(human, make_noise=human.speak)
    print(adapted_dog.make_noise())
    print(adapted_human.make_noise())

    print(DogAdapter().make_noise())