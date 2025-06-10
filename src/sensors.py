from abc import ABC, abstractmethod
import random
import string

class Sensors(ABC):
    def __init__(self, identification, is_active, car_park):
        """
        This function is the initialiser for the Sensors class
        :param identification:
        :param is_active:
        :param car_park:
        """
        self.identification = identification
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        return f"Sensor {self.identification}."

    @abstractmethod
    def update_car_park(self, plate):
        pass

    def generate_random_plate(self):
        random_plate_numbers = format(random.randint(0, 999), '03d')
        raw_random_plate_letters = random.choices(string.ascii_uppercase, k=3)
        random_plate_letters = str(raw_random_plate_letters).replace('[', '').replace(']', '').replace('"', '').replace("'", '').replace(' ', '')
        random_plate = f"{random_plate_letters} {random_plate_numbers}"
        return random_plate

    def _scan_plate(self):
        return self.generate_random_plate()

    def detect_vehicle(self):
        #get the plate of car passing the sensor
        self.plate = self._scan_plate()
        self.update_car_park(plate)

class EntrySensor(Sensors):
    def __init__(self, identification, is_active, car_park):
        super().__init__(identification, is_active, car_park)
    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f'Car passed through Entry with plate: {plate}.')

entry_sensor = EntrySensor("Entry", True, "Perth")
print(entry_sensor)

class ExitSensor(Sensors):
    def __init__(self, identification, is_active, car_park):
        super().__init__(identification, is_active, car_park)
    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
        print(f'Car passed through Exit with plate: {plate}.')

exit_sensor = ExitSensor("Exit", True, "Perth")
print(exit_sensor)