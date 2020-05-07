"""
Code to test Taxi class.
"""
from prac_08.taxi import Taxi

prius = Taxi("Prius 1", 100, 1.23)
prius.drive(40)
print(prius, prius.get_fare())
prius.start_fare()
print(prius, prius.get_fare())
