"""
Client code to test Taxi class.
"""
from prac_08.unreliable_car import UnreliableCar

mazda2 = UnreliableCar("Lemon", 100, 24)
print("Lemon drove {}km = 35km or 0km".format(mazda2.drive(35)))
print("Lemon drove {}km = 35km or 0km".format(mazda2.drive(35)))
print("Lemon drove {}km = 70km or 65km or 30km or 0km".format(mazda2.drive(70)))

subaru_impreza = UnreliableCar("Not Lemon", 90, 85)
print("Not_Lemon drove {}km = 25km or 0km".format(subaru_impreza.drive(25)))
print("Not_Lemon drove {}km = 25km or 0km".format(subaru_impreza.drive(25)))
print("Not_Lemon drove {}km = 70km or 65km or 40km or 0km".format(subaru_impreza.drive(70)))

print("Should see more consecutive 0km for Lemon, and more 25km, 25km then 40km for Not Lemon.")
