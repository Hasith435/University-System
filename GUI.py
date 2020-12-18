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
root.configure(bg="#000000")

font_style_popup_button = tkFont.Font(family= "cobel light", size=15)

class student_functions:
    @staticmethod
    def register_student():
        global fname, lname, DoB, gender, guardian_names, guardian_telephone, address, submit_button, fname_entry, lname_entry, dob_entry, gender_entry, guardian_names_entry, \
            guardian_telephone_entry, address_entry

        window = Toplevel()
        window.configure(bg="#000000")

        f = StringVar()
        l = StringVar()
        d = StringVar()
        ge = StringVar()
        gu = StringVar()
        gt = StringVar()
        a = StringVar()
        #tkvar = StringVar(root)

        #choices = {"M", "F"}

        #student_ID = Label(window,text= "Student ID:",bg="#393939", foreground="white", font= font_style_popup_button)
        fname_lbl = Label(window,text= "First Name:",bg="#000000", foreground="white", font= font_style_popup_button, borderwidth=0, padx= 1.5, pady= 1.5 )
        lname_lbl = Label(window,text= "Last Name:",bg="#393939", foreground="white", font= font_style_popup_button, borderwidth=0)
        dob_lbl = Label(window,text= "Date of Birth (dd/mm/yyyy):",bg="#393939", foreground="white", font= font_style_popup_button, borderwidth=0)
        gender_lbl = Label(window, text= "Gender",bg="#393939", foreground="white", font= font_style_popup_button, borderwidth=0)
        guardian_names_lbl = Label(window,text= "Guardian Names:",bg="#393939", foreground="white", font= font_style_popup_button, borderwidth=0)
        guardian_telephone_lbl = Label(window,text= "Guardian Telephone:",bg="#393939", foreground="white", font= font_style_popup_button, borderwidth=0)
        address_lbl = Label(window,text= "Address:",bg="#393939", foreground="white", font= font_style_popup_button, borderwidth=0)

        submit_button = Button(window,text= "Submit",bg="#393939", foreground="white", width=50, font=font_style_popup_button, command= student_functions.submit, borderwidth=0 )

        #Assigning the Entry Fields
        fname_entry = Entry(window, textvariable= f)
        lname_entry =Entry(window, textvariable= l)
        dob_entry =Entry(window, textvariable= d)
        gender_entry = Entry(window, textvariable= ge)
        guardian_names_entry =Entry(window, textvariable= gu)
        guardian_telephone_entry =Entry(window, textvariable= gt)
        address_entry =Entry(window, textvariable= a)

        #Positioning the Labels
        fname_lbl.grid(row=0, column=0)
        lname_lbl.grid(row=1, column=0)
        dob_lbl.grid(row=2, column=0)
        gender_lbl.grid(row=3, column=0)
        guardian_names_lbl.grid(row=4, column=0)
        guardian_telephone_lbl.grid(row=5, column=0)
        address_lbl.grid(row=6, column=0)


        #Positionning the Entry Fields
        fname_entry.grid(row=0, column=1)
        lname_entry.grid(row=1, column=1)
        dob_entry.grid(row=2, column=1)
        gender_entry.grid(row=3, column=1)
        guardian_names_entry.grid(row=4, column=1)
        guardian_telephone_entry.grid(row=5, column=1)
        address_entry.grid(row=6, column=1)

        submit_button.grid(columnspan= 2)

        #Getting the text that the user entered in the entry fields
    @staticmethod
    def submit():
        global fname, lname, DoB, gender, guardian_names, guardian_telephone, address, submit_button, fname_entry, lname_entry, dob_entry, gender_entry, guardian_names_entry, \
            guardian_telephone_entry, address_entry

        fname = fname_entry.get()
        lname = lname_entry.get()
        DoB = dob_entry.get()
        gender = gender_entry.get()
        guardian_names = guardian_names_entry.get()
        guardian_telephone = guardian_telephone_entry.get()
        address = address_entry.get()

        #Assining the values to the Excel sheet
        ws["B" + str(student_row)] = fname
        ws["C" + str(student_row)] = lname
        ws["D" + str(student_row)] = DoB
        ws["E" + str(student_row)] = gender
        ws["F" + str(student_row)] = guardian_names
        ws["G" + str(student_row)] = guardian_telephone
        ws["H" + str(student_row)] = address


        ws['J3'] = num_students + 1

        ws["A" + str(student_row)] = ws['J3'].value
        wb.save(filename="university.xlsx")


    @staticmethod
    def view_details():
        window_details_ID = Toplevel()
        window_details_ID.configure(bg="#393939")

        window_details = Toplevel()
        window_details.configure(bg="#393939")

        student_ID_entry = Entry(window_details_ID)
        student_ID_get = student_ID_entry.get()

        for i in range(2, num_students + 2):
            if ws["A" + str(i)] == student_ID_get:
                student_ID = ws["A" + str(i)].value
                fname = ws["B" + str(i)].value
                lname = ws["B" + str(i)].value
                DoB = ws["B" + str(i)].value
                gender = ws["B" + str(i)].value
                guardian_names = ws["B" + str(i)].value
                guardian_telephone = ws["B" + str(i)].value
                address = ws["B" + str(i)].value
                break

            else:
                print('Student ID not Found!')

        student_ID_details = Label(text= str(student_ID))
        fname_details = Label(text=str(fname))
        lname_details = Label(text=str(lname))
        DoB_details = Label(text=str(DoB))
        gender_details = Label(text=str(gender))
        guardian_names_details = Label(text=str(guardian_names))
        guardian_telephone_details = Label(text=str(guardian_telephone))
        address_details = Label(text=str(address))

        student_ID_details_lbl = Label(text= "Student ID:")
        fname_details_lbl = Label(text="Student ID:")
        lname_details_lbl = Label(text="Student ID:")
        DoB_details_lbl = Label(text="Student ID:")
        gender_details_lbl = Label(text="Student ID:")
        guardian_details_lbl = Label(text="Student ID:")
        guardian_telephone_lbl = Label(text="Student ID:")
        address_details_lbl = Label(text="Student ID:")

        student_ID_details_lbl.grid(row=0, column=0)
        fname_details_lbl.grid(row=1, column=0)
        lname_details_lbl.grid(row=2, column=0)
        DoB_details_lbl.grid(row=3, column=0)
        gender_details_lbl.grid(row=4, column=0)
        guardian_details_lbl.grid(row=5, column=0)
        guardian_telephone_lbl.grid(row=6, column=0)
        address_details_lbl.grid(row=7, column=0)

        student_ID_details.grid(row= 0, column= 1)
        fname_details.grid(row=1, column=1)
        lname_details.grid(row=2, column=1)
        DoB_details.grid(row=3, column=1)
        gender_details.grid(row=4, column=1)
        guardian_names_details.grid(row=5, column=1)
        guardian_telephone_details.grid(row=6, column=1)
        address_details.grid(row=7, column=1)



font_style_title = tkFont.Font(family= "cobel light", size= 20)
font_style_button = tkFont.Font(family= "cobel light", size= 15)


welcome_lbl = Label(root, text= "Welcome to the University", font= font_style_title, bg="#000000", foreground= "white"  )


register_student_button = Button(root, text= "Register Student", width=20, font= font_style_button, bg="#393939", foreground= "white" , command= student_functions.register_student, borderwidth=0, padx= 2, pady= 2)
view_student_details_button = Button(root,text= "View Student Details", width=20, font= font_style_button, bg="#393939", foreground= "white", command = student_functions.view_details, borderwidth=0, padx= 2, pady= 2)
add_course_button = Button(root,text= "Add a Course", width=20, font= font_style_button, bg="#393939", foreground= "white", borderwidth=0 , padx= 2, pady= 2)
view_course_details_button = Button(root,text= "View Course Details", width=20, font= font_style_button, bg="#393939", foreground= "white", borderwidth=0 , padx= 2, pady= 2)
add_student_to_course_button = Button(root,text= "Add student to a Course", width=20, font= font_style_button, bg="#393939", foreground= "white", borderwidth=0 , padx= 2, pady= 2)
add_club_button = Button(root,text= "Add a Club", width=20, font= font_style_button, bg="#393939", foreground= "white", borderwidth=0, padx= 2, pady= 2 )
view_club_details_button = Button(root,text= "View Club Details", width=20, font= font_style_button, bg="#393939", foreground= "white", borderwidth=0, padx= 2, pady= 2 )
add_student_to_club_button = Button(root,text= "Add student to Club", width=20, font= font_style_button, bg="#393939", foreground= "white", borderwidth=0, padx= 2, pady= 2 )

welcome_lbl.grid(columnspan=6)

register_student_button.grid(row=1, column=0)
view_student_details_button.grid(row=1, column=1)
add_course_button.grid(row=2, column=0)
view_course_details_button.grid(row=2, column=1)
add_student_to_course_button.grid(row=3, column=0)
add_club_button.grid(row=3, column=1)
view_club_details_button.grid(row=4, column=0)
add_student_to_club_button.grid(row=4, column=1)





root.mainloop()