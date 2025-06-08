class CarPark():
    def __init__(self, location, capacity, plates = None, sensors = None, displays = None):
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

    def __str__(self):
        return f"This is the {self.location} Car Park, there are {self.capacity} bays available."

    def methods(self):
        pass

perth = CarPark("Perth", 100)
print(perth)
