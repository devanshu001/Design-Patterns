from .VehicleEnum import VehicleType


class Vehicle:
    def __init__(self, vehicle_no, vehicle_type: VehicleType):
        self.vehicle_no = vehicle_no
        self.vehicle_type = vehicle_type
