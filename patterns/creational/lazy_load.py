from functools import update_wrapper

class lazy_property:
    def __init__(self, function):
        self.function = function
        # updates __doc__ and __name__ of the function instead of the wrapper lazy_property.
        update_wrapper(self, function)

    def __get__(self, obj, type_):
        if obj is None:
            return self
        # function called when accessed and added to the obj attribute(__dict__)
        val = self.function(obj)
        obj.__dict__[self.function.__name__] = val
        return val


class Person:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    @lazy_property
    def relatives(self):
        # Get all relatives, let's assume that it costs much time.
        relatives = "Many relatives."
        return relatives

if __name__ == '__main__':
    ram = Person('ram', 'coder')
    print(ram.__dict__.items())
    ram.relatives
    print(ram.__dict__.items())


