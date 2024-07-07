from ..pricingStrategy import PricingStrategy
from ..pricingStrategy.MinutePricingStrategy import MinutePricingStrategy
from ..pricingStrategy.HourlyPricingStrategy import HourlyPricingStrategy
from ..vehicle.VehicleEnum import VehicleType


class CostCompute:

    def __init__(self, strategy: PricingStrategy):
        self._strategy = strategy

    @property
    def strategy(self): return self._strategy

    @strategy.setter
    def strategy(self, strategy: PricingStrategy):
        self._strategy = strategy

    def calculate_price(self, ticket):
        self._strategy.get_price(ticket)


class TwoWheelerCostCompute(CostCompute):
    def __init__(self):
        super().__init__(MinutePricingStrategy())


class FourWheelerCostCompute(CostCompute):
    def __init__(self):
        super().__init__(HourlyPricingStrategy())


class CostComputeFactory:
    @staticmethod
    def get_manager(vehicle_type: VehicleType):
        if vehicle_type.value == VehicleType.FourWheeler.value:
            return FourWheelerCostCompute()
        elif vehicle_type.value == VehicleType.TwoWheeler.value:
            return TwoWheelerCostCompute()
