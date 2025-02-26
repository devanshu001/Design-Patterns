from .PricingStrategy import PricingStrategyInterface
from datetime import datetime
from math import ceil


class HourlyPricingStrategy(PricingStrategyInterface):
    price = 50

    def get_price(self, ticket):
        hours = ceil((datetime.now() - ticket.entry_time).seconds / (60 * 60))
        hours = 1 if hours == 0 else hours
        return hours * HourlyPricingStrategy.price
