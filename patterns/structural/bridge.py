from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def volume_up(self):
        pass
    @abstractmethod
    def volume_down(self):
        pass

class TV(Device):
    def __init__(self):
        super().__init__()
    def volume_up(self):
        print('TV volume up')

    def volume_down(self):
        print('TV volume down')


class Radio(Device):
    def __init__(self):
        super().__init__()

    def volume_up(self):
        print('Radio volume up')

    def volume_down(self):
        print('Radio volume down')

class UniversalRemote:
    def __init__(self, device):
        # handles abstraction by composition(keeping an object of diff class)
        # acts as a bridge between remote and devices implementation
        self.device = device

    def volume_up(self):
        self.device.volume_up()

    def volume_down(self):
        self.device.volume_down()


if __name__ == '__main__':
    radio_remote = UniversalRemote(Radio())
    radio_remote.volume_up()
    radio_remote.volume_down()
    tv_remote = UniversalRemote(TV())
    tv_remote.volume_up()



