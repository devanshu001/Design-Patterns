from parkingLot.parkingManager import ParkingManagerFactory, ParkingManager
from parkingLot.vehicle.Vehicle import Vehicle
from parkingLot.Ticket import Ticket


class EntryGate:
    def __init__(self):
        self._parking_manager = None

    @property
    def parking_manager(self) -> ParkingManager:
        return self._parking_manager

    @parking_manager.setter
    def parking_manager(self, parking_manager: ParkingManager):
        self._parking_manager = parking_manager

    def generate_ticket(self, vehicle: Vehicle):
        self.parking_manager = ParkingManagerFactory.get_manager(vehicle.vehicle_type)
        print (self.parking_manager.spots)
        try:
            spot = self.parking_manager.find_empty_spot()
            spot.fill_spot(vehicle.vehicle_no)
            return Ticket(vehicle, spot)

        except  Exception as e:
            print(e)
            print('No empty spot found')
