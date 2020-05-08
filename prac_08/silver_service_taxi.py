"""
SilverServiceTaxi class
"""
from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of Taxi with added fanciness attribute."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        Taxi.__init__(self, name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return a string like a Taxi but with flagfall appended."""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)


    def get_fare(self):
        """Get fare like parent Taxi but include flagfall cost."""
        fare = Taxi.get_fare(self) + self.flagfall
        return fare
