from car import Car
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery

class Glissade(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage, current_date):
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        super().__init__(engine, battery)
