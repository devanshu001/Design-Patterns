from parkingLot.vehicle.Vehicle import Vehicle
from parkingLot.spot import Spot
from datetime import datetime
from parkingLot.parkingManager import ParkingManagerFactory


class Ticket:

    def __init__(self, vehicle: Vehicle, spot: Spot):
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = datetime.now()
