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
# root.title("Welcome to the University")
# root.iconbitmap('D:\download.png')


font_style_popup_button = tkFont.Font(family= "corbel light", size=15)
font_style_main_entry = tkFont.Font(family= "corbel light", size= 20)
font_style_user_input_lbl = tkFont.Font(family= "corbel light", size= 13)
font_style_submit_button = tkFont.Font(family= "corbel light", size = 15, weight= "bold")

class student_functions:
    @staticmethod
    def register_student():
        global fname, lname, DoB, gender, guardian_names, guardian_telephone, address, submit_button, fname_entry, lname_entry, dob_entry, gender_entry, guardian_names_entry, \
            guardian_telephone_entry, address_entry, window

        window = Toplevel()
        window.configure(bg="#393939")

        submit_button = Button(window,text= "Submit",bg="#24e1f2", foreground="white", width=50, font=font_style_submit_button, command= student_functions.submit, borderwidth=0 )

        #Assigning the Entry Fields
        fname_entry = Entry(window, width = 40, font= font_style_user_input_lbl, bg="#393939", foreground="white")
        lname_entry =Entry(window, width = 40, font= font_style_user_input_lbl, bg="#393939", foreground="white")
        dob_entry =Entry(window, width = 40, font= font_style_user_input_lbl, bg="#393939", foreground="white")
        gender_entry = Entry(window, width = 40, font= font_style_user_input_lbl, bg="#393939", foreground="white")
        guardian_names_entry =Entry(window, width = 40, font= font_style_user_input_lbl, bg="#393939", foreground="white")
        guardian_telephone_entry =Entry(window, width = 40, font= font_style_user_input_lbl, bg="#393939", foreground="white")
        address_entry =Entry(window, width = 40, font= font_style_user_input_lbl, bg="#393939", foreground="white")

        fname_lbl = Label(window, text= "First Name:", font= font_style_user_input_lbl, bg="#393939", foreground="white")
        lname_lbl = Label(window,text="Last Name:", font=font_style_user_input_lbl, bg="#393939", foreground="white")
        dob_lbl = Label(window,text="Date of Birth:", font=font_style_user_input_lbl, bg="#393939", foreground="white")
        gender_lbl = Label(window,text="Gender:", font=font_style_user_input_lbl, bg="#393939", foreground="white")
        guardian_names_lbl = Label(window,text="Guardian Names:", font=font_style_user_input_lbl, bg="#393939", foreground="white")
        guardian_telephone_lbl = Label(window,text="Guardian Telephone:", font=font_style_user_input_lbl, bg="#393939", foreground="white")
        address_lbl = Label(window,text="Address:", font=font_style_user_input_lbl, bg="#393939", foreground="white")

        fname_lbl.grid(row=0, column=0, sticky=W)
        lname_lbl.grid(row=1, column=0, sticky=W)
        dob_lbl.grid(row=2, column=0, sticky=W)
        gender_lbl.grid(row=3, column=0, sticky=W)
        guardian_names_lbl.grid(row=4, column=0, sticky=W)
        guardian_telephone_lbl.grid(row=5, column=0, sticky=W)
        address_lbl.grid(row=6, column=0, sticky=W)

        #Positionning the Entry Fields
        fname_entry.grid(row=0, column=1)
        lname_entry.grid(row=1, column=1)
        dob_entry.grid(row=2, column=1)
        gender_entry.grid(row=3, column=1)
        guardian_names_entry.grid(row=4, column=1)
        guardian_telephone_entry.grid(row=5, column=1)
        address_entry.grid(row=6, column=1)

        submit_button.grid(columnspan= 2, pady= 10)
    @staticmethod
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

        fname = fname[11:]
        lname = lname[11:]
        DoB = DoB[27:]
        gender = gender[7:]
        guardian_names = guardian_names[15:]
        guardian_telephone = guardian_telephone[19:]
        address = address[8:]

        submit_button = Button(window,text= "Registered", bg= "#393939", foreground= "white")
        submit_button.grid(columnspan= 2, pady= 10)

        students.register_students(fname, lname, DoB, gender, guardian_names, guardian_telephone, address)


    @staticmethod
    def view_details_get_entry():

        student_ID_get = 0

        window_details_ID = Toplevel()
        window_details_ID.configure(bg="#393939")


        student_ID_label = Label(window_details_ID,text= "Student ID:", font=font_style_main_entry, pady= 2, bg="#393939", foreground= "white")
        student_ID_label.grid(row=0, column=0)
        student_ID_entry = Entry(window_details_ID)
        student_ID_entry.grid(row= 0 , column= 1)




        def view_details():

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
            student_ID_details = Label(window_details_ID, text=returned_list[0],bg="#393939", foreground="white")
            fname_details = Label(window_details_ID, text=returned_list[1], bg="#393939",foreground="white")
            lname_details = Label(window_details_ID, text=returned_list[2], bg="#393939", foreground="white")
            DoB_details = Label(window_details_ID, text=returned_list[3], bg="#393939",foreground="white")
            gender_details = Label(window_details_ID, text=returned_list[4], bg="#393939",foreground="white")
            guardian_names_details = Label(window_details_ID, text=returned_list[5],bg="#393939", foreground="white")
            guardian_telephone_details = Label(window_details_ID, text=returned_list[6],bg="#393939", foreground="white")
            address_details = Label(window_details_ID, text=returned_list[7], bg="#393939", foreground="white")

            student_ID_details_lbl.grid(row=1, column=0)
            fname_details_lbl.grid(row=2, column=0)
            lname_details_lbl.grid(row=3, column=0)
            DoB_details_lbl.grid(row=4, column=0)
            gender_details_lbl.grid(row=5, column=0)
            guardian_details_lbl.grid(row=6, column=0)
            guardian_telephone_lbl.grid(row=7, column=0)
            address_details_lbl.grid(row=8, column=0)

            student_ID_details.grid(row=1, column=1)
            fname_details.grid(row=2, column=1)
            lname_details.grid(row=3, column=1)
            DoB_details.grid(row=4, column=1)
            gender_details.grid(row=5, column=1)
            guardian_names_details.grid(row=6, column=1)
            guardian_telephone_details.grid(row=7, column=1)
            address_details.grid(row=8, column=1)

            
            print(type(student_ID_get))

            

        enter_button = Button(window_details_ID, text= "Enter", font= font_style_popup_button, command=view_details, bg="#393939", foreground= "white")
        enter_button.grid(row=9, column=0)
    


font_style_title = tkFont.Font(family= "corbel light", size= 40)
font_style_button = tkFont.Font(family= "corbel light", size= 30)


welcome_lbl = Label(root, text= "Welcome to the University", font= font_style_title, bg="#000000", foreground= "white"  )


register_student_button = Button(root, text= "Register Student", width=20, font= font_style_button, bg="#393939", foreground= "white" , command= student_functions.register_student, borderwidth=0)
view_student_details_button = Button(root,text= "View Student Details", width=20, font= font_style_button, bg="#393939", foreground= "white", command = student_functions.view_details_get_entry, borderwidth=0)
add_course_button = Button(root,text= "Add a Course", width=20, font= font_style_button, bg="#393939", foreground= "white", borderwidth=0 )
view_course_details_button = Button(root,text= "View Course Details", width=20, font= font_style_button, bg="#393939", foreground= "white", borderwidth=0 )
add_student_to_course_button = Button(root,text= "Add student to a Course", width=20, font= font_style_button, bg="#393939", foreground= "white", borderwidth=0 )
add_club_button = Button(root,text= "Add a Club", width=20, font= font_style_button, bg="#393939", foreground= "white", borderwidth=0 )
view_club_details_button = Button(root,text= "View Club Details", width=20, font= font_style_button, bg="#393939", foreground= "white", borderwidth=0)
add_student_to_club_button = Button(root,text= "Add student to Club", width=20, font= font_style_button, bg="#393939", foreground= "white", borderwidth=0 )

welcome_lbl.grid(columnspan=6)

register_student_button.grid(row=1, column=0, padx=2, pady=2)
view_student_details_button.grid(row=1, column=1, padx=2, pady=2)
add_course_button.grid(row=2, column=0, padx=2, pady=2)
view_course_details_button.grid(row=2, column=1, padx=2, pady=2)
add_student_to_course_button.grid(row=3, column=0, padx=2, pady=2)
add_club_button.grid(row=3, column=1, padx=2, pady=2)
view_club_details_button.grid(row=4, column=0, padx=2, pady=2)
add_student_to_club_button.grid(row=4, column=1, padx=2, pady=2)


root.mainloop()