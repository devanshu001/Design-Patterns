"""The Borg pattern (also known as the Monostate pattern) is a way to
implement singleton behavior, but instead of having only one instance
of a class, there are multiple instances that share the same state."""

class Borg:
    _shared_state = {}
    def __init__(self):

        """
        in Python, instance attributes are stored in a attribute dictionary called __dict__.
        Borg pattern modifies each instances dict at init so that all instances have the same dictionary
        """
        self.__dict__ = self._shared_state


class Database(Borg):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def __str__(self) -> str:
        return self.url

if __name__== '__main__':
    d1=Database('abc')
    d2=Database('pqr')
    print(d1)
    print(d2)
