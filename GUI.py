import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout

from student_functions import students
from student_functions import courses
from student_functions import clubs

import openpyxl as xl

wb = xl.load_workbook("university.xlsx")
ws = wb['students']
ws_courses = wb['courses']
ws_student_courses = wb['student_courses']
ws_student_clubs = wb['student_clubs']

num_students = ws["J3"].value
student_row = num_students + 2

num_courses = ws_courses["F4"].value
course_row = num_courses + 2

num_student_courses = ws_student_courses["L4"].value
student_course_row = num_student_courses + 2

num_student_clubs = ws_student_clubs["H4"].value
student_club_row = num_student_clubs + 2

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

        #defining all the buttons
        self.register_students = Button(text = "Register Student")
        self.register_students.bind(on_press = register.show_pop)
        self.add_widget(self.register_students)

        self.view_student_details = Button(text= "View Student Details")

        self.add_course = Button(text= "Add Course")

        self.view_course_details = Button(text= "View Course Details")

        self.add_student_course = Button(text= "Add Student to a Course")

        self.add_club = Button(text= "Add a Club")

        self.view_club_details = Button(text= "View Club Details")

        self.add_student_club = Button(text= "Add student to a club")

class register(GridLayout):

    def __init__(self, **kwargs):
        super(register, self).__init__(**kwargs)

        self.cols = 2

        self.student_ID = Label(text="Student_ID:")
        self.add_widget(self.student_ID)
        self.student_ID = TextInput(multiline=False)
        self.add_widget(self.student_ID)

        self.first_name = Label(text="First Name:")
        self.add_widget(self.first_name)
        self.first_name = TextInput(multiline=False)
        self.add_widget(self.first_name)

        self.last_name = Label(text="Last Name:")
        self.add_widget(self.last_name)
        self.last_name = TextInput(multiline=False)
        self.add_widget(self.last_name)

        self.Date_of_Birth = Label(text="Date of Birth (mm/dd/yyyy):")
        self.add_widget(self.Date_of_Birth)
        self.Date_of_Birth = TextInput(multiline=False)
        self.add_widget(self.Date_of_Birth)

        self.Gender = Label(text="Gender:")
        self.add_widget(self.Gender)
        self.Gender = TextInput(multiline=False)
        self.add_widget(self.Gender)

        self.guardian_names = Label(text="Guardian Names:")
        self.add_widget(self.guardian_names)
        self.guardian_names = TextInput(multiline=False)
        self.add_widget(self.guardian_names)

        self.guardian_telephone = Label(text="Guardian Telephone Number:")
        self.add_widget(self.guardian_telephone)
        self.guardian_telephone = TextInput(multiline=False)
        self.add_widget(self.guardian_telephone)

        self.address = Label(text="Address:")
        self.add_widget(self.address)
        self.address = TextInput(multiline=False)
        self.add_widget(self.address)

        self.submit = Button(text= "Submit", font_size= "20")
        self.submit.bind(on_press = self.register_press)
        self.add_widget(self.submit)

    def show_pop(self):
        show = register()

        register_pop = Popup(title="Register Students", content = show, size_hint=(None, None), size = (400,400))

        register_pop.open()

    def register_press(self, instance):
        student_ID = self.student_ID.text
        fname = self.first_name.text
        lname = self.last_name.text
        dob = self.Date_of_Birth.text
        gender = self.Gender.text
        guardian_names = self.guardian_names.text
        guardian_telephone = self.guardian_telephone.text
        address = self.address.text

        ws["A" + str(student_row)] = student_ID
        ws["B" + str(student_row)] = fname
        ws["C" + str(student_row)] = lname
        ws["D" + str(student_row)] = dob
        ws["E" + str(student_row)] = gender
        ws["F" + str(student_row)] = guardian_names
        ws["G" + str(student_row)] = guardian_telephone
        ws["H" + str(student_row)] = address

        ws['J3'] = num_students + 1
        wb.save(filename="university.xlsx")

        self.student_ID.text = ''
        self.first_name.text = ''
        self.last_name.text = ''
        self.Date_of_Birth.text = ''
        self.Gender.text = ''
        self.guardian_names.text = ''
        self.guardian_telephone.text = ''
        self.address.text = ''



class GUI(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    GUI().run()
