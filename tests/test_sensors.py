import unittest
from sensors import EntrySensor
from sensors import ExitSensor
from car_park import CarPark

class TestEntrySensor(unittest.TestCase):
    def __init__(self, method_name: str = 'run_test'):
        super().__init__(method_name)
        self.car_park = CarPark(location='Perth', capacity=100, weather=25)

    def setUp(self):
        self.entry_sensor = EntrySensor(car_park=self.car_park, display_id='1', is_active=True)

    def test_entry_sensor_initialised_with_all_attributes(self):
        self.assertIsInstance(self.entry_sensor, EntrySensor)
        self.assertEqual(self.entry_sensor.display_id, '1')
        self.assertEqual(self.entry_sensor.is_active, True)
        self.assertIsInstance(self.entry_sensor.car_park, CarPark)

    def test_update(self):
        self.entry_sensor.update_car_park('ABC 123')
        self.assertEqual(self.entry_sensor.car_park.check_car('ABC 123'), True)