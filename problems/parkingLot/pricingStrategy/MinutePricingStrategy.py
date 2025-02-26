from .PricingStrategy import PricingStrategyInterface
from datetime import datetime


class MinutePricingStrategy(PricingStrategyInterface):
    price = 2

    def get_price(self, ticket):
        minutes = (datetime.now() - ticket.entry_time).minute
        return minutes * MinutePricingStrategy.price
