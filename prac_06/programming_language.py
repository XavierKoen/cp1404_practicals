"""
ProgrammingLanguage Class code.
Utilises the traits: typing, reflection, and year for each instance.
"""


class ProgrammingLanguage:
    """Represents a programming language."""

    def __init__(self, name='', typing='', reflection='', year=''):
        """
        Initialise a ProgramingLanguage instance.
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == 'Dynamic':
            is_result_dynamice = True
        elif self.typing == 'Static':
            is_result_dynamic = False
        return is_result_dynamic
