
class TextTag:
    """Represents a base text tag"""

    def __init__(self, text: str) -> None:
        self._text = text

    def render(self) -> str:
        return self._text


class BoldWrapper(TextTag):
    """wrapper extends base class and also keep a composition of its object. Wrapper implements all it's functionality"""

    def __init__(self, wrapped: TextTag) -> None:
        self._wrapped = wrapped

    def render(self) -> str:
        return f"<b>{self._wrapped.render()}</b>"


if __name__ == "__main__":
     simple_hello = TextTag("hello, world!")
     special_hello = BoldWrapper(simple_hello)

     print("before:", simple_hello.render())

     print("after:", special_hello.render())
