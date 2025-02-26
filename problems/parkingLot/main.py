# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from problems.parkingLot.parkingManager import TwoWheelerParkingManager, FourWheelerParkingManager
from problems.parkingLot.EntryGate import EntryGate
from problems.parkingLot.vehicle.Vehicle import Vehicle, VehicleType
from problems.parkingLot.ExitGate import ExitGate
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('ParkingLot')

    TwoWheelerParkingManager.add_spot()
    TwoWheelerParkingManager.add_spot()
    FourWheelerParkingManager.add_spot()
    entry_gate=EntryGate()
    exit_gate=ExitGate()
    vehicle1=Vehicle('001',VehicleType.FourWheeler)
    vehicle2=Vehicle('002', VehicleType.FourWheeler)
    ticket1=entry_gate.generate_ticket(vehicle1)
    ticket2=entry_gate.generate_ticket(vehicle2)


    exit_gate.charge_ticket(ticket1)
    ticket2 = entry_gate.generate_ticket(vehicle2)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

