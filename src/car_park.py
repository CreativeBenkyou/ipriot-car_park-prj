GLOBAL_ATTRIBUTES = "global_attributes"

class CarPark():
    GLOBAL_ATTRIBUTES = "global_attributes"

    def __init__(self, location = "", capacity = "", plates = None, sensors = None, displays = None):
        '''
        This function is the initialiser for the CarPark class
        '''
        location = self.location
        capacity = self.capacity
        plates = self.plates
        sensors = self.sensors
        displays = self.displays

    def __str__(self):
        print(f"This is the {location} Car Park, there are {capacity} bays available.")

    def methods(self):
        pass

