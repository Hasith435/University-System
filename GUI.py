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

column_headers = ["A", "B", "C", "D", "E", "F","G", "H","I"]

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
        self.options.add_widget(self.register_students)

        self.view_student_details = Button(text= "View Student Details")
        self.view_student_details.bind(on_press = view_student_details.show_pop)
        self.options.add_widget(self.view_student_details)

        self.add_course = Button(text= "Add Course")
        self.add_course.bind(on_press = add_course.show_pop)
        self.options.add_widget(self.add_course)

        self.view_course_details = Button(text= "View Course Details")
        self.options.add_widget(self.view_course_details)

        self.add_student_course = Button(text= "Add Student to a Course")
        self.options.add_widget(self.add_student_course)

        self.add_club = Button(text= "Add a Club")
        self.options.add_widget(self.add_club)

        self.view_club_details = Button(text= "View Club Details")
        self.options.add_widget(self.view_club_details)

        self.add_student_club = Button(text= "Add student to a club")
        self.options.add_widget(self.add_student_club)

        self.add_widget(self.options)

class register(GridLayout):

    def __init__(self, **kwargs):
        super(register, self).__init__(**kwargs)

        self.cols = 2

        # self.submit = Button(text= "Submit", font_size= "20")
        # self.submit.bind(on_press = self.register_press)
        # self.add_widget(self.submit)

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

#This is not done yet
class view_student_details(GridLayout):
    def __init__(self, **kwargs):
        super(view_student_details, self).__init__(**kwargs)

        self.cols = 2

        self.add_widget(Label(text="Student_ID:"))
        self.student_ID = TextInput(multiline = False)
        self.add_widget(self.student_ID)

        self.submit = Button(text="Enter", font_size="20")
        self.submit.bind(on_press= view_student_details.show_pop)
        self.add_widget(self.submit)

        self.fname_details_label = Label(text="First Name:")
        self.add_widget(self.fname_details_label)
        self.fname_details_details = Label(text= str())
        self.add_widget(self.fname_details_details)

        self.lname_details_label = Label(text="Last Name:")
        self.add_widget(self.fname_details_label)
        self.lname_details_details = Label(text=str(self.lname))
        self.add_widget(self.lname_details_details)

        self.dob_details_label = Label(text="Date of Birth:")
        self.add_widget(self.fname_details_label)
        self.dob_details_details = Label(text=str(self.dob))
        self.add_widget(self.dob_details_details)

        self.gender_details_label = Label(text="Gender:")
        self.add_widget(self.fname_details_label)
        self.gender_details_details = Label(text=str(self.gender))
        self.add_widget(self.gender_details_details)

        self.guardian_names_details_label = Label(text="Guardian Name:")
        self.add_widget(self.fname_details_label)
        self.guardian_name_details_details = Label(text=str(self.guardian_name))
        self.add_widget(self.guardian_name_details_details)

        self.guardian_telephone_details_label = Label(text="Guardian Telephone:")
        self.add_widget(self.fname_details_label)
        self.guardian_telephone_details_details = Label(text=str(self.guardian_telephone))
        self.add_widget(self.fname_details_details)

        self.address_details_label = Label(text="Address:")
        self.add_widget(self.fname_details_label)
        self.address_details_details = Label(text=str(self.address))
        self.add_widget(self.address_details_details)


    def show_pop(self):
        show = view_student_details()

        register_pop = Popup(title="View student Details", content = show, size_hint=(None, None), size = (400,400))

        register_pop.open()

    def view_details(self, instance):
        student_ID = self.student_ID.text

        y = 0

        for i in range(2, num_students + 2):
            if ws["A" + str(i)].value == student_ID:
                fname =  ws[column_headers[y + 1] + str(i)].value
                lname = ws[column_headers[y + 2] + str(i)].value
                dob = ws[column_headers[y + 3] + str(i)].value
                gender = ws[column_headers[y + 4] + str(i)].value
                guardian_name = ws[column_headers[y + 5] + str(i)].value
                guardian_telephone = ws[column_headers[y + 6] + str(i)].value
                address = ws[column_headers[y + 7] + str(i)].value

        return fname, lname, dob, gender, guardian_name, guardian_telephone, address

        self.fname_details = Label(text= str(self.fname))
        self.lname_details = Label(text=str(self.lname))
        self.dob_details = Label(text=str(self.dob))
        self.gender_details = Label(text=str(self.gender))
        self.guardian_name_details = Label(text=str(self.guardian_name))
        self.guardian_telephone_details = Label(text=str(self.guardian_telephone))
        self.address_details = Label(text=str(self.address))



class add_course(GridLayout):
    def __init__(self, **kwargs):
        super(add_course, self).__init__(**kwargs)

        self.cols = 2

        self.course_ID = Label(text= "Course_ID:")
        self.add_widget(self.course_ID)
        self.course_ID = TextInput(multiline=False)
        self.add_widget(self.course_ID)

        self.course_name = Label(text= "Course Name:")
        self.add_widget(self.course_name)
        self.course_name = TextInput(multiline=False)
        self.add_widget(self.course_name)

        self.course_duration = Label(text= "Course Duration:")
        self.add_widget(self.course_duration)
        self.course_duration = TextInput(multiline=False)
        self.add_widget(self.course_duration)

        self.prerequisites = Label(text= "Prerequisites: ")
        self.add_widget(self.prerequisites)
        self.prerequisites = TextInput(multiline=False)
        self.add_widget(self.prerequisites)

        self.instructors = Label(text= "Instructors: ")
        self.add_widget(self.instructors)
        self.instructors = TextInput(multiline=False)
        self.add_widget(self.instructors)

        self.enter = Button(text="Enter")
        self.enter.bind(on_press = add_course)
        self.add_widget(self.enter)

    def show_pop(self):
        show = add_course()

        show_pop_window = Popup(title= "Add Course", content= show, size_hint = (None, None), size = (400,400))

        show_pop_window.open()

    def add_course(self, instances):
        course_ID = self.course_ID.text
        course_name = self.course_name.text
        course_duration = self.course_duration.text
        prerequisites = self.prerequisites.text
        instructors = self.instructors.text

        ws_courses["A" + str(course_row)] = course_ID
        ws_courses["B" + str(course_row)] = course_name
        ws_courses["C" + str(course_row)] = course_duration
        ws_courses["D" + str(course_row)] = prerequisites
        ws_courses["E" + str(course_row)] = instructors

        ws_courses['F4'] = num_courses + 1
        wb.save(filename="university.xlsx")



class GUI(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    GUI().run()
