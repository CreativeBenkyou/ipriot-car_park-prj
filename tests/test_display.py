import unittest
from display import Display

class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.display = Display(display_id='123', message="Welcome", is_on=True)

    def test_display_initialised_with_all_attributes(self):
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.display_id, '123')
        self.assertEqual(self.display.message, 'Welcome')
        self.assertEqual(self.display.is_on, True)

