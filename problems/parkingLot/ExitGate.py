from .parkingManager import ParkingManagerFactory, ParkingManager
from .vehicle.Vehicle import Vehicle
from .Ticket import Ticket
from .costComputation.CostCompute import CostComputeFactory


class ExitGate:
    @staticmethod
    def charge_ticket( ticket: Ticket):
        cost_compute = CostComputeFactory.get_manager(ticket.vehicle.vehicle_type)
        price = cost_compute.calculate_price(ticket)
        ticket.spot.empty_spot()
        return price
