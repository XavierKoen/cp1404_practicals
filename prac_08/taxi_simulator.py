"""
Taxi simulator program
Provides range of taxi choices
Simulates fare for trip taken in chosen taxi
"""
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Initialise available taxis and constructs menu."""
    current_taxi = None
    current_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    menu_selection = ''
    while menu_selection != 'q':
        print("q)uit, c)hoose taxi, d)rive")
        menu_selection = input(">>> ")
        if menu_selection == 'c':
            current_taxi = choose_taxi(taxis)
            print("Bill to date: ${:.2f}".format(current_bill))
        elif menu_selection == 'd':
            try:
                cost_of_trip = commence_trip(current_taxi)
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name, cost_of_trip))
                current_bill += cost_of_trip
                print("Bill to date: ${:.2f}".format(current_bill))
            except AttributeError:
                print("Please choose a taxi first.")
        elif menu_selection == 'q':
            print("Total trip cost: ${:.2f}\nTaxis are now:".format(current_bill))
            list_taxis(taxis)
        else:
            print("Please select a valid menu option:")


def choose_taxi(taxis):
    """List available taxis and allow user to select one."""
    print("Taxis available:")
    list_taxis(taxis)
    valid_taxi_index = False
    while not valid_taxi_index:
        try:
            chosen_taxi = taxis[int(input("Choose taxi: "))]
            valid_taxi_index = True
            return chosen_taxi
        except IndexError:
            print("Number is out of range! Please enter a valid taxi index number.")
        except ValueError:
            print("Invalid input! Please enter a valid taxi index number.")


def list_taxis(taxis):
    """List taxis."""
    [print("{} - {}".format(taxis.index(taxi), taxi)) for taxi in taxis]


def commence_trip(current_taxi):
    """Drive taxi desired distance and update bill based on fare."""
    current_taxi.start_fare()
    current_taxi.drive(float(input("Drive how far? ")))
    cost = current_taxi.get_fare()
    return cost


main()
