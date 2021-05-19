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
ws_student_psswd = wb["student_pswd"]

num_students = ws["J3"].value
student_row = num_students + 2

num_courses = ws_courses["F4"].value
course_row = num_courses + 2

num_student_courses = ws_student_courses["L4"].value
student_course_row = num_student_courses + 2

num_student_clubs = ws_student_clubs["H4"].value
student_club_row = num_student_clubs + 2

num_student_psswd = ws_student_psswd["G6"].value
num_student_psswd_row = num_student_psswd + 2



column_headers = ["A", "B", "C", "D", "E", "F","G", "H","I"]

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

root = Tk()
root.configure(bg="#2e2e2d")
root.title("Welcome to the University")
# root.iconbitmap('D:\download.png')


font_style_popup_button = tkFont.Font(family= "corbel light", size=15)
font_style_main_entry = tkFont.Font(family= "corbel light", size= 20)
font_style_user_input_lbl = tkFont.Font(family= "corbel light", size= 13)
font_style_submit_button = tkFont.Font(family= "corbel light", size = 15, weight= "bold")
font_style_title = tkFont.Font(family= "corbel light", size= 40)
font_style_button = tkFont.Font(family= "corbel light", size= 20)
font_style_welcome_frame_title = tkFont.Font(family= "corbel", size=30 )
font_style_choice = tkFont.Font(family= "corbel light", size=18)
font_style_enter_button = tkFont.Font(family= "cobel light", size= 13)
font_style_passwd_entry_field = tkFont.Font(family= "cobel light", size= 13)

def home():
    global welcome_lbl, student_button, teacher_button, admin_button, parent_button, choice_lbl

    welcome_lbl = Label(root, text= "UNIVERSITY SYSTEM", font= font_style_title, bg="#2e2e2d", foreground= "white"  )
    choice_lbl = Label(root, text= "PLEASE CHOOSE YOUR POSITION:", font= font_style_choice, bg="#2e2e2d", foreground= "white")

    student_button = Button(text= "STUDENT", font= font_style_button, bg="#545352", foreground= "#ed9339", command= student_admission_number_and_pswd, borderwidth= 0, width= 9)
    teacher_button = Button(text= "TEACHER", font= font_style_button, bg="#545352", foreground= "#ed9339", borderwidth= 0, width= 9)
    admin_button = Button(text= "ADMIN", font= font_style_button, bg="#545352", foreground= "#ed9339", command= admin_button_root_password,borderwidth= 0, width= 9)
    parent_button = Button(text="PARENT", font=font_style_button, bg="#545352", foreground="#ed9339", borderwidth=0, width= 9)

    welcome_lbl.grid(columnspan=4)
    choice_lbl.grid(columnspan=4)

    student_button.grid(row=5, column=0, pady= 20, padx= 10)
    teacher_button.grid(row=5, column=1, pady= 20, padx=10)
    admin_button.grid(row=5, column=2, pady= 20, padx=10)
    parent_button.grid(row= 5, column= 3, pady= 20, padx=10)


class second_screen_students:

    @staticmethod
    def courses():
        welcome_lbl.grid_forget()
        course_button.grid_forget()
        credentials_button.grid_forget()
        view_details_button.grid_forget()
        clubs_button.grid_forget()
        back_button.grid_forget()

        def back():
            register_button.grid_forget()
            view_grades_button.grid_forget()
            disenroll_button.grid_forget()
            back_button_courses.grid_forget()
            course_details_button.grid_forget()

            student_button_root()


        #THIS IS THE SECTION FOR THE STUDENTS TO REGISTER FOR A COURSE
        def register():

            course_register_window = Toplevel()
            course_register_window.configure(bg="#2e2e2d")
            course_register_window.title('Register')

            student_ID_lbl = Label(course_register_window, text="Student ID", font=font_style_user_input_lbl, bg="#2e2e2d",foreground="white")
            course_ID_lbl = Label(course_register_window, text="Course ID", font=font_style_user_input_lbl, bg="#2e2e2d", foreground="white")

            student_ID_entry = Entry(course_register_window, font=font_style_user_input_lbl, bg="#393939", foreground= "white")
            course_ID_entry = Entry(course_register_window, font=font_style_user_input_lbl, bg="#393939", foreground= "white")

            student_ID_lbl.grid(row=0, column=0, padx= 10, pady= 10)
            course_ID_lbl.grid(row=1, column=0, padx= 10, pady= 10)

            student_ID_entry.grid(row=0, column=1, padx= 10, pady= 10)
            course_ID_entry.grid(row=1, column=1, padx= 10, pady= 10)

            def enter():
                student_ID = int(student_ID_entry.get())
                course_ID = int(course_ID_entry.get())
                courses.add_student_courses(student_ID, course_ID)

                registered_lbl = Label(course_register_window,text= "REGISTERED", bg="#2e2e2d",foreground="white")
                registered_lbl.grid(row= 3, column= 1)

            def back():
                course_register_window.destroy()

            Enter_button = Button(course_register_window, text="Enter", font=font_style_enter_button, command=enter, bg="#1aeb8d", foreground= "black", width= 19)
            Enter_button.grid(row= 2, column= 1, padx=10, pady=10)

            back_button = Button(course_register_window, text= "Back", font= font_style_enter_button, command= back, bg="#e84d1a", foreground= "white", width= 10)
            back_button.grid(row= 2, column= 0, padx=10, pady=10)

        register_button = Button(root, text= "ENROLL",font= font_style_button, command= register, borderwidth= 0, bg="#545352", foreground= "white", width= 12)
        register_button.grid(row= 0, column= 0, padx= 10, pady= 10)


        #THIS IS THE SECTION TO ALLOW STUDENTS TO VIEW THEIR Grades
        def view_grades():
            view_grades_window = Toplevel()
            view_grades_window.configure(bg="#2e2e2d")
            view_grades_window.title('Grades')

            student_ID_lbl = Label(view_grades_window, text="Student ID", font=font_style_user_input_lbl, bg="#2e2e2d",foreground="white")
            course_ID_lbl = Label(view_grades_window, text="Course ID", font=font_style_user_input_lbl, bg="#2e2e2d", foreground="white")

            student_ID_entry = Entry(view_grades_window, font=font_style_user_input_lbl, bg="#393939", foreground= "white")
            course_ID_entry = Entry(view_grades_window, font=font_style_user_input_lbl, bg="#393939", foreground= "white")

            student_ID_lbl.grid(row=0, column=0, padx= 10, pady= 10)
            course_ID_lbl.grid(row=1, column=0, padx= 10, pady= 10)

            student_ID_entry.grid(row=0, column=1, padx= 10, pady= 10)
            course_ID_entry.grid(row=1, column=1, padx= 10, pady= 10)

            def enter():
                student_ID = int(student_ID_entry.get())
                course_ID = int(course_ID_entry.get())
                grade_list = courses.view_grades(student_ID, course_ID)

                g1_lbl = Label(view_grades_window, text = "Term 1:", bg="#393939", foreground="white")
                g2_lbl = Label(view_grades_window, text = "Term 2:", bg="#393939", foreground="white")
                g3_lbl = Label(view_grades_window, text = "Term 3:", bg="#393939", foreground="white")
                g4_lbl = Label(view_grades_window, text = "Term 4:", bg="#393939", foreground="white")
                g5_lbl = Label(view_grades_window, text = "Term 5:", bg="#393939", foreground="white")

                g1_result = Label(view_grades_window, text= grade_list[0], bg="#393939", foreground="white")
                g2_result = Label(view_grades_window, text= grade_list[1], bg="#393939", foreground="white")
                g3_result = Label(view_grades_window, text= grade_list[2], bg="#393939", foreground="white")
                g4_result = Label(view_grades_window, text= grade_list[3], bg="#393939", foreground="white")
                g5_result = Label(view_grades_window, text= grade_list[4], bg="#393939", foreground="white")

                g1_lbl.grid(row= 2, column= 0, padx= 10, pady= 10)
                g2_lbl.grid(row= 3, column= 0, padx= 10, pady= 10)
                g3_lbl.grid(row= 4, column= 0, padx= 10, pady= 10)
                g4_lbl.grid(row= 5, column= 0, padx= 10, pady= 10)
                g5_lbl.grid(row= 6, column= 0, padx= 10, pady= 10)

                g1_result.grid(row= 2, column= 1, padx= 10, pady= 10)
                g2_result.grid(row= 3, column= 1, padx= 10, pady= 10)
                g3_result.grid(row= 4, column= 1, padx= 10, pady= 10)
                g4_result.grid(row= 5, column= 1, padx= 10, pady= 10)
                g5_result.grid(row= 6, column= 1, padx= 10, pady= 10)

            def back():
                view_grades_window.destroy()

            Enter_button = Button(view_grades_window, text="Enter", font=font_style_enter_button, command=enter, bg="#1aeb8d", foreground= "black", width= 19)
            Enter_button.grid(row= 7, column= 1, padx=10, pady=10)

            back_button = Button(view_grades_window, text= "Back", font= font_style_enter_button, command= back, bg="#e84d1a", foreground= "white", width= 10)
            back_button.grid(row= 7, column= 0, padx=10, pady=10)

        view_grades_button = Button(root, text= "GRADES",font= font_style_button, command= view_grades, borderwidth= 0, bg="#545352", foreground= "white", width= 12)
        view_grades_button.grid(row= 0, column= 1, padx= 10, pady= 10)


        #THIS IS THE SECTION TO ALLOW STUDENTS TO UN-REGISTER FROM A COURSE
        def disenroll() :
            course_disenroll_window = Toplevel()
            course_disenroll_window.configure(bg="#2e2e2d")
            course_disenroll_window.title('Disenroll')

            student_ID_lbl = Label(course_disenroll_window, text="Student ID", font=font_style_user_input_lbl,bg="#2e2e2d", foreground="white")
            course_ID_lbl = Label(course_disenroll_window, text="Course ID", font=font_style_user_input_lbl,bg="#2e2e2d", foreground="white")

            student_ID_entry = Entry(course_disenroll_window, font=font_style_user_input_lbl, bg="#393939",foreground="white")
            course_ID_entry = Entry(course_disenroll_window, font=font_style_user_input_lbl, bg="#393939",foreground="white")

            student_ID_lbl.grid(row=0, column=0, padx=10, pady=10)
            course_ID_lbl.grid(row=1, column=0, padx=10, pady=10)

            student_ID_entry.grid(row=0, column=1, padx=10, pady=10)
            course_ID_entry.grid(row=1, column=1, padx=10, pady=10)

            def enter():
                student_ID = int(student_ID_entry.get())
                course_ID = int(course_ID_entry.get())
                courses.remove_student_courses(student_ID, course_ID)

            def back():
                course_disenroll_window.destroy()

            Enter_button = Button(course_disenroll_window, text="Enter", font=font_style_enter_button, command=enter,bg="#1aeb8d", foreground="black", width=19)
            Enter_button.grid(row=2, column=1, padx=10, pady=10)

            back_button = Button(course_disenroll_window, text="Back", font=font_style_enter_button, command=back,bg="#e84d1a", foreground="white", width=10)
            back_button.grid(row=2, column=0, padx=10, pady=10)

        disenroll_button = Button(root, text= "DISENROLL",font= font_style_button, command= disenroll, borderwidth= 0, bg="#545352", foreground= "white", width= 13)
        disenroll_button.grid(row=0, column= 2, padx= 10, pady= 10)

        #THIS IS THE SECTION TO VIEW THE COURSE DETAILS
        def course_details() :
            course_details_window = Toplevel()
            course_details_window.configure(bg="#2e2e2d")
            course_details_window.title('Register')

            course_ID_lbl = Label(course_details_window, text="Course ID", font=font_style_user_input_lbl,bg="#2e2e2d", foreground="white")

            course_ID_entry = Entry(course_details_window, font=font_style_user_input_lbl, bg="#393939",foreground="white")

            course_ID_lbl.grid(row=1, column=0, padx=10, pady=10)

            course_ID_entry.grid(row=1, column=1, padx=10, pady=10)

            def enter():
                course_id = int(course_ID_entry.get())

                course_list = courses.view_course_details(course_id)

                course_name_lbl = Label(course_details_window, text="Course Name:", bg="#2e2e2d", foreground="white")
                course_duration_lbl = Label(course_details_window, text="Course Duration:", bg="#2e2e2d", foreground="white")
                prerequisites_lbl = Label(course_details_window, text="Prerequisites:", bg="#2e2e2d", foreground="white")
                instructors_lbl = Label(course_details_window, text="Instructors:", bg="#2e2e2d", foreground="white")

                course_name_results = Label(course_details_window, text=course_list[1], bg="#2e2e2d", foreground="white")
                course_duration_results = Label(course_details_window, text=course_list[2], bg="#2e2e2d", foreground="white")
                prerequisites_results = Label(course_details_window, text=course_list[3], bg="#2e2e2d", foreground="white")
                instructors_results = Label(course_details_window, text=course_list[4], bg="#2e2e2d", foreground="white")

                course_name_lbl.grid(row=2, column=0, padx=10, pady=10, sticky= W)
                course_duration_lbl.grid(row=3, column=0, padx=10, pady=10, sticky= W)
                prerequisites_lbl.grid(row=4, column=0, padx=10, pady=10, sticky= W)
                instructors_lbl.grid(row=5, column=0, padx=10, pady=10, sticky= W)

                course_name_results.grid(row=2, column=1, padx=10, pady=10, sticky= W)
                course_duration_results.grid(row=3, column=1, padx=10, pady=10, sticky= W)
                prerequisites_results.grid(row=4, column=1, padx=10, pady=10, sticky= W)
                instructors_results.grid(row=5, column=1, padx=10, pady=10, sticky= W)

            def back():
                course_details_window.destroy()

            Enter_button = Button(course_details_window, text="Enter", font=font_style_enter_button, command=enter,bg="#1aeb8d", foreground="black", width=19)
            Enter_button.grid(row=6, column=1, padx=10, pady=10)

            back_button = Button(course_details_window, text="Back", font=font_style_enter_button, command=back,bg="#e84d1a", foreground="white", width=10)
            back_button.grid(row=6, column=0, padx=10, pady=10)

        course_details_button = Button(root, text= "DETAILS",font= font_style_button, command= course_details, borderwidth= 0, bg="#545352", foreground= "white", width= 12)
        course_details_button.grid(row=0, column=3, padx=10, pady=10)



        #THIS IS THE BACK BUTTON
        back_button_courses = Button(root, text= "Back", font= font_style_enter_button, command = back, borderwidth= 0, bg="#e84d1a",foreground="white", width= 86)
        back_button_courses.grid(columnspan= 4, padx= 10, pady= 10)



#ADD THE COMMANDS TO THE BUTTONS HERE
def student_button_root():
    global course_button, credentials_button, view_details_button, clubs_button, back_button

    def home_buttons_disappear():
        student_button.grid_forget()
        teacher_button.grid_forget()
        admin_button.grid_forget()
        parent_button.grid_forget()
        choice_lbl.grid_forget()

    def back():
        welcome_lbl.grid_forget()
        course_button.grid_forget()
        credentials_button.grid_forget()
        view_details_button.grid_forget()
        clubs_button.grid_forget()
        back_button.grid_forget()
        greeting_lbl.grid_forget()

        home()

    home_buttons_disappear()

    greeting_lbl = Label(root, text= f"Hello {student_name}, what is your task related to:", font = font_style_popup_button, bg= "#2e2e2d", foreground= "white")


    #COMPLETE THE COMMANDS IN THESE BUTTONS

    #courses_button
    course_button = Button(root, text= "Courses", font= font_style_button,borderwidth= 0, width= 13, bg="#545352",foreground="white", command= second_screen_students.courses)
    #Credentials
    credentials_button = Button(root, text= "Credentials", font= font_style_button,  borderwidth= 0, width= 13, bg="#545352",foreground="white")
    #view_details
    view_details_button = Button(root, text= "View Details", font= font_style_button,  borderwidth= 0, width= 13, bg="#545352",foreground="white")
    #clubs button
    clubs_button = Button(root, text= "Clubs", font= font_style_button,borderwidth= 0, width= 13, bg="#545352",foreground="white")
    #back Button
    back_button = Button(root, text= "Back", font= font_style_button, borderwidth= 0, width= 62, bg="#e84d1a",foreground="white", command= back)

    greeting_lbl.grid(columnspan= 5, sticky= "NSWE", padx= 10, pady= 10)

    course_button.grid(row= 3, column= 0, padx= 10, pady= 10)
    credentials_button.grid(row= 3, column= 1, padx= 10, pady= 10)
    view_details_button.grid(row= 3, column= 2, padx= 10, pady= 10)
    clubs_button.grid(row= 3, column= 3, padx= 10, pady= 10)
    back_button.grid(columnspan= 4, padx= 10, pady= 10)

def student_admission_number_and_pswd():
    global student_name

    passwd_frame_student = Frame(root, bg="#4f4f4d")
    passwd_frame_student.grid(columnspan=4, padx=10, pady=10)

    admission_number_lbl = Label(passwd_frame_student, text="INDEX NO.", font=font_style_user_input_lbl,bg="#4f4f4d", foreground="#FFFFFF")
    admission_number_entry = Entry(passwd_frame_student, bg="#2e2e2d", foreground="#FFFFFF", borderwidth=0, width=74,font=font_style_passwd_entry_field)

    password_label_stdnt = Label(passwd_frame_student, text="PASSWORD", font=font_style_user_input_lbl,bg="#4f4f4d", foreground="#FFFFFF")
    password_entry_stdnt = Entry(passwd_frame_student, bg="#2e2e2d", foreground="#FFFFFF", borderwidth=0, width=74,font=font_style_passwd_entry_field)

    admission_number_lbl.grid(row=1, column= 0, pady= 10)
    admission_number_entry.grid(row=1, column =1, padx =10)

    password_label_stdnt.grid(row= 2,column= 0, padx= 10)
    password_entry_stdnt.grid(row= 2, column= 1, padx= 10, pady= 10)

    def password_verify():
        global student_name

        student_admission_number = int(admission_number_entry.get())
        print(student_admission_number)
        student_password = password_entry_stdnt.get()

        for i in range(2, num_student_psswd + 2):
            if ws_student_psswd["A" + str(i)].value == student_admission_number and ws_student_psswd["B" + str(i)].value == student_password:

                admission_number_lbl.grid_forget()
                admission_number_entry.grid_forget()
                password_label_stdnt.grid_forget()
                password_entry_stdnt.grid_forget()
                passwd_frame_student.grid_forget()
                enter_button.grid_forget()
                print('correct')

                student_name = students.get_name_for_password(student_admission_number)
                print(student_name)

                student_button_root()


            else:
                admission_number_entry.delete(0,100)
                password_entry_stdnt.delete(0,100)

                admission_number_entry.insert(0, "Incorrect")
                password_entry_stdnt.insert(0, "Incorrect")


    enter_button = Button(passwd_frame_student, text="ENTER", font=font_style_enter_button, borderwidth=0, width=82,command=password_verify, bg="#1aeb8d")
    enter_button.grid(columnspan= 4, pady= 10, padx= 10)





def teacher_button_root():
    pass

#Features that Teachers can Access
class teacher_functions:
    pass





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

class admin_second_screen:

    @staticmethod
    def student_page():

        admin_student_window = Toplevel()
        admin_student_window.configure(bg="#2e2e2d")
        admin_student_window.title("STUDENTS")

        register_student_button = Button(admin_student_window, text="Register Student", width=20, font=font_style_button, bg="#545352", foreground="white", command=admin_functions.register_students, borderwidth=0)
        view_student_details_button = Button(admin_student_window, text="View Student Details", width=20, font=font_style_button,bg="#545352", foreground="white", command=admin_functions.view_details_get_entry, borderwidth=0)
        remove_student_button = Button(admin_student_window, text="Remove a Student", width=20, font=font_style_button, bg="#545352",foreground="white", borderwidth=0, command=admin_functions.remove_student)
        view_grades_button = Button(admin_student_window, text="View Grades", width=20, font=font_style_button, bg="#545352",foreground="white", borderwidth=0)


        register_student_button.grid(row=9, column=0, padx=7, pady=7)
        view_student_details_button.grid(row=9, column=1, padx=7, pady=7)
        remove_student_button.grid(row=10, column=0, padx=7, pady=7)
        view_grades_button.grid(row=10, column=1, padx=7, pady=7)

        def back():
            admin_student_window.destroy()

        back_button = Button(admin_student_window, text="Back", width=53, font=font_style_submit_button, bg="#e84d1a",foreground="white", borderwidth=0, command= back)
        back_button.grid(columnspan= 2, pady =10, padx= 10)

    @staticmethod
    def teacher_page():
        pass

    @staticmethod
    def course_page():
        pass

    @staticmethod
    def clubs_page():
        pass


def admin_button_root_rest():

    def home_buttons_disappear():
        student_button.grid_forget()
        teacher_button.grid_forget()
        admin_button.grid_forget()
        parent_button.grid_forget()
        choice_lbl.grid_forget()

    home_buttons_disappear()


    task_lbl = Label(root, text= "WHAT IS YOUR TASK RELATED TO:", font = font_style_popup_button, bg= "#2e2e2d", foreground= "white")

    Students_button = Button(root, text= "STUDENTS", width=20, font=font_style_button, bg="#545352",foreground="white", command=admin_second_screen.student_page , borderwidth=0)
    Teachers_button = Button(root, text= "TEACHERS", width=20, font=font_style_button, bg="#545352",foreground="white", borderwidth=0)
    Courses_button = Button(root, text= "COURSES", width=20, font=font_style_button, bg="#545352",foreground="white", borderwidth=0)
    Clubs_button = Button(root, text= "CLUBS", width=20, font=font_style_button, bg="#545352",foreground="white", borderwidth=0)


    task_lbl.grid(columnspan = 4)
    Students_button.grid(row=10, column=0, padx=7, pady=10)
    Teachers_button.grid(row=10, column=1, padx=7, pady=10)
    Courses_button.grid(row=10, column=2, padx=7, pady=10)
    Clubs_button.grid(row=10, column=3, padx=7, pady=10)


    def admin_screen_back():
        welcome_lbl.grid_forget()
        task_lbl.grid_forget()
        Students_button.grid_forget()
        Teachers_button.grid_forget()
        Courses_button.grid_forget()
        Clubs_button.grid_forget()
        back_button.grid_forget()

        home()

    back_button = Button(root, text="BACK", width=107, font=font_style_submit_button, bg="#e84d1a", foreground="white",borderwidth=0, command= admin_screen_back)
    back_button.grid(columnspan=4, pady=10)

def admin_button_root_password():

    passwd_frame = Frame(root,bg= "#4f4f4d" )
    passwd_frame.grid(columnspan= 4, padx= 10, pady= 10)

    password_label = Label(passwd_frame, text= "PLEASE ENTER YOUR PASSWORD", font= font_style_user_input_lbl, bg="#4f4f4d", foreground= "#FFFFFF")
    password_entry = Entry(passwd_frame, bg="#2e2e2d", foreground= "#FFFFFF",borderwidth= 0, width = 74, font=font_style_passwd_entry_field)

    password_label.grid(columnspan= 4, pady= 10)
    password_entry.grid(columnspan= 3, padx= 10)


    def password_verify():
        password= '12'
        entered_password = password_entry.get()

        if entered_password == password:
            print('correct')
            admin_button_root_rest()

            password_entry.delete(0,100)
            password_entry.insert(0, "correct")

            password_label.grid_forget()
            password_entry.grid_forget()
            enter_button.grid_forget()
            passwd_frame.grid_forget()

        else:
            print('incorrect')
            password_entry.delete(0, 100)
            password_entry.insert(0, "Incorrect")

    enter_button = Button(passwd_frame, text="ENTER", font=font_style_enter_button, borderwidth=0, width=13, command= password_verify, bg="#1aeb8d")
    enter_button.grid(row=1, column=3, pady= 10, padx= 10)




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
