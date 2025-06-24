from display import Display
from sensors import Sensors

from pathlib import Path
from datetime import datetime

class CarPark():
    def __init__(self, location, capacity, weather, plates = None, sensors = None, displays = None, temp_plates = None, log_file=Path("log.txt")):
        """
        The initialiser for the CarPark class
        :param location:
        :param capacity:
        :param plates:
        :param sensors:
        :param displays:
        """
        self.location = location
        self.capacity = capacity
        self.weather = weather
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.temp_plates = temp_plates or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)

    def __str__(self):
        return f"This is the {self.location} Car Park, there are {self.capacity} bays available."

    @property
    def available_bays(self):
        """
        Figures out the amount of available bays in the car park, it also returns 0 if there are extra cars in the car park than there are total bays.
        :return:
        """
        available_bays_number = self.capacity - len(self.plates)
        if available_bays_number >= 0:
            return available_bays_number
        else:
            return 0

    def update_displays(self):
        """
        Finds the correct display to update and updates the display.
        :return:
        """
        data = {
            "available_bays": self.available_bays,
            "temperature": self.weather,
        }
        for display in self.displays:
            display.update(data)

    def check_car(self):
        """
        Checks a licence plate of a car as it enters the car park to see if it's already in the car park, updates the displays.
        :return:
        """
        raise ValueError('Car can not be removed, the car is not currently in the car park.')

    def add_car(self, plate):
        """
        Records a licence plate of a car as it enters the car park, updates the displays.
        :return:
        """
        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate):
        """
        Removes a licence plate of a car as it exits the car park, updates the displays.
        :return:
        """
        # TO DO: What if plates aren't there?
        if plate in self.plates:
            self.plates.remove(plate)
        else:
            self.check_car()
        self.update_displays()
        self._log_car(plate, entry=False)
        #remove a car that doesn't exist, check car_park.py to see if it cares whether or not a car can get removed if it doesn't exist (unittest error)
        #check_car() not implemented

    def register(self, component):
        """
        Register the sensors and the displays.
        """
        if not isinstance(component, (Sensors, Display)):
            raise TypeError("Object needs to be from Sensors or a Display.")
        if isinstance(component, Sensors):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def _log_car(self, plate:str, entry = True):
        time = format(datetime.now(), "%Y-%m-%d %H:%M:%S")
        with self.log_file.open(mode='a', encoding='utf8') as f:
            f.write(f"Car {plate}{'entered' if entry else 'exited'}\n")

#perth = CarPark("Perth", 100, 10)
#print(perth)

#print(perth.plates)
#print(perth.temp_plates)