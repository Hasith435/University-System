from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
import os

import openpyxl as xl

from student_functions import students
from student_functions import courses
from student_functions import clubs

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

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

root = Tk()
root.configure(bg="#000000")
root.title("Welcome to the University")
# root.iconbitmap('D:\download.png')


font_style_popup_button = tkFont.Font(family= "corberl light", size=15)
font_style_main_entry = tkFont.Font(family= "corbel light", size= 20)
font_style_user_input_lbl = tkFont.Font(family= "corbel light", size= 13)
font_style_submit_button = tkFont.Font(family= "corbel light", size = 15, weight= "bold")
font_style_title = tkFont.Font(family= "corbel light", size= 40)
font_style_button = tkFont.Font(family= "corbel light", size= 20)
font_style_welcome_frame_title = tkFont.Font(family= "corbel", size=30 )
font_style_choice = tkFont.Font(family= "corbel light", size=18)
font_style_enter_button = tkFont.Font(family= "cobel light", size= 12)


#Features that students can access
class student_functions:
    @staticmethod
    def view_details_get_entry():

        student_ID_get = 0

        window_details_ID = Toplevel()
        window_details_ID.configure(bg="#393939")
        window_details_ID.title("View student Details")


        student_ID_label = Label(window_details_ID,text= "Student ID:", font=font_style_main_entry, pady= 2, bg="#393939", foreground= "white")
        student_ID_label.grid(row=0, column=0)
        student_ID_entry = Entry(window_details_ID, width= 50,bg="#393939", foreground= "white")
        student_ID_entry.grid(row= 0 , column= 1)




        def view_details():

            try:
                student_ID_get = int(student_ID_entry.get())

                returned_list = students.view_student_details(student_ID_get)

                # view_details_window = Toplevel()
                # view_details_window.configure(bg="#393939")

                student_ID_details_lbl = Label(window_details_ID, text="Student ID:", bg="#393939", foreground="white")
                fname_details_lbl = Label(window_details_ID, text="First Name:", bg="#393939", foreground="white")
                lname_details_lbl = Label(window_details_ID, text="Last Name:", bg="#393939", foreground="white")
                DoB_details_lbl = Label(window_details_ID, text="Date of Birth:", bg="#393939", foreground="white")
                gender_details_lbl = Label(window_details_ID, text="Gender:", bg="#393939", foreground="white")
                guardian_details_lbl = Label(window_details_ID, text="Guardain Names:", bg="#393939", foreground="white")
                guardian_telephone_lbl = Label(window_details_ID, text="Guardian Telephone:", bg="#393939",foreground="white")
                address_details_lbl = Label(window_details_ID, text="Address:", bg="#393939", foreground="white")

                print(students.view_student_details(student_ID_get))
                student_ID_details = Label(window_details_ID, text=returned_list[0],bg="#393939", foreground="white", width= 50)
                fname_details = Label(window_details_ID, text=returned_list[1], bg="#393939",foreground="white", width= 50)
                lname_details = Label(window_details_ID, text=returned_list[2], bg="#393939", foreground="white", width= 50)
                DoB_details = Label(window_details_ID, text=returned_list[3], bg="#393939",foreground="white", width= 50)
                gender_details = Label(window_details_ID, text=returned_list[4], bg="#393939",foreground="white", width= 50)
                guardian_names_details = Label(window_details_ID, text=returned_list[5],bg="#393939", foreground="white", width= 50)
                guardian_telephone_details = Label(window_details_ID, text=returned_list[6],bg="#393939", foreground="white", width= 50)
                address_details = Label(window_details_ID, text=returned_list[7], bg="#393939", foreground="white", width= 50)

                student_ID_details_lbl.grid(row=1, column=0)
                fname_details_lbl.grid(row=2, column=0)
                lname_details_lbl.grid(row=3, column=0)
                DoB_details_lbl.grid(row=4, column=0)
                gender_details_lbl.grid(row=5, column=0)
                guardian_details_lbl.grid(row=6, column=0)
                guardian_telephone_lbl.grid(row=7, column=0)
                address_details_lbl.grid(row=8, column=0)

                student_ID_details.grid(row=1, column=1, sticky= W)
                fname_details.grid(row=2, column=1, sticky= W)
                lname_details.grid(row=3, column=1, sticky= W)
                DoB_details.grid(row=4, column=1, sticky= W)
                gender_details.grid(row=5, column=1, sticky= W)
                guardian_names_details.grid(row=6, column=1, sticky= W)
                guardian_telephone_details.grid(row=7, column=1, sticky= W)
                address_details.grid(row=8, column=1, sticky= W)

            except:
                student_not_found_lbl = Label(window_details_ID,text= "Student Not Found!",bg="#393939", foreground="white" )
                student_not_found_lbl.grid(columnspan= 2)
                print('Student Not found')

            
            print(type(student_ID_get))

            

        enter_button = Button(window_details_ID, text= "Enter", font= font_style_popup_button, command=view_details, bg="#393939", foreground= "white", width= 30)
        enter_button.grid(row=9, column=1, pady= 10)

        def back():
            window_details_ID.destroy()

        back_button = Button(window_details_ID, text="Back", bg="#e84d1a", foreground="white", width=10, font=font_style_submit_button, command=back, borderwidth=0)
        back_button.grid(row=9, column=0, pady= 10)


def student_button_root():

    view_student_details_button = Button(root,text= "View Student Details", width=20, font= font_style_button, bg="#393939", foreground= "white", command = student_functions.view_details_get_entry, borderwidth=0)
    apply_for_course = Button(root, text= "Apply for a Course", width= 20,font= font_style_button, bg="#393939", foreground= "white",borderwidth= 0)
    view_grades_button= Button(root, text="View Grades", width=20, font=font_style_button,bg="#393939", foreground="white", borderwidth=0)
    apply_for_club = Button(root, text="Apply for a Club", width=20, font=font_style_button,bg="#393939", foreground="white", borderwidth=0)

    view_student_details_button.grid(row=7, column=0, padx=7, pady=10)
    apply_for_course.grid(row=7, column=1, padx=7, pady=10)
    view_grades_button.grid(row=7, column=2, padx=7, pady=10)
    apply_for_club.grid(row=7, column=3, padx=7, pady=10)





#Features that Teachers can Access
class teacher_functions:
    @staticmethod
    def view_details_get_entry():

        student_ID_get = 0

        window_details_ID = Toplevel()
        window_details_ID.configure(bg="#393939")
        window_details_ID.title("View student Details")


        student_ID_label = Label(window_details_ID,text= "Student ID:", font=font_style_main_entry, pady= 2, bg="#393939", foreground= "white")
        student_ID_label.grid(row=0, column=0)
        student_ID_entry = Entry(window_details_ID, width= 50,bg="#393939", foreground= "white")
        student_ID_entry.grid(row= 0 , column= 1)




        def view_details():

            try:
                student_ID_get = int(student_ID_entry.get())

                returned_list = students.view_student_details(student_ID_get)

                # view_details_window = Toplevel()
                # view_details_window.configure(bg="#393939")

                student_ID_details_lbl = Label(window_details_ID, text="Student ID:", bg="#393939", foreground="white")
                fname_details_lbl = Label(window_details_ID, text="First Name:", bg="#393939", foreground="white")
                lname_details_lbl = Label(window_details_ID, text="Last Name:", bg="#393939", foreground="white")
                DoB_details_lbl = Label(window_details_ID, text="Date of Birth:", bg="#393939", foreground="white")
                gender_details_lbl = Label(window_details_ID, text="Gender:", bg="#393939", foreground="white")
                guardian_details_lbl = Label(window_details_ID, text="Guardain Names:", bg="#393939", foreground="white")
                guardian_telephone_lbl = Label(window_details_ID, text="Guardian Telephone:", bg="#393939",foreground="white")
                address_details_lbl = Label(window_details_ID, text="Address:", bg="#393939", foreground="white")

                print(students.view_student_details(student_ID_get))
                student_ID_details = Label(window_details_ID, text=returned_list[0],bg="#393939", foreground="white", width= 50)
                fname_details = Label(window_details_ID, text=returned_list[1], bg="#393939",foreground="white", width= 50)
                lname_details = Label(window_details_ID, text=returned_list[2], bg="#393939", foreground="white", width= 50)
                DoB_details = Label(window_details_ID, text=returned_list[3], bg="#393939",foreground="white", width= 50)
                gender_details = Label(window_details_ID, text=returned_list[4], bg="#393939",foreground="white", width= 50)
                guardian_names_details = Label(window_details_ID, text=returned_list[5],bg="#393939", foreground="white", width= 50)
                guardian_telephone_details = Label(window_details_ID, text=returned_list[6],bg="#393939", foreground="white", width= 50)
                address_details = Label(window_details_ID, text=returned_list[7], bg="#393939", foreground="white", width= 50)

                student_ID_details_lbl.grid(row=1, column=0)
                fname_details_lbl.grid(row=2, column=0)
                lname_details_lbl.grid(row=3, column=0)
                DoB_details_lbl.grid(row=4, column=0)
                gender_details_lbl.grid(row=5, column=0)
                guardian_details_lbl.grid(row=6, column=0)
                guardian_telephone_lbl.grid(row=7, column=0)
                address_details_lbl.grid(row=8, column=0)

                student_ID_details.grid(row=1, column=1, sticky= W)
                fname_details.grid(row=2, column=1, sticky= W)
                lname_details.grid(row=3, column=1, sticky= W)
                DoB_details.grid(row=4, column=1, sticky= W)
                gender_details.grid(row=5, column=1, sticky= W)
                guardian_names_details.grid(row=6, column=1, sticky= W)
                guardian_telephone_details.grid(row=7, column=1, sticky= W)
                address_details.grid(row=8, column=1, sticky= W)

            except:
                student_not_found_lbl = Label(window_details_ID,text= "Student Not Found!",bg="#393939", foreground="white" )
                student_not_found_lbl.grid(columnspan= 2)
                print('Student Not found')

            
            print(type(student_ID_get))

            

        enter_button = Button(window_details_ID, text= "Enter", font= font_style_popup_button, command=view_details, bg="#393939", foreground= "white", width= 30)
        enter_button.grid(row=9, column=1, pady= 10)

        def back():
            window_details_ID.destroy()

        back_button = Button(window_details_ID, text="Back", bg="#e84d1a", foreground="white", width=10, font=font_style_submit_button, command=back, borderwidth=0)
        back_button.grid(row=9, column=0, pady= 10)

    @staticmethod
    def add_student_grades():
        

def teacher_button_root():
    view_student_details_button = Button(root, text= "View Student Details", width= 20,font= font_style_button, bg="#393939", foreground= "white",borderwidth= 0,command= teacher_functions.view_details_get_entry)
    add_course_grades_button = Button(root, text= "Add Grades", width= 20,font= font_style_button, bg="#393939", foreground= "white",borderwidth= 0)

    view_student_details_button.grid(row= 7, column= 0, padx=7, pady=10 )
    add_course_grades_button.grid(row= 7, column= 1, padx= 7, pady= 10)



#Features that the Admin can Access
class admin_functions:

    @staticmethod
    def register_students():
        global fname, lname, DoB, gender, guardian_names, guardian_telephone, address, submit_button, fname_entry, lname_entry, dob_entry, gender_entry, guardian_names_entry, \
            guardian_telephone_entry, address_entry, window

        window = Toplevel()
        window.configure(bg="#393939")
        window.title("Register Students")

        # Assigning the Entry Fields
        fname_entry = Entry(window, width=40, font=font_style_user_input_lbl, bg="#393939", foreground="white")
        lname_entry = Entry(window, width=40, font=font_style_user_input_lbl, bg="#393939", foreground="white")
        dob_entry = Entry(window, width=40, font=font_style_user_input_lbl, bg="#393939", foreground="white")
        gender_entry = Entry(window, width=40, font=font_style_user_input_lbl, bg="#393939", foreground="white")
        guardian_names_entry = Entry(window, width=40, font=font_style_user_input_lbl, bg="#393939", foreground="white")
        guardian_telephone_entry = Entry(window, width=40, font=font_style_user_input_lbl, bg="#393939",
                                         foreground="white")
        address_entry = Entry(window, width=40, font=font_style_user_input_lbl, bg="#393939", foreground="white")

        fname_lbl = Label(window, text="First Name:", font=font_style_user_input_lbl, bg="#393939", foreground="white")
        lname_lbl = Label(window, text="Last Name:", font=font_style_user_input_lbl, bg="#393939", foreground="white")
        dob_lbl = Label(window, text="Date of Birth:", font=font_style_user_input_lbl, bg="#393939", foreground="white")
        gender_lbl = Label(window, text="Gender:", font=font_style_user_input_lbl, bg="#393939", foreground="white")
        guardian_names_lbl = Label(window, text="Guardian Names:", font=font_style_user_input_lbl, bg="#393939",
                                   foreground="white")
        guardian_telephone_lbl = Label(window, text="Guardian Telephone:", font=font_style_user_input_lbl, bg="#393939",
                                       foreground="white")
        address_lbl = Label(window, text="Address:", font=font_style_user_input_lbl, bg="#393939", foreground="white")

        fname_lbl.grid(row=0, column=0, sticky=W)
        lname_lbl.grid(row=1, column=0, sticky=W)
        dob_lbl.grid(row=2, column=0, sticky=W)
        gender_lbl.grid(row=3, column=0, sticky=W)
        guardian_names_lbl.grid(row=4, column=0, sticky=W)
        guardian_telephone_lbl.grid(row=5, column=0, sticky=W)
        address_lbl.grid(row=6, column=0, sticky=W)

        # Positionning the Entry Fields
        fname_entry.grid(row=0, column=1)
        lname_entry.grid(row=1, column=1)
        dob_entry.grid(row=2, column=1)
        gender_entry.grid(row=3, column=1)
        guardian_names_entry.grid(row=4, column=1)
        guardian_telephone_entry.grid(row=5, column=1)
        address_entry.grid(row=6, column=1)

        def submit():
            global fname, lname, DoB, gender, guardian_names, guardian_telephone, address, submit_button, fname_entry, lname_entry, dob_entry, gender_entry, guardian_names_entry, \
                guardian_telephone_entry, address_entry, window

            fname = fname_entry.get()
            lname = lname_entry.get()
            DoB = dob_entry.get()
            gender = gender_entry.get()
            guardian_names = guardian_names_entry.get()
            guardian_telephone = guardian_telephone_entry.get()
            address = address_entry.get()

            submit_label = Label(window, text="Registered", bg="#393939", foreground="white")
            submit_label.grid(columnspan=2, pady=10)

            students(fname, lname, DoB, gender, guardian_names, guardian_telephone, address)

            fname_entry.delete(first=0, last=22)
            lname_entry.delete(first=0, last=22)
            dob_entry.delete(first=0, last=22)
            gender_entry.delete(first=0, last=22)
            guardian_names_entry.delete(first=0, last=100)
            guardian_telephone_entry.delete(first=0, last=100)
            address_entry.delete(first=0, last=22)

        def back():
            window.destroy()

        submit_button = Button(window, text="Submit", bg="#24e1f2", foreground="white", width=30,
                               font=font_style_submit_button, command=submit, borderwidth=0)
        submit_button.grid(row=7, column=1, pady=5, padx=10)

        back_button = Button(window, text="Back", bg="#e84d1a", foreground="white", width=10,
                             font=font_style_submit_button, command=back, borderwidth=0)
        back_button.grid(row=7, column=0)

    @staticmethod
    def view_details_get_entry():
        student_ID_get = 0

        window_details_ID = Toplevel()
        window_details_ID.configure(bg="#393939")
        window_details_ID.title("View student Details")

        student_ID_label = Label(window_details_ID, text="Student ID:", font=font_style_main_entry, pady=2,
                                 bg="#393939", foreground="white")
        student_ID_label.grid(row=0, column=0)
        student_ID_entry = Entry(window_details_ID, width=50, bg="#393939", foreground="white")
        student_ID_entry.grid(row=0, column=1)

        def view_details():

            try:
                student_ID_get = int(student_ID_entry.get())

                returned_list = students.view_student_details(student_ID_get)

                # view_details_window = Toplevel()
                # view_details_window.configure(bg="#393939")

                student_ID_details_lbl = Label(window_details_ID, text="Student ID:", bg="#393939", foreground="white")
                fname_details_lbl = Label(window_details_ID, text="First Name:", bg="#393939", foreground="white")
                lname_details_lbl = Label(window_details_ID, text="Last Name:", bg="#393939", foreground="white")
                DoB_details_lbl = Label(window_details_ID, text="Date of Birth:", bg="#393939", foreground="white")
                gender_details_lbl = Label(window_details_ID, text="Gender:", bg="#393939", foreground="white")
                guardian_details_lbl = Label(window_details_ID, text="Guardain Names:", bg="#393939",
                                             foreground="white")
                guardian_telephone_lbl = Label(window_details_ID, text="Guardian Telephone:", bg="#393939",
                                               foreground="white")
                address_details_lbl = Label(window_details_ID, text="Address:", bg="#393939", foreground="white")

                print(students.view_student_details(student_ID_get))
                student_ID_details = Label(window_details_ID, text=returned_list[0], bg="#393939", foreground="white",
                                           width=50)
                fname_details = Label(window_details_ID, text=returned_list[1], bg="#393939", foreground="white",
                                      width=50)
                lname_details = Label(window_details_ID, text=returned_list[2], bg="#393939", foreground="white",
                                      width=50)
                DoB_details = Label(window_details_ID, text=returned_list[3], bg="#393939", foreground="white",
                                    width=50)
                gender_details = Label(window_details_ID, text=returned_list[4], bg="#393939", foreground="white",
                                       width=50)
                guardian_names_details = Label(window_details_ID, text=returned_list[5], bg="#393939",
                                               foreground="white", width=50)
                guardian_telephone_details = Label(window_details_ID, text=returned_list[6], bg="#393939",
                                                   foreground="white", width=50)
                address_details = Label(window_details_ID, text=returned_list[7], bg="#393939", foreground="white",
                                        width=50)

                student_ID_details_lbl.grid(row=1, column=0)
                fname_details_lbl.grid(row=2, column=0)
                lname_details_lbl.grid(row=3, column=0)
                DoB_details_lbl.grid(row=4, column=0)
                gender_details_lbl.grid(row=5, column=0)
                guardian_details_lbl.grid(row=6, column=0)
                guardian_telephone_lbl.grid(row=7, column=0)
                address_details_lbl.grid(row=8, column=0)

                student_ID_details.grid(row=1, column=1, sticky=W)
                fname_details.grid(row=2, column=1, sticky=W)
                lname_details.grid(row=3, column=1, sticky=W)
                DoB_details.grid(row=4, column=1, sticky=W)
                gender_details.grid(row=5, column=1, sticky=W)
                guardian_names_details.grid(row=6, column=1, sticky=W)
                guardian_telephone_details.grid(row=7, column=1, sticky=W)
                address_details.grid(row=8, column=1, sticky=W)

            except:
                student_not_found_lbl = Label(window_details_ID, text="Student Not Found!", bg="#393939",
                                              foreground="white")
                student_not_found_lbl.grid(columnspan=2)
                print('Student Not found')

            print(type(student_ID_get))

        enter_button = Button(window_details_ID, text="Enter", font=font_style_popup_button, command=view_details,
                              bg="#393939", foreground="white", width=30)
        enter_button.grid(row=9, column=1, pady=10)

        def back():
            window_details_ID.destroy()

        back_button = Button(window_details_ID, text="Back", bg="#e84d1a", foreground="white", width=10,
                             font=font_style_submit_button, command=back, borderwidth=0)
        back_button.grid(row=9, column=0, pady=10)

    @staticmethod
    def remove_student():
        window_remove_student = Toplevel()
        window_remove_student.configure(bg="#393939")
        window_remove_student.title('Remove Student')

        Student_ID_lbl = Label(window_remove_student, text="Student ID:", bg="#393939", foreground="white",
                               font=font_style_main_entry)
        Student_ID_lbl.grid(row=0, column=0)

        Student_ID_entry = Entry(window_remove_student, width=50, bg="#393939", foreground="white")
        Student_ID_entry.grid(row=0, column=1)

        def enter_button():
            try:
                student_ID = int(Student_ID_entry.get())
                print(student_ID)
                students.remove_student_function(student_ID)

                removed_lbl = Label(window_remove_student, text="Removed", bg="#393939", foreground="white")
                removed_lbl.grid(columnspan=2)

            except:
                student_not_found_lbl = Label(window_remove_student, text="Student Not Found!", bg="#393939",
                                              foreground="white")
                student_not_found_lbl.grid(columnspan=2)
                print('Student Not found')

        def back():
            window_remove_student.destroy()

        back_button = Button(window_remove_student, text="Back", bg="#e84d1a", foreground="white", width=10,
                             font=font_style_submit_button, command=back, borderwidth=0)
        back_button.grid(row=1, column=0, pady=10)

        enter_button = Button(window_remove_student, text="Enter", font=font_style_popup_button, command=enter_button,
                              bg="#393939", foreground="white", width=30)
        enter_button.grid(row=1, column=1)

    @staticmethod
    def add_course():
        course_register_window = Toplevel()
        course_register_window.configure(bg="#393939")
        course_register_window.title("Register Course")

        course_name_entry = Entry(course_register_window, width=40, font=font_style_user_input_lbl, bg="#393939", foreground="white")
        course_duration_entry = Entry(course_register_window, width=40, font=font_style_user_input_lbl, bg="#393939", foreground="white")
        prerequisites_entry = Entry(course_register_window, width=40, font=font_style_user_input_lbl, bg="#393939", foreground="white")
        instructors_entry = Entry(course_register_window, width=40, font=font_style_user_input_lbl, bg="#393939", foreground="white")

        course_name_lbl = Label(course_register_window, text="Course Name:", font=font_style_user_input_lbl, bg="#393939", foreground="white")
        course_duration_lbl = Label(course_register_window, text="Course Duration:", font=font_style_user_input_lbl, bg="#393939", foreground="white")
        prerequisites_lbl = Label(course_register_window, text="Prerequisites:", font=font_style_user_input_lbl, bg="#393939", foreground="white")
        instructors_lbl = Label(course_register_window, text="Instructors:", font=font_style_user_input_lbl, bg="#393939", foreground="white")

        course_name_entry.grid(row=0, column=1)
        course_duration_entry.grid(row=1, column=1)
        prerequisites_entry.grid(row=2, column=1)
        instructors_entry.grid(row=3, column=1)

        course_name_lbl.grid(row=0, column=0, sticky=W)
        course_duration_lbl.grid(row=1, column=0, sticky=W)
        prerequisites_lbl.grid(row=2, column=0, sticky=W)
        instructors_lbl.grid(row=3, column=0, sticky=W)

        def submit():
            course_name = course_name_entry.get()
            course_duration = course_duration_entry.get()
            prerequisites = prerequisites_entry.get()
            instructors = instructors_entry.get()

            registered_label = Label(window, text="Registered", bg="#393939", foreground="white")
            registered_label.grid(columnspan=2, pady=10)

            courses(course_name, course_duration, prerequisites, instructors)

            course_name_entry.delete(0,100)
            course_duration_entry.delete(0,100)
            prerequisites_entry.delete(0,100)
            instructors_entry.delete(0,100)
        
        def back():
            course_register_window.destroy()
        
        submit_button = Button(course_register_window, text="Submit", bg="#24e1f2", foreground="white", width=30,font=font_style_submit_button, command=submit, borderwidth=0)
        submit_button.grid(row=7, column=1, pady=5, padx=10)

        back_button = Button(course_register_window, text="Back", bg="#e84d1a", foreground="white", width=10,font=font_style_submit_button, command=back, borderwidth=0)
        back_button.grid(row=7, column=0)

def admin_button_root_rest():
    register_student_button = Button(root, text="Register Student", width=20, font=font_style_button, bg="#393939",foreground="white", command=admin_functions.register_students, borderwidth=0)
    view_student_details_button = Button(root, text="View Student Details", width=20, font=font_style_button,bg="#393939", foreground="white", command=admin_functions.view_details_get_entry, borderwidth=0)
    remove_student_button = Button(root, text="Remove a Student", width=20, font=font_style_button, bg="#393939",foreground="white", borderwidth=0, command=admin_functions.remove_student)
    add_course = Button(root, text="Add a Course", width=20, font=font_style_button, bg="#393939",foreground="white", borderwidth=0, command= admin_functions.add_course)
    view_grades_button = Button(root, text="View Grades", width=20, font=font_style_button, bg="#393939",foreground="white", borderwidth=0)

    register_student_button.grid(row=9, column=0, padx=7, pady=10)
    view_student_details_button.grid(row=9, column=1, padx=7, pady=10)
    remove_student_button.grid(row=9, column=2, padx=7, pady=10)
    add_course.grid(row=9, column=3, padx=7, pady=10)
    view_grades_button.grid(row=10, column=0, padx=7, pady=10)

def admin_button_root_password():
    password_label = Label(root, text= "PASSWORD:", font= font_style_user_input_lbl, bg="#000000", foreground= "#FFFFFF")
    password_entry = Entry(root)

    password_label.grid(row=7, column=1)
    password_entry.grid(row=7, column=2)


    def password_verify():
        password= "12"
        entered_password = password_entry.get()

        if entered_password == password:
            print('correct')
            admin_button_root_rest()

            password_entry.delete(0,100)
            password_entry.insert(0, "correct")

        else:
            print('incorrect')
            password_entry.delete(0, 100)
            password_entry.insert(0, "Incorrect")

    enter_button = Button(root, text="Enter", font=font_style_enter_button, borderwidth=0, width=10, command= password_verify)
    enter_button.grid(row=8, column=2)


def home():
    welcome_lbl = Label(root, text= "Welcome to the University", font= font_style_title, bg="#000000", foreground= "white"  )
    choice_lbl = Label(root, text= "Please choose your Position:", font= font_style_choice, bg="#000000", foreground= "white")

    student_button = Button(text= "STUDENT", font= font_style_button, bg="#545352", foreground= "white", command= student_button_root, borderwidth= 0, width= 9)
    teacher_button = Button(text= "TEACHER", font= font_style_button, bg="#545352", foreground= "white", borderwidth= 0, width= 9, command= teacher_button_root)
    admin_button = Button(text= "ADMIN", font= font_style_button, bg="#545352", foreground= "white", command= admin_button_root_password,borderwidth= 0, width= 9)
    parent_button = Button(text="PARENT", font=font_style_button, bg="#545352", foreground="white", borderwidth=0, width= 9)

    welcome_lbl.grid(columnspan=4)
    choice_lbl.grid(columnspan=4)

    student_button.grid(row=5, column=0, pady= 20)
    teacher_button.grid(row=5, column=1, pady= 20)
    admin_button.grid(row=5, column=2, pady= 20)
    parent_button.grid(row= 5, column= 3, pady= 20)

home()






# students_frame = LabelFrame(text= "STUDENTS", font=font_style_welcome_frame_title, padx=80, pady=5, bg="#000000", foreground= "white")
# students_frame.grid(row=1, column=0)

# course_frame = LabelFrame(text= "COURSES", font=font_style_welcome_frame_title, padx= 80, pady=5, bg="#000000", foreground= "white")
# course_frame.grid(row=5, column=0)


# register_student_button = Button(students_frame, text= "Register Student", width=20, font= font_style_button, bg="#393939", foreground= "white" , command= student_functions.register_student, borderwidth=0)
# view_student_details_button = Button(students_frame,text= "View Student Details", width=20, font= font_style_button, bg="#393939", foreground= "white", command = student_functions.view_details_get_entry, borderwidth=0)
# remove_student_button = Button(students_frame,text= "Remove a Student", width=20, font= font_style_button, bg="#393939", foreground= "white", borderwidth=0, command=student_functions.remove_student )
# add_course_button = Button(course_frame,text= "Add a Course", width=20, font= font_style_button, bg="#393939", foreground= "white", borderwidth=0 )
# view_course_details_button = Button(course_frame,text= "View Course Details", width=20, font= font_style_button, bg="#393939", foreground= "white", borderwidth=0 )
# add_student_to_course_button = Button(course_frame,text= "Enroll in Course", width=20, font= font_style_button, bg="#393939", foreground= "white", borderwidth=0 )
# # add_club_button = Button(root,text= "Add a Club", width=20, font= font_style_button, bg="#393939", foreground= "white", borderwidth=0 )
# # view_club_details_button = Button(root,text= "View Club Details", width=20, font= font_style_button, bg="#393939", foreground= "white", borderwidth=0)
# # add_student_to_club_button = Button(root,text= "Add student to Club", width=20, font= font_style_button, bg="#393939", foreground= "white", borderwidth=0 )


# #
# register_student_button.grid(row=1, column=0, padx=2, pady=2)
# view_student_details_button.grid(row=1, column=1, padx=2, pady=2)
# remove_student_button.grid(row=1, column=2, padx=2, pady=2)
# add_course_button.grid(row=1, column=0, padx=2, pady=2)
# view_course_details_button.grid(row=1, column=1, padx=2, pady=2)
# add_student_to_course_button.grid(row=1, column=2, padx=2, pady=2)
# # add_club_button.grid(row=3, column=1, padx=2, pady=2)
# # view_club_details_button.grid(row=4, column=0, padx=2, pady=2)
# # add_student_to_club_button.grid(row=4, column=1, padx=2, pady=2)




root.mainloop()
