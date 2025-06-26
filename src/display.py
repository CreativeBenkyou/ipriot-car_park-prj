class Display():
    def __init__(self, display_id, car_park, message ="", is_active = False):
        """
        The initialiser for the Display class.
        :param display_id:
        :param message:
        :param is_active:
        :param car_park:
        """
        self.display_id = display_id
        self.message = message
        self.is_on = is_active
        self.car_park = car_park

    def __str__(self):
        return f"Display {self.display_id}: {self.message}."

    def update(self, data, delay=0.5):
        """
        Iterate through the displays to print what's in the data, printed as an item.
        :param data:
        :return:
        """
        if 'message' in data:
            self.message = data['message']
        for key, value in data.items():
            print(f"Key: {key}, Value: {value}")

#display = Display(1, "Perth", "Welcome")
#print(display)
