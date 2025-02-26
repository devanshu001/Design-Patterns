from problems.parkingLot.spot import Spot
from abc import ABC, abstractmethod
from problems.parkingLot.costComputation.CostCompute import TwoWheelerCostCompute, FourWheelerCostCompute
from problems.parkingLot.vehicle.VehicleEnum import VehicleType


class ParkingManager(ABC):

    @classmethod
    @abstractmethod
    def add_spot(cls):
        pass

    @classmethod
    @abstractmethod
    def find_empty_spot(cls):
        pass


class TwoWheelerParkingManager(ParkingManager):
    spots = []

    def __init__(self):
        self.cost_compute = TwoWheelerCostCompute()

    @classmethod
    def add_spot(cls):
        cls.spots.append(Spot(spot_type=VehicleType.TwoWheeler))

    @classmethod
    def find_empty_spot(cls):
        print (cls.spots)
        for spot in cls.spots:
            if spot.empty: return spot
        raise Exception("Parking full")


class FourWheelerParkingManager(ParkingManager):
    spots = []

    def __init__(self):
        self.cost_compute = FourWheelerCostCompute()

    @classmethod
    def add_spot(cls):
        cls.spots.append(Spot(spot_type=VehicleType.FourWheeler))

    @classmethod
    def find_empty_spot(cls):
        for spot in cls.spots:
            if spot.empty: return spot
        raise Exception("Parking full")


class ParkingManagerFactory:
    @staticmethod
    def get_manager(vehicle_type: VehicleType):
        if vehicle_type.value == VehicleType.FourWheeler.value:
            return FourWheelerParkingManager()
        elif vehicle_type.value == VehicleType.TwoWheeler.value:
            return TwoWheelerParkingManager()
