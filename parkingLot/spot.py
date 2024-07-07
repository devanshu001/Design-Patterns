from .vehicle.VehicleEnum import VehicleType
from uuid import UUID


class Spot:
    def __init__(self, spot_type: VehicleType):
        self.id = UUID(int=True)
        self.empty = True
        self.spot_type = spot_type
        self.vehicle_no = None

    def fill_spot(self, vehicle_no):
        self.vehicle_no = vehicle_no
        self.empty = False
        print (f'parked {vehicle_no}, {self.spot_type} at {self.id}')

    def empty_spot(self):
        self.empty = True
        self.vehicle_no = None
        print(f'unparked {self.vehicle_no}, {self.spot_type} at {self.id}')
