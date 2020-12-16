from tkinter import *
import tkinter as tk
import tkinter.font as tkFont

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

root = Tk()
root.configure(bg="#393939")

font_style_title = tkFont.Font(family= "times new roman", size= 40)
font_style_button = tkFont.Font(family= "times new roman", size= 20)

welcome_lbl = Label(root, text= "Welcome to the University", font= font_style_title, bg="#393939", foreground= "white"  )

register_student_button = Button(root, text= "Register Student", width=25, font= font_style_button, bg="#393939", foreground= "white" )
view_student_details_button = Button(root,text= "View Student Details", width=25, font= font_style_button, bg="#393939", foreground= "white" )
add_course_button = Button(root,text= "Add a Course", width=25, font= font_style_button, bg="#393939", foreground= "white" )
view_course_details_button = Button(root,text= "View Course Details", width=25, font= font_style_button, bg="#393939", foreground= "white" )
add_student_to_course_button = Button(root,text= "Add student to a Course", width=25, font= font_style_button, bg="#393939", foreground= "white" )
add_club_button = Button(root,text= "Add a Club", width=25, font= font_style_button, bg="#393939", foreground= "white" )
view_club_details_button = Button(root,text= "View Club Details", width=25, font= font_style_button, bg="#393939", foreground= "white" )
add_student_to_club_button = Button(root,text= "Add student to Club", width=25, font= font_style_button, bg="#393939", foreground= "white" )

welcome_lbl.grid(columnspan=6)

register_student_button.grid(row=1, column=0)
view_student_details_button.grid(row=1, column=1)
add_course_button.grid(row=2, column=0)
view_course_details_button.grid(row=2, column=1)
add_student_to_course_button.grid(row=3, column=0)
add_club_button.grid(row=3, column=1)
view_club_details_button.grid(row=4, column=0)
add_student_to_club_button.grid(row=4, column=1)

def register_student():
    window = Toplevel()

    tkvar = StringVar(root)

    choices = {"M", "F"}

    student_ID = Label(text= "Student ID:")
    fname = Label(text= "First Name:")
    lname = Label(text= "Last Name:")
    dob = Label(text= "Date of Birth (dd/mm/yyyy):")
    gender = OptionMenu(window, tkvar, *choices)
    guardian_names = Label(text= "Guardian Names:")
    guardian_telephone = Label(text= "Guardian Telephone:")
    address = Label(text= "Address:")

root.mainloop()