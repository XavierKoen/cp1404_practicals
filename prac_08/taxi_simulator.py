"""
Taxi simulator program
Provides range of taxi choices
Simulates fare for trip taken in chosen taxi
"""
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 100, 4)]
    print("Let's drive!\nq)uit, c)hoose taxi, d)rive")
    menu_selection = input(">>> ")
    if menu_selection == 'c':
        pass
        # current_taxi = choose_taxi()
    elif menu_selection == 'd':
        pass
    elif menu_selection == 'q':
        pass
    else:
        pass


# def choose_taxi():


main()
