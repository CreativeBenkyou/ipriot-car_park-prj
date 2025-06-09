from display import Display
from sensors import Sensors


class CarPark():
    def __init__(self, location, capacity, plates = None, sensors = None, displays = None, temp_plates = None):
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
        self.plates = plates
        self.sensors = sensors
        self.displays = displays
        self.temp_plates = temp_plates

    def __str__(self):
        return f"This is the {self.location} Car Park, there are {self.capacity} bays available."

    def register(self):
        """
        This function will register the sensors and the displays
        """
        pass

    def add_car(self):
        """
        Records a licence plate of a car as it enters the car park, updates the displays
        :return:
        """
        pass

    def check_car(self):
        """
        Checks a licence plate of a car as it enters the car park to see if it's already in the car park, updates the displays
        :return:
        """
        pass

    def remove_car(self):
        """
        Removes a licence plate of a car as it exits the car park, updates the displays
        :return:
        """
        pass

    def update_displays(self):
        """
        Finds the correct display to update and updates the display
        :return:
        """
        pass

    def register(self, component):
        if not issubclass(component, Sensors):
            raise TypeError("Object needs to be from Sensors or a Display.")
        if issubclass(component, Sensors):
            self.sensors.append(component)
        if issubclass(component, Display):
            self.displays.append(component)

perth = CarPark("Perth", 100)
print(perth)
