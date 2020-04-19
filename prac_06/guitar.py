"""
Guitar Class code.
"""


class Guitar:
    """Represents a guitar."""
    def __init__(self, name='', year=0, cost=0):
        """
        Initialise a Guitar instance.
        name: string, make and model name of guitar object
        year: integer, year of manufacturing for guitar object
        cost: float, price of guitar object
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return guitar object as a string."""
        return "{} ({}) : ${.2f}"

    def get_age(self):
        """Return guitar object age for the year 2020."""
        age = 2020 - self.year
        return age

    def is_vintage(self):
        """Return boolean whether guitar object is vintage (50 years or older)."""
        age = self.get_age()
        if age >= 50:
            vintage_state = True
        else:
            vintage_state = False
        return vintage_state
