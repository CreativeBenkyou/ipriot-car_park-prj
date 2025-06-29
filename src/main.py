from display import Display
from sensors import EntrySensor
from sensors import ExitSensor
from car_park import CarPark
import random

main_car_park = CarPark('Moondalup', 100, 25, log_file="moondalup.txt")
entry_sensor = EntrySensor(main_car_park, '1', is_active = True)
exit_sensor = ExitSensor(main_car_park, '2', is_active = True)
display = Display('1', main_car_park, "Welcome to Moondalup Car Park!")
main_car_park.register(display)

def main():
    for car in range(10):
        entry_sensor.detect_vehicle()

    print("\nShows ten cars entering the Moondalup Car Park:\n")
    main_car_park.read_log_file()

    for car in range(2):
        plate = random.choice(main_car_park.plates)
        exit_sensor.update_car_park(plate)

    print("\nShows two cars exiting the Moondalup Car Park:\n")
    main_car_park.read_log_file()

main()