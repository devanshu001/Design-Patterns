""" This pattern is used when new objects are needed with different attribute values
instead of creating subclasses for all different valued object
Useful when object instantiation is difficult"""

class Prototype:
    def __init__(self,  **attributes):
        self.__dict__.update(attributes)

    def clone(self, **attributes):
        # new clone obj with current obj attributes
        clone_obj =self.__class__(**self.__dict__)
        # apply new attributes to new object
        clone_obj.__dict__.update(attributes)
        return clone_obj

class Shape(Prototype):
    def __init__(self, **attributes):
        super().__init__(**attributes)

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length=length, width=width)
        self.length = length
        self.width = width

    def area(self):
        return self.length* self.width

# this class holds the prototype objects
class PrototypeDispatcher:
    def __init__(self):
        self._objects = {}

    def get_objects(self) :
        """Get all objects"""
        return self._objects

    def register_object(self, name: str, obj: Prototype):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name: str):
        """Unregister an object"""
        del self._objects[name]


if __name__ == '__main__':
    rec=Rectangle(length=100, width=80)
    rec2=rec.clone(length=120)
    print(rec.area())
    print(rec2.area())
