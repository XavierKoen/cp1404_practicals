"""
UnreliableCar class
"""
from prac_08.car import Car
import random


class UnreliableCar(Car):
    """Specialised version of Car with added reliability attribute."""

    def __init__(self, name, fuel, reliability):
        Car.__init__(self, name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Similar to parent Car, but pass in reliability attribute."""
        if random.uniform(1,100) < self.reliability:
            distance_driven = Car.drive(self, distance)
        else:
            distance_driven = 0
        return distance_driven
