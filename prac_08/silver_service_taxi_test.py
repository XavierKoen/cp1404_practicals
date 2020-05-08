"""
Client code to test SilverServiceTaxi class.
"""
from prac_08.silver_service_taxi import SilverServiceTaxi


my_nice_taxi = SilverServiceTaxi("Gold-Mobile", 100, 2)
print("Initial cost/flagfall should be $4.50, actually is ${}".format(my_nice_taxi.get_fare()))
print("Cost/flagfall after driving 18km should be $48.78, driving distance is actually {}km and fare is actually ${}"
      .format(my_nice_taxi.drive(18), my_nice_taxi.get_fare()))

hummer = SilverServiceTaxi("Hummer", 200, 4)
print(hummer)
