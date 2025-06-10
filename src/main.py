from display import Display
from sensors import EntrySensor
from sensors import ExitSensor
from car_park import CarPark

main_car_park = CarPark('Perth', 100, 25)
entry_sensor = EntrySensor(main_car_park, 'Entry Way', is_active = True)
exit_sensor = ExitSensor(main_car_park, 'Exit Way', is_active = True)
display = Display('Entry Display', main_car_park)
main_car_park.register(display)
entry_sensor.detect_vehicle()
