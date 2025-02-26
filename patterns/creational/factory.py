"""A Factory is an object for creating other objects.
"""
from abc import ABC, abstractmethod


class Localizer(ABC):
    @abstractmethod
    def localize(self, msg):
        pass


class EnglishLocalizer(Localizer):
    def __init__(self) -> None:
        self.translations = {"dog": "dog", "cat": "cat"}

    def localize(self, msg):
        return self.translations[msg]


class GreekLocalizer(Localizer):
    def __init__(self) -> None:
        self.translations = {"dog": "σκύλος", "cat": "γάτα"}

    def localize(self, msg):
        return self.translations[msg]


def localizer_factory(lang):
    """factory"""
    localizers = {
        'english': EnglishLocalizer,
        'greek': GreekLocalizer,
    }
    return localizers[lang]()

if __name__ == "__main__":
    localizer_english = localizer_factory('english')
    localizer_greek = localizer_factory('greek')
    print(localizer_english.localize('dog'))
    print(localizer_greek.localize('dog'))
