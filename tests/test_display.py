import unittest
from display import Display
from car_park import CarPark

class TestDisplay(unittest.TestCase):
    def __init__(self, method_name: str = 'run_test'):
        super().__init__(method_name)
        self.car_park = CarPark(location=None, capacity=None, weather=None)

    def setUp(self):
        self.display = Display(display_id='1', message='Welcome to the car park', is_on=True, car_park=self.car_park)

    def test_display_initialised_with_all_attributes(self):
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.display_id, '1')
        self.assertEqual(self.display.message, 'Welcome to the car park')
        self.assertEqual(self.display.is_on, True)
        self.assertIsInstance(self.display.car_park, CarPark)

    def test_update(self):
        self.display.update({'message': 'Goodbye'})
        self.assertEqual(self.display.message, 'Goodbye')