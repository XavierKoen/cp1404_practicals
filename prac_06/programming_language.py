"""
ProgrammingLanguage Class code.
Utilises the traits: typing, reflection, and year for each instance.
"""


class ProgrammingLanguage:
    """Represents a programming language."""

    def __init__(self, name='', typing='', reflection='', year=''):
        """
        Initialise a ProgramingLanguage instance.
        name: string, name of program object
        typing: string, whether program object contains Dynamic or Static typing
        reflection: boolean, whether program object contains reflection or not
        year: integer, year of program object
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return programming object as a string."""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                           self.year)

    def is_dynamic(self):
        if self.typing == 'Dynamic':
            is_result_dynamic = True
        elif self.typing == 'Static':
            is_result_dynamic = False
        return is_result_dynamic
