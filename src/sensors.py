class Sensors():
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

    def methods(self):
        pass

entry_display = Sensors(1, True, "Perth")
print(entry_display)

class EntrySensor(Sensors):
    def __init__(self, identification, is_active, car_park):
        super().__init__(identification, is_active, car_park)

entry_sensor = EntrySensor("Entry", True, "Perth")
print(entry_sensor)

class ExitSensor(Sensors):
    def __init__(self, identification, is_active, car_park):
        super().__init__(identification, is_active, car_park)

exit_sensor = ExitSensor("Exit", True, "Perth")
print(exit_sensor)