import unittest
from car_park import CarPark
from sensors import EntrySensor
from display import Display

from pathlib import Path

log_file = Path("log.txt")

class TestCarPark(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("Perth", 100, 25)

    def test_car_park_initialised_with_all_attributes(self):
        self.assertEqual(self.car_park.log_file, log_file)
        self.assertIsInstance(self.car_park, CarPark)
        self.assertEqual(self.car_park.location, "Perth")
        self.assertEqual(self.car_park.capacity, 100)
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.displays, [])
        self.assertEqual(self.car_park.available_bays, 100)

    def test_add_car(self):
        self.car_park.add_car("ABC 001")
        self.assertEqual(self.car_park.plates, ["ABC 001"])
        self.assertEqual(self.car_park.available_bays, 99)

    def test_remove_car(self):
        self.car_park.add_car("ABC 001")
        self.car_park.remove_car("ABC 001")
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.available_bays, 100)

    def test_overfill_the_car_park(self):
        for i in range(100):
            self.car_park.add_car(f"ABC {i}")
        self.assertEqual(self.car_park.available_bays, 0)
        self.car_park.add_car("ABC 100")
        # Overfilling the car park should not change the number of available bays
        self.assertEqual(self.car_park.available_bays, 0)

        # Removing a car from an overfilled car park should not change the number of available bays
        self.car_park.remove_car("ABC 100")
        self.assertEqual(self.car_park.available_bays, 0)

    def test_removing_a_car_that_does_not_exist(self):
        with self.assertRaises(ValueError):
            self.car_park.remove_car("AB 1")

    def test_register_raises_type_error(self):
        test_string = 'Not a Sensor or Display'
        car_park = CarPark('Perth', 100, 25)
        with self.assertRaises(TypeError):
            self.car_park.register(test_string)

    @classmethod
    def test_car_logged_when_entering(self):
        new_carpark = CarPark("Perth", 100, 25, log_file="log.txt")
        self.car_park.add_car("NEW 001")
        with self.car_park.log_file.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("NEW 001", last_line)  # check plate entered
        self.assertIn("entered", last_line)  # check description
        self.assertIn("\n", last_line)  # check entry has a new line

    @classmethod
    def test_car_logged_when_exiting(self):
        new_carpark = CarPark("Perth", 100, 25, log_file="log.txt")
        self.car_park.add_car("NEW 001")
        self.car_park.remove_car("NEW 001")
        with self.car_park.log_file.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("NEW 001", last_line)  # check plate entered
        self.assertIn("exited", last_line)  # check description
        self.assertIn("\n", last_line)  # check entry has a new line

    def test_log_file_created(self):
        new_carpark = CarPark('Perth', 100, 25, log_file="log.txt")
        self.assertTrue(Path("log.txt").exists())

    def tearDown(self):
        Path("log.txt").unlink(missing_ok=True)

if __name__ == "__main__":
    unittest.main()
