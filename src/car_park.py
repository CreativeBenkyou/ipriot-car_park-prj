from display import Display
from sensors import Sensors


class CarPark():
    def __init__(self, location, capacity, weather, plates = None, sensors = None, displays = None, temp_plates = None):
        """
        This function is the initialiser for the CarPark class
        :param location:
        :param capacity:
        :param plates:
        :param sensors:
        :param displays:
        """
        self.location = location
        self.capacity = capacity
        self.weather = weather
        self.plates = plates
        self.sensors = sensors
        self.displays = displays
        self.temp_plates = temp_plates

    def __str__(self):
        return f"This is the {self.location} Car Park, there are {self.capacity} bays available."

    @property
    def available_bays(self):
        available_bays_number = self.capacity - len(self.plates)
        if available_bays_number >= 0:
            return 0
        else:
            return available_bays_number


    def register(self):
        """
        This function will register the sensors and the displays
        """
        pass

    def update_displays(self):
        """
        Finds the correct display to update and updates the display
        :return:
        """
        data = {
            "available_bays": self.available_bays(),
            "temperature": self.weather,
        }
        for display in self.displays:
            display.update(data)

    def check_car(self):
        """
        Checks a licence plate of a car as it enters the car park to see if it's already in the car park, updates the displays
        :return:
        """
        pass

    def add_car(self, plate):
        """
        Records a licence plate of a car as it enters the car park, updates the displays
        :return:
        """
        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate):
        """
        Removes a licence plate of a car as it exits the car park, updates the displays
        :return:
        """
        if plate in self.plates:
            self.plates.remove(plate)
        else:
            self.check_car()
        self.update_displays()

    def register(self, component):
        if not issubclass(component, Sensors):
            raise TypeError("Object needs to be from Sensors or a Display.")
        if issubclass(component, Sensors):
            self.sensors.append(component)
        elif issubclass(component, Display):
            self.displays.append(component)

perth = CarPark("Perth", 100, 10)
print(perth)

print(perth.plates)
print(perth.temp_plates)