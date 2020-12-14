import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

from student_functions import students
from student_functions import courses
from student_functions import clubs


class MyGrid(GridLayout):

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        self.cols = 1

        #creating grid layout for welcome
        self.welcome = GridLayout()
        self.welcome.cols = 1

        self.welcome.add_widget(Label(text = 'Welcome to the Univeristy', font_size = 50))

        self.add_widget(self.welcome)


        #creating grid layout for options
        self.options = GridLayout()
        self.options.cols = 2

        self.options.add_widget(Button(text="Register Student", font_size = 20))
        self.options.add_widget(Button(text="View Student Details", font_size=20))
        self.options.add_widget(Button(text="Add a Course", font_size=20))
        self.options.add_widget(Button(text="View Course Details", font_size=20))

        self.add_widget(self.options)

    def register_student_button(self, instances):


class GUI(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    GUI().run()
