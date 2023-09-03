from abc import ABCMeta, abstractmethod


class Transmitter(metaclass=ABCMeta):
    def _voice_record(self):
        print('Rec voice')

    def _simpling(self):
        pass

    def _digitization(self):
        pass

    @abstractmethod
    def _modulation(self):
        pass

    def transmission(self):
        print('Transmission on radio wave')

    def process_start(self):
        self._voice_record()
        self._simpling()
        self._digitization()
        self._modulation()
        self.transmission()


class AnalogTransmitter(Transmitter):
    def _modulation(self):
        print('Modulation analog signal')


class DigitalTransmitter(Transmitter):
    def _simpling(self):
        print('Discretion recorded fragment')

    def _digitization(self):
        print('Digitization')

    def _modulation(self):
        print('Modulating digital signal')


if __name__ == '__main__':
    analog_transmiter = AnalogTransmitter()
    analog_transmiter.process_start()

    digital = DigitalTransmitter()
    digital.process_start()