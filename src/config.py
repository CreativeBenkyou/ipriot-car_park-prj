class Config():
    def __init__(self, configuration):
        """
        """
        self.configuration = configuration

    def __str__(self):
        return self.configuration

    def methods(self):
        pass

config1 = Config("First config settings.")
print(config1)
