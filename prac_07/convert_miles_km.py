"""
Kivy program to convert miles to kilometres
Xavier Koen
"""


from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Xavier Koen'


class ConvertMilesToKilometresApp(App):
    """ ConvertMilesToKilometresApp is a Kivy App for converting miles to kilometres """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (400, 200)
        self.title = "Square Number"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        result = value * 1.60934
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, current_input, increment):
        """ handle input change (button press of other call) to increase or decrease in text input widget value """
        result = current_input + increment
        self.root.ids.input_number.text = str(result)


ConvertMilesToKilometresApp().run()
