class Display():
    def __init__(self, identification, car_park, message = "", is_on = False):
        """
        This function is the initialiser for the Display class
        :param identification:
        :param message:
        :param is_on:
        :param car_park:
        """
        self.identification = identification
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        return f"Display {self.identification}: {self.message}."

    def methods(self):
        pass

display = Display(1, "Perth", "Welcome")
print(display)