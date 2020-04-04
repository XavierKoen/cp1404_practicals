"""
Hexadecimal colour code look up.
User input of colour name returns respective hexadecimal colour code.
10 different colours available.
"""

COLOUR_DICT = {"aquamarine1": "#7fffd4", "azure3": "#c1cdcd", "blue1": "#0000ff", "brown1": "#ff4040",
               "burlywood": "#deb887", "chartreuse1": "#7fff00", "chocolate1": "#ff7f24", "gold1": "#ffd700",
               "khaki": "#f0e68c", "maroon1": "#ff34b3"}

colour_name = input("Please enter colour name: ").lower()
while colour_name != "":  # Keep asking user input until an empty input ("") is received.
    try:
        print(COLOUR_DICT[colour_name])
        colour_name = input("Please enter colour name: ").lower()
    except KeyError:
        print("Invalid colour name!")
        colour_name = input("Please enter colour name: ").lower()
