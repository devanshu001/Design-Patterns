from problems.parkingLot.vehicle.Vehicle import Vehicle
from problems.parkingLot.spot import Spot
from datetime import datetime


class Ticket:

    def __init__(self, vehicle: Vehicle, spot: Spot):
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = datetime.now()
