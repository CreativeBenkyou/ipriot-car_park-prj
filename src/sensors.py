from abc import ABC, abstractmethod
import random
import string

class Sensors(ABC):
    def __init__(self, identification, is_active, car_park):
        """
        This function is the initialiser for the Sensors class.
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
        """
        The function is an abstract method to enable the child class to modify it.
        :param plate:
        :return:
        """
        pass

    def generate_random_plate(self):
        """
        This function is used to make random plate numbers for checking if the car park is working properly.
        :return:
        """
        random_plate_numbers = format(random.randint(0, 999), '03d')
        raw_random_plate_letters = random.choices(string.ascii_uppercase, k=3)
        random_plate_letters = str(raw_random_plate_letters).replace('[', '').replace(']', '').replace('"', '').replace("'", '').replace(' ', '')
        random_plate = f"{random_plate_letters} {random_plate_numbers}"
        return random_plate

    def _scan_plate(self):
        """
        This function should scan the car's licence plate as they pass the sensor, but is not implemented yet. Instead, it will return the random plate.
        :return:
        """
        return self.generate_random_plate()

    def detect_vehicle(self):
        """
        This function gets the plate of car passing the sensor.
        :return:
        """
        plate = self._scan_plate()
        self.update_car_park(plate)

class EntrySensor(Sensors):
    def __init__(self, identification, is_active, car_park):
        """
        This function is the initialiser for the EntrySensors class, it has a super() function to allow access to the parent class attributes and methods.
        :param identification:
        :param is_active:
        :param car_park:
        """
        super().__init__(identification, is_active, car_park)
    def update_car_park(self, plate):
        """
        This function updates the plate parameter/argument to add a plate to the data.
        :param plate:
        :return:
        """
        self.car_park.add_car(plate)
        print(f'Car passed through Entry with plate: {plate}.')

entry_sensor = EntrySensor("Entry", True, "Perth")
print(entry_sensor)

class ExitSensor(Sensors):
    def __init__(self, identification, is_active, car_park):
        """
        This function is the initialiser for the ExitSensors class, it has a super() function to allow access to the parent class attributes and methods.
        :param identification:
        :param is_active:
        :param car_park:
        """
        super().__init__(identification, is_active, car_park)
    def update_car_park(self, plate):
        """
        This function updates the plate parameter/argument to add a plate to the data.
        :param plate:
        :return:
        """
        self.car_park.remove_car(plate)
        print(f'Car passed through Exit with plate: {plate}.')

exit_sensor = ExitSensor("Exit", True, "Perth")
print(exit_sensor)