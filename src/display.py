class Display():
    def __init__(self, display_id, car_park, message ="", is_on = False):
        """
        This function is the initialiser for the Display class.
        :param display_id:
        :param message:
        :param is_on:
        :param car_park:
        """
        self.display_id = display_id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        return f"Display {self.display_id}: {self.message}."

    def update(self, data, delay=0.5):
        """
        This function will iterate through the displays to print what's in the data, printed as an item.
        :param data:
        :return:
        """
        for key, value in data.items():
            print(f"Key: {key}, Value: {value}")

#display = Display(1, "Perth", "Welcome")
#print(display)
