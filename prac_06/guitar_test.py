"""Client code to use the ProgrammingLanguage class."""


from prac_06.guitar import Guitar

my_guitar = Guitar('Gibson L-5 CES', 1922, 16035.40)
sam_guitar = Guitar("Gretsch G542TG", 2013, 1069.78)

print("Expected 98. Got {}".format(my_guitar.get_age()))
print("Expected 7. Got {}".format(sam_guitar.get_age()))
print("Expected True. Got {}".format(my_guitar.is_vintage()))
print("Expected False. Got {}".format(sam_guitar.is_vintage()))
