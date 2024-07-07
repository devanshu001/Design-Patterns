import abc


class PricingStrategyInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_price(self, ticket):
        pass
