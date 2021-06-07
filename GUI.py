from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
import os
import openpyxl as xl
import time

from student_functions import students
from student_functions import courses
from student_functions import clubs
from student_functions import teachers
from student_functions import notifications

wb = xl.load_workbook("university.xlsx")
ws = wb['students']
ws_courses = wb['courses']
ws_student_courses = wb['student_courses']
ws_student_clubs = wb['student_clubs']
ws_student_psswd = wb["student_pswd"]
ws_teachers = wb["Teachers"]
ws_teacher_passwd = wb["teacher_psswd"]
ws_notifications = wb["notifications"]

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

num_teachers = ws_teachers["H4"].value
num_teachers_row = num_teachers + 2

num_teacher_passwd = ws_teacher_passwd["F4"].value
teacher_passwd_row = num_teacher_passwd + 2

column_headers = ["A", "B", "C", "D", "E", "F","G", "H","I"]

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

root = Tk()
root.title("UNIVERISTY SYSTEM")


# Accent colours
button_colour1 = "#2b2b2b"
button_colour2 = "#595959"
# side_bar_color =
bg_colour1 = "#393939"
dark_bg = "#1C1C1C"
sidebar_button_hover_color = '#636363'
enter_button_hover_color = "#63ed28"
back_button_hover_color = "#eb6709"
enter_button_color = "#1aeb8d"
back_button_color = "#e84d1a"

root.configure(bg=dark_bg)

font_style_popup_button = tkFont.Font(family= "corbel light", size=15)
font_style_main_entry = tkFont.Font(family= "corbel light", size= 20)
corbel_13 = tkFont.Font(family="corbel light", size= 13)
font_style_submit_button = tkFont.Font(family= "corbel light", size = 15, weight= "bold")
font_style_title = tkFont.Font(family= "corbel light", size= 40)
corbel_15 = tkFont.Font(family="corbel light", size= 15)
corbel_bold_13 = tkFont.Font(family="corbel bold", size= 13)
font_style_welcome_frame_title = tkFont.Font(family= "corbel", size=30 )
font_style_choice = tkFont.Font(family= "corbel light", size=18)
font_style_enter_button = tkFont.Font(family= "cobel light", size= 13)
font_style_passwd_entry_field = tkFont.Font(family= "cobel light", size= 13)

close_eye_image = PhotoImage(file='close_eye.png')
open_eye_image = PhotoImage(file='open_eye.png')

class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self, master=master, **kw)
        self.default_bg = self["bg"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['bg'] = self['activebackground']

    def on_leave(self, e):
        self['bg'] = self.default_bg

def create_frame(popup, colour, row=0, column=0, padx=20, pady=20, sticky=NSEW, columnspan=1):
    frame = LabelFrame(popup, padx=padx, pady=pady, borderwidth=0)
    frame.configure(bg=colour)
    frame.grid(row=row, column=column, sticky=sticky, columnspan=columnspan)
    return frame

def home():
    global welcome_lbl, student_button, teacher_button, admin_button, parent_button, choice_lbl, welcome_lbl_frame

    home_buttons_frame = create_frame(root, bg_colour1)
    welcome_lbl_frame = create_frame(root, dark_bg, row=0, column=1, padx=150)

    welcome_lbl = Label(welcome_lbl_frame, text= "UNIVERSITY SYSTEM", font= font_style_title, bg=dark_bg, foreground= "white"  )

    student_button = HoverButton(home_buttons_frame, text= "STUDENT ", font= corbel_15, bg=bg_colour1, foreground="#ed9339", command= student_admission_number_and_pswd, borderwidth= 0, width= 9, activebackground= sidebar_button_hover_color)
    teacher_button = HoverButton(home_buttons_frame, text= "TEACHER  ", font= corbel_15, bg=bg_colour1, foreground="#ed9339", command=teacher_password_check, borderwidth= 0, width= 9, activebackground= sidebar_button_hover_color)
    admin_button = HoverButton(home_buttons_frame, text= "ADMIN       ", font= corbel_15, bg=bg_colour1, foreground="#ed9339", command= admin_button_root_password, borderwidth= 0, width= 9, activebackground= sidebar_button_hover_color)
    parent_button = HoverButton(home_buttons_frame, text="PARENT     ", font=corbel_15, bg=bg_colour1, foreground="#ed9339", borderwidth=0, width= 9, activebackground= sidebar_button_hover_color)
    random_button = Button(home_buttons_frame,bg=bg_colour1, borderwidth=0, height=20)
    settings_button = HoverButton(home_buttons_frame, text="SETTINGS", font=corbel_15, bg=button_colour2, foreground='white', borderwidth=0, width= 9, activebackground= button_colour1)

    welcome_lbl.grid(row=1, column=1)
    welcome_lbl_frame.grid_rowconfigure(0, weight=1)
    welcome_lbl_frame.grid_rowconfigure(2, weight=1)
    welcome_lbl_frame.grid_columnconfigure(0, weight=1)
    welcome_lbl_frame.grid_columnconfigure(2, weight=1)

    student_button.grid(row=1, column=0, padx= 10)
    teacher_button.grid(row=2, column=0, padx=10)
    admin_button.grid(row=3, column=0, padx=10)
    parent_button.grid(row= 4, column= 0, padx=10)
    random_button.grid(row=5, column=0, padx=10)
    settings_button.grid(row=6, column=0, padx=10, sticky=W)


class second_screen_students:

    @staticmethod
    def courses():
        student_buttons_frame.grid_forget()

        def back():
            register_button.grid_forget()
            view_grades_button.grid_forget()
            disenroll_button.grid_forget()
            back_button_courses.grid_forget()
            course_details_button.grid_forget()

            student_button_root()

        courses_frame = create_frame(root, dark_bg, row=0, column=1)

        #THIS IS THE SECTION FOR THE STUDENTS TO REGISTER FOR A COURSE
        def register():
            back_button_root.grid_forget()

            register_frame = create_frame(root, "#2e2e2d", row=0, column=2)

            courses_lbl = Label(register_frame, text="COURSES", font=corbel_13, bg="#2e2e2d", fg='white')
            courses_lbl.grid(row=0, column=0)

            options = courses.view_all_course_names()
            print(options)

            clicked = StringVar()
            clicked.set('PLEASE CHOOSE THE COURSE')
            course_list = OptionMenu(register_frame, clicked, *options)
            course_list.config(bg=dark_bg, fg='white', width=26)
            course_list.grid(row=0, column=1)

            def enter():
                course_name = clicked.get()
                courses.add_student_courses(student_admission_number, course_name)
                notifications.add_notification_details(student_admission_number, course_name)

                def registered_lbl():
                    registered_lbl = Label(register_frame, text= "REGISTERED", bg="#2e2e2d", foreground="white", font=corbel_13)
                    registered_lbl.grid(row= 5, columnspan=2)

                registering_lbl = Label(register_frame, text="REGISTERING...", font=corbel_13, bg="#2e2e2d", foreground="white")
                registering_lbl.grid(row=3, columnspan=2)

                course_register_progress_bar = ttk.Progressbar(register_frame, orient=HORIZONTAL, length=300, mode="determinate")
                course_register_progress_bar.grid(row=4, columnspan=2)


                for i in range(5):
                    course_register_progress_bar['value'] += 20
                    root.update_idletasks()
                    time.sleep(1)

                registered_lbl()

            def back():
                register_frame.grid_forget()

            Enter_button = HoverButton(register_frame, text="Enter", font=font_style_enter_button, command=enter, bg="#1aeb8d", foreground= "black", width= 19, borderwidth=0, activebackground=enter_button_hover_color)
            Enter_button.grid(row= 2, column= 1, padx=10, pady=10)

            back_button = HoverButton(register_frame, text= "Back", font= font_style_enter_button, command= back, bg="#e84d1a", foreground= "white", width= 10, borderwidth=0, activebackground=back_button_hover_color)
            back_button.grid(row= 2, column= 0, padx=10, pady=10)

        register_button = HoverButton(courses_frame, text= "ENROLL", font= corbel_15, command= register, borderwidth= 0, bg=bg_colour1, foreground="white", width= 71, activebackground=sidebar_button_hover_color)
        register_button.grid(row= 0, columnspan=2, padx= 10, pady= 10)


        #THIS IS THE SECTION TO ALLOW STUDENTS TO VIEW THEIR Grades
        def view_grades():
            view_grades_frame = create_frame(root, "#2e2e2d", row=0, column=2)

            student_ID_lbl = Label(view_grades_frame, text="Student ID", font=corbel_13, bg="#2e2e2d", foreground="white")
            course_ID_lbl = Label(view_grades_frame, text="Course ID", font=corbel_13, bg="#2e2e2d", foreground="white")

            student_ID_entry = Entry(view_grades_frame, font=corbel_13, bg=dark_bg, foreground="white", borderwidth=0)
            course_ID_entry = Entry(view_grades_frame, font=corbel_13, bg=dark_bg, foreground="white", borderwidth=0)

            student_ID_lbl.grid(row=0, column=0, padx= 10, pady= 10)
            course_ID_lbl.grid(row=1, column=0, padx= 10, pady= 10)

            student_ID_entry.grid(row=0, column=1, padx= 10, pady= 10)
            course_ID_entry.grid(row=1, column=1, padx= 10, pady= 10)

            def enter():
                student_ID = int(student_ID_entry.get())
                course_ID = int(course_ID_entry.get())
                grade_list = courses.view_grades(student_ID, course_ID)

                g1_lbl = Label(view_grades_frame, text = "Term 1:", bg="#2e2e2d", foreground="white")
                g2_lbl = Label(view_grades_frame, text = "Term 2:", bg="#2e2e2d", foreground="white")
                g3_lbl = Label(view_grades_frame, text = "Term 3:", bg="#2e2e2d", foreground="white")
                g4_lbl = Label(view_grades_frame, text = "Term 4:", bg="#2e2e2d", foreground="white")
                g5_lbl = Label(view_grades_frame, text = "Term 5:", bg="#2e2e2d", foreground="white")

                g1_result = Label(view_grades_frame, text= grade_list[0], bg="#2e2e2d", foreground="white")
                g2_result = Label(view_grades_frame, text= grade_list[1], bg="#2e2e2d", foreground="white")
                g3_result = Label(view_grades_frame, text= grade_list[2], bg="#2e2e2d", foreground="white")
                g4_result = Label(view_grades_frame, text= grade_list[3], bg="#2e2e2d", foreground="white")
                g5_result = Label(view_grades_frame, text= grade_list[4], bg="#2e2e2d", foreground="white")

                g1_lbl.grid(row= 2, column= 0, padx= 10, pady= 10)
                g2_lbl.grid(row= 3, column= 0, padx= 10, pady= 10)
                g3_lbl.grid(row= 4, column= 0, padx= 10, pady= 10)
                g4_lbl.grid(row= 5, column= 0, padx= 10, pady= 10)
                g5_lbl.grid(row= 6, column= 0, padx= 10, pady= 10)

                g1_result.grid(row= 2, column= 1, padx= 10, pady= 10, sticky=W)
                g2_result.grid(row= 3, column= 1, padx= 10, pady= 1, sticky=W)
                g3_result.grid(row= 4, column= 1, padx= 10, pady= 10, sticky=W)
                g4_result.grid(row= 5, column= 1, padx= 10, pady= 10, sticky=W)
                g5_result.grid(row= 6, column= 1, padx= 10, pady= 10, sticky=W)

            def back():
                view_grades_frame.grid_forget()

            Enter_button = HoverButton(view_grades_frame, text="Enter", font=font_style_enter_button, command=enter, bg="#1aeb8d", foreground= "black", width= 19, activebackground=enter_button_hover_color, borderwidth=0)
            Enter_button.grid(row= 7, column= 1, padx=10, pady=10)

            back_button = HoverButton(view_grades_frame, text= "Back", font= font_style_enter_button, command= back, bg="#e84d1a", foreground= "white", width= 10, activebackground=back_button_hover_color, borderwidth=0)
            back_button.grid(row= 7, column= 0, padx=10, pady=10)

        view_grades_button = HoverButton(courses_frame, text= "GRADES", font= corbel_15, command= view_grades, borderwidth= 0, bg=bg_colour1, foreground="white", width= 34, activebackground=sidebar_button_hover_color)
        view_grades_button.grid(row= 1, column= 0, padx= 10, pady= 10)


        #THIS IS THE SECTION TO ALLOW STUDENTS TO UN-REGISTER FROM A COURSE
        def disenroll() :
            disenroll_frame = create_frame(root,"#2e2e2d", row=0, column=2)

            student_ID_lbl = Label(disenroll_frame, text="Student ID", font=corbel_13, bg="#2e2e2d", foreground="white")
            course_ID_lbl = Label(disenroll_frame, text="Course ID", font=corbel_13, bg="#2e2e2d", foreground="white")

            student_ID_entry = Entry(disenroll_frame, font=corbel_13, bg=dark_bg, foreground="white", borderwidth=0)
            course_ID_entry = Entry(disenroll_frame, font=corbel_13, bg=dark_bg, foreground="white", borderwidth=0)

            student_ID_lbl.grid(row=0, column=0, padx=10, pady=10)
            course_ID_lbl.grid(row=1, column=0, padx=10, pady=10)

            student_ID_entry.grid(row=0, column=1, padx=10, pady=10)
            course_ID_entry.grid(row=1, column=1, padx=10, pady=10)

            def enter():
                student_ID = int(student_ID_entry.get())
                course_ID = int(course_ID_entry.get())
                courses.remove_student_courses(student_ID, course_ID)

            def back():
                disenroll_frame.grid_forget()

            Enter_button = HoverButton(disenroll_frame, text="Enter", font=font_style_enter_button, command=enter,bg="#1aeb8d", foreground="black", width=19, borderwidth=0, activebackground=enter_button_hover_color)
            Enter_button.grid(row=2, column=1, padx=10, pady=10)

            back_button = HoverButton(disenroll_frame, text="Back", font=font_style_enter_button, command=back,bg="#e84d1a", foreground="white", width=10, borderwidth=0, activebackground=back_button_hover_color)
            back_button.grid(row=2, column=0, padx=10, pady=10)

        disenroll_button = HoverButton(courses_frame, text= "DISENROLL", font= corbel_15, command= disenroll, borderwidth= 0, bg=bg_colour1, foreground="white", width= 34, activebackground=sidebar_button_hover_color)
        disenroll_button.grid(row=1, column= 1, padx= 10, pady= 10)

        #THIS IS THE SECTION TO VIEW THE COURSE DETAILS
        def course_details() :
            course_details_frame = create_frame(root, "#2e2e2d", row=0, column=2)

            course_ID_lbl = Label(course_details_frame, text="Course ID", font=corbel_13, bg="#2e2e2d", foreground="white")
            course_ID_entry = Entry(course_details_frame, font=corbel_13, bg=dark_bg, foreground="white", borderwidth=0)

            course_ID_lbl.grid(row=1, column=0, padx=10, pady=10)
            course_ID_entry.grid(row=1, column=1, padx=10, pady=10)

            def enter():
                course_id = int(course_ID_entry.get())

                course_list = courses.view_course_details(course_id)

                course_name_lbl = Label(course_details_frame, text="Course Name:", bg="#2e2e2d", foreground="white")
                course_duration_lbl = Label(course_details_frame, text="Course Duration:", bg="#2e2e2d", foreground="white")
                prerequisites_lbl = Label(course_details_frame, text="Prerequisites:", bg="#2e2e2d", foreground="white")
                instructors_lbl = Label(course_details_frame, text="Instructors:", bg="#2e2e2d", foreground="white")

                course_name_results = Label(course_details_frame, text=course_list[1], bg="#2e2e2d", foreground="white")
                course_duration_results = Label(course_details_frame, text=course_list[2], bg="#2e2e2d", foreground="white")
                prerequisites_results = Label(course_details_frame, text=course_list[3], bg="#2e2e2d", foreground="white")
                instructors_results = Label(course_details_frame, text=course_list[4], bg="#2e2e2d", foreground="white")

                course_name_lbl.grid(row=2, column=0, padx=10, pady=10, sticky= W)
                course_duration_lbl.grid(row=3, column=0, padx=10, pady=10, sticky= W)
                prerequisites_lbl.grid(row=4, column=0, padx=10, pady=10, sticky= W)
                instructors_lbl.grid(row=5, column=0, padx=10, pady=10, sticky= W)

                course_name_results.grid(row=2, column=1, padx=10, pady=10, sticky= W)
                course_duration_results.grid(row=3, column=1, padx=10, pady=10, sticky= W)
                prerequisites_results.grid(row=4, column=1, padx=10, pady=10, sticky= W)
                instructors_results.grid(row=5, column=1, padx=10, pady=10, sticky= W)

            def back():
                course_details_frame.grid_forget()

            Enter_button = HoverButton(course_details_frame, text="Enter", font=font_style_enter_button, command=enter,bg="#1aeb8d", foreground="black", width=19, borderwidth=0, activebackground=enter_button_hover_color)
            Enter_button.grid(row=6, column=1, padx=10, pady=10)

            back_button = HoverButton(course_details_frame, text="Back", font=font_style_enter_button, command=back,bg="#e84d1a", foreground="white", width=10, borderwidth=0, activebackground=back_button_hover_color)
            back_button.grid(row=6, column=0, padx=10, pady=10)

        course_details_button = HoverButton(courses_frame, text= "DETAILS", font= corbel_15, command= course_details, borderwidth= 0, bg=bg_colour1, foreground="white", width= 71, activebackground=sidebar_button_hover_color)
        course_details_button.grid(row=2,columnspan=2, padx=10, pady=10)



        #THIS IS THE BACK BUTTON
        back_button_courses = HoverButton(courses_frame, text= "BACK", font= font_style_enter_button, command = back, borderwidth= 0, bg="#e84d1a",foreground="white", width= 79, activebackground=back_button_hover_color)
        back_button_courses.grid(row=3,columnspan= 4, padx= 10, pady= 10)

    @staticmethod
    def change_password():
        #THIS IS THE SECTION THAT ALLOWS THE STUDENT TO CHANGE THEIR PASSWORd
        change_password_frame = create_frame(root,"#2e2e2d", row=0, column=2)

        student_ID_lbl = Label(change_password_frame, text="Student ID", font=corbel_13, bg="#2e2e2d", foreground="white")
        student_ID_lbl.grid(row= 0, column=0, padx=10, pady= 10, sticky=W)

        student_ID_entry = Entry(change_password_frame, font=corbel_13, bg="#393939", foreground="white", borderwidth=0)
        student_ID_entry.grid(row= 0, column=1, padx= 10, pady= 10)

        current_password_lbl = Label(change_password_frame, text="Current Passowrd", font=corbel_13, bg="#2e2e2d", foreground="white")
        current_password_lbl.grid(row= 1, column= 0, padx= 10, pady= 10, sticky=W)

        current_password_entry = Entry(change_password_frame, font=corbel_13, bg="#393939", foreground="white", borderwidth=0)
        current_password_entry.grid(row=1, column=1, padx=10, pady=10)

        new_password_lbl = Label(change_password_frame, text="New Password", font=corbel_13, bg="#2e2e2d", foreground="white")
        new_password_lbl.grid(row= 2, column= 0, padx= 10, pady= 10, sticky=W)

        new_password_entry = Entry(change_password_frame, font=corbel_13, bg="#393939", foreground="white", borderwidth=0)
        new_password_entry.grid(row=2, column=1, padx=10, pady=10)

        def back():
            change_password_frame.grid_forget()

        def enter():
            student_ID = student_ID_entry.get()
            current_password = current_password_entry.get()
            new_password = new_password_entry.get()
            print(f"student_ID {student_ID}")
            print(f'current passoword {current_password}')
            print(f"new_password {new_password}")



            final_decision = students.change_password(int(student_ID), current_password, new_password)
            print(f"This is the final decision: {final_decision}")

            if final_decision == False:
                incorrect_lbl = Label(change_password_frame, text="Incorrect", font=corbel_13, bg="#2e2e2d", foreground="white")
                incorrect_lbl.grid(columnspan=2, padx=10, pady=10)

            else:
                changed_lbl = Label(change_password_frame, text="Changed", font=corbel_13, bg="#2e2e2d", foreground="white")
                changed_lbl.grid(columnspan = 2, padx=10, pady= 10)


        Enter_button = HoverButton(change_password_frame, text="Enter", font=font_style_enter_button,bg="#1aeb8d", foreground="black", width=19, command= enter, borderwidth=0, activebackground=enter_button_hover_color)
        Enter_button.grid(row=3, column=1, padx=10, pady=10)

        back_button = HoverButton(change_password_frame, text="Back", font=font_style_enter_button, bg="#e84d1a", foreground="white", width=10, command= back, borderwidth=0, activebackground=back_button_hover_color)
        back_button.grid(row=3, column=0, padx=10, pady=10)

    @staticmethod
    def view_details():
        pass

    @staticmethod
    def clubs():
        pass


#ADD THE COMMANDS TO THE BUTTONS HERE
def student_button_root():
    global course_button, credentials_button, view_details_button, clubs_button, back_button_root, greeting_lbl, student_buttons_frame

    def back():
        student_buttons_frame.grid_forget()

        home()

    passwd_frame_student.grid_forget()


    student_buttons_frame = create_frame(root, dark_bg, row=0, column=1)
    greeting_lbl = Label(student_buttons_frame, text=f"Hello {student_name}, what is your task related to:",font=font_style_popup_button, bg=dark_bg, foreground="white")

    #COMPLETE THE COMMANDS IN THESE BUTTONS

    #courses_button
    course_button = HoverButton(student_buttons_frame, text= "COURSES", font= corbel_15, borderwidth= 0, width= 70, bg=bg_colour1, foreground="white", command= second_screen_students.courses, activebackground=sidebar_button_hover_color)
    #Credentials
    credentials_button = HoverButton(student_buttons_frame, text= "CHANGE PASSWORD", font= corbel_15, borderwidth= 0, width= 70, bg=bg_colour1, foreground="white", command = second_screen_students.change_password, activebackground=sidebar_button_hover_color)
    #view_details
    view_details_button = HoverButton(student_buttons_frame, text= "VIEW DETAILS", font= corbel_15, borderwidth= 0, width= 34, bg=bg_colour1, foreground="white", activebackground=sidebar_button_hover_color)
    #clubs button
    clubs_button = HoverButton(student_buttons_frame, text= "CLUBS", font= corbel_15, borderwidth= 0, width= 34, bg=bg_colour1, foreground="white", activebackground=sidebar_button_hover_color)
    #back Button
    back_button_root = HoverButton(student_buttons_frame, text= "BACK", font= font_style_enter_button, borderwidth= 0, width= 78, bg="#e84d1a",foreground="white", command= back, activebackground=sidebar_button_hover_color)

    greeting_lbl.grid(columnspan=2, sticky= "NSWE", padx= 10, pady= 10)

    course_button.grid(row=1,columnspan=2, padx= 10, pady= 10)
    clubs_button.grid(row=2, column=0, padx=10, pady=10)
    view_details_button.grid(row=2, column=1, padx=10, pady=10)
    credentials_button.grid(row= 3, columnspan=2, padx= 10, pady= 10)

    back_button_root.grid(columnspan= 4, padx= 10, pady= 10)

def student_admission_number_and_pswd():
    global student_name, passwd_frame_student, passwd_frame_student

    welcome_lbl_frame.grid_forget()

    passwd_frame_student = Frame(root, bg="#4f4f4d")
    passwd_frame_student.grid(row=0, column=1, padx=90)
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(2, weight=1)

    instructions_lbl = Label(passwd_frame_student, text="Please enter your Username and Password",font=font_style_popup_button, bg="#4f4f4d", foreground="white")
    instructions_lbl.grid(row=0, columnspan=2, padx=10)

    admission_number_lbl = Label(passwd_frame_student, text="INDEX NO.", font=corbel_13, bg="#4f4f4d", foreground="#FFFFFF")
    admission_number_entry = Entry(passwd_frame_student, bg="#2e2e2d", foreground="#FFFFFF", borderwidth=0, width=55,font=font_style_passwd_entry_field)

    def toggle_password():
        if password_entry_stdnt.cget('show') == "" :
            password_entry_stdnt.config(show="*")
            show_hide_password_button['image'] = close_eye_image
        else:
            password_entry_stdnt.config(show='')
            show_hide_password_button['image'] = open_eye_image

    password_label_stdnt = Label(passwd_frame_student, text="PASSWORD", font=corbel_13, bg="#4f4f4d", foreground="#FFFFFF")
    password_entry_stdnt = Entry(passwd_frame_student, bg="#2e2e2d", foreground="#FFFFFF", borderwidth=0, width=55,font=font_style_passwd_entry_field, show="*")


    show_hide_password_button = HoverButton(passwd_frame_student, image=close_eye_image, bg="#4f4f4d", command=toggle_password, borderwidth=0, activebackground=sidebar_button_hover_color)
    show_hide_password_button.grid(row=2, column=2, padx=5, sticky=W)

    admission_number_lbl.grid(row=1, column= 0, pady= 10)
    admission_number_entry.grid(row=1, column =1, padx =10)

    password_label_stdnt.grid(row= 2,column= 0, padx= 10, sticky=W)
    password_entry_stdnt.grid(row= 2, column= 1, padx= 10, pady= 10)

    def password_verify():
        global student_name, student_admission_number

        student_admission_number = int(admission_number_entry.get())
        print(student_admission_number)
        student_password = password_entry_stdnt.get()

        for i in range(2, num_student_psswd + 2):
            print('For loop works')
            admission_number_in_spreadsheet = ws_student_psswd["A" + str(i)].value
            password_in_spreadsheet = ws_student_psswd["B" + str(i)].value

            if admission_number_in_spreadsheet == student_admission_number:

                if password_in_spreadsheet == student_password:
                    passwd_frame_student.grid_forget()
                    enter_button.grid_forget()
                    print('correct')

                    student_name = students.get_name_for_password(student_admission_number)
                    print(student_name)

                    student_button_root()

                else:
                    print('incorrect')


            else:
                password_entry_stdnt.delete(0,100)
                password_entry_stdnt.insert(0, 'INCORRECT PASSWORD')


    enter_button = Button(passwd_frame_student, text="ENTER", font=font_style_enter_button, borderwidth=0, width=50,command=password_verify, bg="#1aeb8d")
    enter_button.grid(columnspan= 4, pady= 10, padx= 10)





def teacher_button_root():
    #view student details
    #add grades
    #add homework
    #enter course
    #View current courses

    num_notifications = ws_notifications["H3"].value
    notifications_row = num_notifications + 2

    teacher_buttons_frame = create_frame(root, dark_bg, row=0, column=1)
    greetings_lbl_teachers = Label(teacher_buttons_frame, text=f"Hello, {teacher_name}, what is you task related to:", bg=dark_bg, fg='white', font=corbel_15)
    greetings_lbl_teachers.grid(row=0, columnspan=2)

    def back():
        teacher_buttons_frame.grid_forget()

    view_student_details_button = HoverButton(teacher_buttons_frame, text='STUDENT DETAILS', font= corbel_15, borderwidth= 0, width= 70, bg=bg_colour1, foreground="white", command= second_screen_students.courses, activebackground=sidebar_button_hover_color)
    enter_into_course_button = HoverButton(teacher_buttons_frame, text='COURSES', font= corbel_15, borderwidth= 0, width= 34, bg=bg_colour1, foreground="white", command= second_screen_students.courses, activebackground=sidebar_button_hover_color)
    credentials_button = HoverButton(teacher_buttons_frame, text='CHANGE PASSWORD', font= corbel_15, borderwidth= 0, width= 34, bg=bg_colour1, foreground="white", command= second_screen_students.courses, activebackground=sidebar_button_hover_color)

    back_button_root = HoverButton(teacher_buttons_frame, text="BACK", font=font_style_enter_button, borderwidth=0,width=78, bg="#e84d1a", foreground="white", command=back,activebackground=sidebar_button_hover_color)

    view_student_details_button.grid(row=1, columnspan=2, padx=10, pady=10)
    enter_into_course_button.grid(row=2, column=0, padx=10, pady=10)
    credentials_button.grid(row=2, column=1, padx=10, pady=10)
    back_button_root.grid(row=3, columnspan=2, padx=10, pady=10)

    name_validity = notifications.check_name_validity(teacher_name)
    print(name_validity)
    print(f"teacher name: {teacher_name}")

    if name_validity == True:
        print('notification if')

        course_register_notification_frame = create_frame(teacher_buttons_frame, dark_bg, row=5, columnspan=2)

        random_button = Button(teacher_buttons_frame, bg=dark_bg, height=10, borderwidth=0)
        topic_lbl = Label(course_register_notification_frame, text=ws_notifications["B" + str(i)].value, font=corbel_15, bg=dark_bg, fg='white')
        description_lbl = Label(course_register_notification_frame, text=ws_notifications["E" + str(i)].value, font=corbel_13, bg=dark_bg, fg='white')

        accept_button = HoverButton(course_register_notification_frame, text="ACCEPT", font=corbel_13, bg=enter_button_color, fg='black', borderwidth=0, width=10)
        deny_button = HoverButton(course_register_notification_frame, text='DENY', font=corbel_13, bg=back_button_color, fg='White', borderwidth=0, width=10)

        random_button.grid(row=4, columnspan=2)
        topic_lbl.grid(row=0, column=0, sticky=W)
        description_lbl.grid(row=1, column=0, sticky=W)

        accept_button.grid(row=0, column=1, padx=10, pady=7)
        deny_button.grid(row=1, column=1, padx=10, pady=7)

    else:
        print('soemthing went wrong')


#Features that Teachers can Access
class teacher_functions:
    pass

def teacher_password_check():
    global passwd_frame_teacher

    welcome_lbl_frame.grid_forget()

    passwd_frame_teacher = Frame(root, bg="#4f4f4d")
    passwd_frame_teacher.grid(row=0, column=1, padx=90)
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(2, weight=1)

    instructions_lbl = Label(passwd_frame_teacher, text="Please enter your index No. and Password",
                             font=font_style_popup_button, bg="#4f4f4d", foreground="white")
    instructions_lbl.grid(row=0, columnspan=2, padx=10)

    admission_number_lbl = Label(passwd_frame_teacher, text="INDEX NO.", font=corbel_13, bg="#4f4f4d",
                                 foreground="#FFFFFF")
    admission_number_entry = Entry(passwd_frame_teacher, bg="#2e2e2d", foreground="#FFFFFF", borderwidth=0, width=55,
                                   font=font_style_passwd_entry_field)

    def toggle_password():
        if password_entry_teacher.cget('show') == "":
            password_entry_teacher.config(show="*")
            show_hide_password_button['image'] = close_eye_image
        else:
            password_entry_teacher.config(show='')
            show_hide_password_button['image'] = open_eye_image

    password_label_teacher = Label(passwd_frame_teacher, text="PASSWORD", font=corbel_13, bg="#4f4f4d",
                                 foreground="#FFFFFF")
    password_entry_teacher = Entry(passwd_frame_teacher, bg="#2e2e2d", foreground="#FFFFFF", borderwidth=0, width=55,
                                 font=font_style_passwd_entry_field, show="*")

    show_hide_password_button = HoverButton(passwd_frame_teacher, image=close_eye_image, bg="#4f4f4d",
                                            command=toggle_password, borderwidth=0,
                                            activebackground=sidebar_button_hover_color)
    show_hide_password_button.grid(row=2, column=2, padx=5, sticky=W)

    admission_number_lbl.grid(row=1, column=0, pady=10)
    admission_number_entry.grid(row=1, column=1, padx=10)

    password_label_teacher.grid(row=2, column=0, padx=10, sticky=W)
    password_entry_teacher.grid(row=2, column=1, padx=10, pady=10)

    def password_verify():
        global student_name, student_admission_number, teacher_name

        teacher_admission_number = int(admission_number_entry.get())
        print(teacher_admission_number)
        teacher_password = password_entry_teacher.get()

        for i in range(2, num_student_psswd + 2):
            print('For loop works')
            admission_number_in_spreadsheet = ws_teacher_passwd["A" + str(i)].value
            password_in_spreadsheet = ws_teacher_passwd["B" + str(i)].value

            if admission_number_in_spreadsheet == teacher_admission_number:

                if password_in_spreadsheet == teacher_password:
                    passwd_frame_teacher.grid_forget()
                    enter_button.grid_forget()
                    print('correct')

                    teacher_name = teachers.get_name_for_password(teacher_admission_number)
                    print(teacher_name)

                    teacher_button_root()

                else:
                    print('incorrect')


            else:
                password_entry_teacher.config(show="")

                password_entry_teacher.delete(0, 100)
                password_entry_teacher.insert(0, 'INCORRECT PASSWORD')

    enter_button = Button(passwd_frame_teacher, text="ENTER", font=font_style_enter_button, borderwidth=0, width=50,
                          command=password_verify, bg="#1aeb8d")
    enter_button.grid(columnspan=4, pady=10, padx=10)




#Features that the Admin can Access
class admin_functions:

    #THESE ARE THE ADMIN FUNCTIONS FOR STUDENTS
    @staticmethod
    def register_students():
        global fname, lname, DoB, gender, guardian_names, guardian_telephone, address, submit_button, fname_entry, lname_entry, dob_entry, gender_entry, guardian_names_entry, \
            guardian_telephone_entry, address_entry, window

        register_student_frame = create_frame(root, "#2e2e2d", row=0, column=2)

        # Assigning the Entry Fields
        fname_entry = Entry(register_student_frame, width=40, font=corbel_13, bg=dark_bg, foreground="white", borderwidth=0)
        lname_entry = Entry(register_student_frame, width=40, font=corbel_13, bg=dark_bg, foreground="white", borderwidth=0)
        dob_entry = Entry(register_student_frame, width=40, font=corbel_13, bg=dark_bg, foreground="white", borderwidth=0)
        gender_entry = Entry(register_student_frame, width=40, font=corbel_13, bg=dark_bg, foreground="white", borderwidth=0)
        guardian_names_entry = Entry(register_student_frame, width=40, font=corbel_13, bg=dark_bg, foreground="white", borderwidth=0)
        guardian_telephone_entry = Entry(register_student_frame, width=40, font=corbel_13, bg=dark_bg, borderwidth=0,foreground="white")
        address_entry = Entry(register_student_frame, width=40, font=corbel_13, bg=dark_bg, foreground="white", borderwidth=0)

        fname_lbl = Label(register_student_frame, text="First Name:", font=corbel_13, bg="#2e2e2d", foreground="white")
        lname_lbl = Label(register_student_frame, text="Last Name:", font=corbel_13, bg="#2e2e2d", foreground="white")
        dob_lbl = Label(register_student_frame, text="Date of Birth:", font=corbel_13, bg="#2e2e2d", foreground="white")
        gender_lbl = Label(register_student_frame, text="Gender:", font=corbel_13, bg="#2e2e2d", foreground="white")
        guardian_names_lbl = Label(register_student_frame, text="Guardian Names:", font=corbel_13, bg="#2e2e2d",foreground="white")
        guardian_telephone_lbl = Label(register_student_frame, text="Guardian Telephone:", font=corbel_13, bg="#2e2e2d",foreground="white")
        address_lbl = Label(register_student_frame, text="Address:", font=corbel_13, bg="#2e2e2d", foreground="white")

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

        def register():
            global fname, lname, DoB, gender, guardian_names, guardian_telephone, address, submit_button, fname_entry, lname_entry, dob_entry, gender_entry, guardian_names_entry, \
                guardian_telephone_entry, address_entry, window

            fname = fname_entry.get()
            lname = lname_entry.get()
            DoB = dob_entry.get()
            gender = gender_entry.get()
            guardian_names = guardian_names_entry.get()
            guardian_telephone = guardian_telephone_entry.get()
            address = address_entry.get()

            def registered_lbl():
                registered_lbl = Label(register_student_frame, text="REGISTERED", bg="#2e2e2d", foreground="white",font=corbel_13)
                registered_lbl.grid(row=10, columnspan=2)

            registering_lbl = Label(register_student_frame, text="REGISTERING...", font=corbel_13, bg="#2e2e2d",
                                    foreground="white")
            registering_lbl.grid(row=8, columnspan=2)

            course_register_progress_bar = ttk.Progressbar(register_student_frame, orient=HORIZONTAL, length=300,
                                                           mode="determinate")
            course_register_progress_bar.grid(row=9, columnspan=2)

            for i in range(5):
                course_register_progress_bar['value'] += 20
                root.update_idletasks()
                time.sleep(1)

            registered_lbl()

            students(fname, lname, DoB, gender, guardian_names, guardian_telephone, address)

            fname_entry.delete(first=0, last=22)
            lname_entry.delete(first=0, last=22)
            dob_entry.delete(first=0, last=22)
            gender_entry.delete(first=0, last=22)
            guardian_names_entry.delete(first=0, last=100)
            guardian_telephone_entry.delete(first=0, last=100)
            address_entry.delete(first=0, last=22)

        def back():
            register_student_frame.grid_forget()

        register_button = HoverButton(register_student_frame, text="REGISTER", bg="#1aeb8d", foreground="black", width=40,font=corbel_13, command=register, borderwidth=0, activebackground=enter_button_hover_color)
        register_button.grid(row=7, column=1, pady=10, padx=10)

        back_button = HoverButton(register_student_frame, text="BACK", bg="#e84d1a", foreground="white", width=10,font=corbel_13, command=back, borderwidth=0, activebackground=back_button_hover_color)
        back_button.grid(row=7, column=0, pady=10)

    @staticmethod
    def view_student_details():
        student_ID_get = 0

        view_student_details_frame = create_frame(root, "#2e2e2d", row=0, column=2)

        student_ID_label = Label(view_student_details_frame, text="Student ID:", font=corbel_13, pady=2,
                                 bg="#2e2e2d", foreground="white")
        student_ID_label.grid(row=0, column=0)
        student_ID_entry = Entry(view_student_details_frame, width=50, bg=dark_bg, foreground="white", borderwidth=0)
        student_ID_entry.grid(row=0, column=1)

        def enter():

            try:
                student_ID_get = int(student_ID_entry.get())

                returned_list = students.view_student_details(student_ID_get)

                # view_details_window = Toplevel()
                # view_details_window.configure(bg="#393939")

                student_ID_details_lbl = Label(view_student_details_frame, text="Student ID:", bg="#2e2e2d", foreground="white", font=corbel_13)
                fname_details_lbl = Label(view_student_details_frame, text="First Name:", bg="#2e2e2d", foreground="white", font=corbel_13)
                lname_details_lbl = Label(view_student_details_frame, text="Last Name:", bg="#2e2e2d", foreground="white", font=corbel_13)
                DoB_details_lbl = Label(view_student_details_frame, text="Date of Birth:", bg="#2e2e2d", foreground="white", font=corbel_13)
                gender_details_lbl = Label(view_student_details_frame, text="Gender:", bg="#2e2e2d", foreground="white", font=corbel_13)
                guardian_details_lbl = Label(view_student_details_frame, text="Guardain Names:", bg="#2e2e2d", font=corbel_13,
                                             foreground="white")
                guardian_telephone_lbl = Label(view_student_details_frame, text="Guardian Telephone:", bg="#2e2e2d", font=corbel_13,
                                               foreground="white")
                address_details_lbl = Label(view_student_details_frame, text="Address:", bg="#2e2e2d", foreground="white", font=corbel_13)

                print(students.view_student_details(student_ID_get))
                student_ID_details = Label(view_student_details_frame, text=returned_list[0], bg="#2e2e2d", foreground="white",
                                           width=50)
                fname_details = Label(view_student_details_frame, text=returned_list[1], bg="#2e2e2d", foreground="white",
                                      width=50)
                lname_details = Label(view_student_details_frame, text=returned_list[2], bg="#2e2e2d", foreground="white",
                                      width=50)
                DoB_details = Label(view_student_details_frame, text=returned_list[3], bg="#2e2e2d", foreground="white",
                                    width=50)
                gender_details = Label(view_student_details_frame, text=returned_list[4], bg="#2e2e2d", foreground="white",
                                       width=50)
                guardian_names_details = Label(view_student_details_frame, text=returned_list[5], bg="#2e2e2d",
                                               foreground="white", width=50)
                guardian_telephone_details = Label(view_student_details_frame, text=returned_list[6], bg="#2e2e2d",
                                                   foreground="white", width=50)
                address_details = Label(view_student_details_frame, text=returned_list[7], bg="#2e2e2d", foreground="white",
                                        width=50)

                student_ID_details_lbl.grid(row=1, column=0, sticky= W)
                fname_details_lbl.grid(row=2, column=0, sticky= W)
                lname_details_lbl.grid(row=3, column=0, sticky= W)
                DoB_details_lbl.grid(row=4, column=0, sticky= W)
                gender_details_lbl.grid(row=5, column=0, sticky= W)
                guardian_details_lbl.grid(row=6, column=0, sticky= W)
                guardian_telephone_lbl.grid(row=7, column=0, sticky= W)
                address_details_lbl.grid(row=8, column=0, sticky= W)

                student_ID_details.grid(row=1, column=1, sticky=W)
                fname_details.grid(row=2, column=1, sticky=W)
                lname_details.grid(row=3, column=1, sticky=W)
                DoB_details.grid(row=4, column=1, sticky=W)
                gender_details.grid(row=5, column=1, sticky=W)
                guardian_names_details.grid(row=6, column=1, sticky=W)
                guardian_telephone_details.grid(row=7, column=1, sticky=W)
                address_details.grid(row=8, column=1, sticky=W)

            except:
                student_not_found_lbl = Label(view_student_details_frame, text="Student Not Found!", bg="#393939",
                                              foreground="white")
                student_not_found_lbl.grid(columnspan=2)
                print('Student Not found')


        enter_button = HoverButton(view_student_details_frame, text="Enter", font=corbel_13, command=enter,
                              bg="#1aeb8d", foreground="black", width=30, activebackground=enter_button_hover_color)
        enter_button.grid(row=9, column=1, pady=10)

        def back():
            view_student_details_frame.grid_forget()

        back_button = Button(view_student_details_frame, text="Back", bg="#e84d1a", foreground="white", width=10,
                             font=corbel_13, command=back, borderwidth=0, activebackground=back_button_hover_color)
        back_button.grid(row=9, column=0, pady=10)

    @staticmethod
    def remove_student():
        remove_student_frame = create_frame(root, "#2e2e2d", row=0, column=2)

        Student_ID_lbl = Label(remove_student_frame, text="Student ID:", bg="#2e2e2d", foreground="white",
                               font=corbel_13)
        Student_ID_lbl.grid(row=0, column=0)

        Student_ID_entry = Entry(remove_student_frame, width=50, bg=dark_bg, foreground="white", borderwidth=0)
        Student_ID_entry.grid(row=0, column=1)

        def enter():
            try:
                student_ID = int(Student_ID_entry.get())
                print(student_ID)
                students.remove_student_function(student_ID)

                removed_lbl = Label(remove_student_frame, text="Removed", bg="#393939", foreground="white")
                removed_lbl.grid(columnspan=2)

            except:
                student_not_found_lbl = Label(remove_student_frame, text="Student Not Found!", bg="#393939",foreground="white")
                student_not_found_lbl.grid(columnspan=2)
                print('Student Not found')

        def back():
            remove_student_frame.grid_forget()

        back_button = HoverButton(remove_student_frame, text="Back", bg="#e84d1a", foreground="white", width=10,font=font_style_submit_button, command=back, borderwidth=0, activebackground=back_button_hover_color)
        back_button.grid(row=1, column=0, pady=10)

        enter_button = HoverButton(remove_student_frame, text="Enter", font=font_style_popup_button, command=enter,bg="#1aeb8d", foreground="black", width=30, activebackground=enter_button_hover_color)
        enter_button.grid(row=1, column=1, padx=10)


    #THESE ARE THE ADMIN FUNCTIONS FOR TEACHERS
    @staticmethod
    def register_teacher():
        register_teacher_frame = create_frame(root, "#2e2e2d", row=0, column=2)

        # Assigning the Entry Fields
        fname_entry = Entry(register_teacher_frame, width=40, font=corbel_13, bg=dark_bg, foreground="white", borderwidth=0)
        lname_entry = Entry(register_teacher_frame, width=40, font=corbel_13, bg=dark_bg, foreground="white", borderwidth=0)
        qualifications_entry = Entry(register_teacher_frame, width=40, font=corbel_13, bg=dark_bg, foreground="white", borderwidth=0)
        experience_entry = Entry(register_teacher_frame, width=40, font=corbel_13, bg=dark_bg, foreground="white", borderwidth=0)

        fname_lbl = Label(register_teacher_frame, text="First Name:", font=corbel_13, bg="#2e2e2d", foreground="white")
        lname_lbl = Label(register_teacher_frame, text="Last Name:", font=corbel_13, bg="#2e2e2d", foreground="white")
        qualifications_lbl = Label(register_teacher_frame, text="Qualifications:", font=corbel_13, bg="#2e2e2d", foreground="white")
        experience_lbl = Label(register_teacher_frame, text="Experience:", font=corbel_13, bg="#2e2e2d", foreground="white")

        fname_lbl.grid(row=0, column=0, sticky=W)
        lname_lbl.grid(row=1, column=0, sticky=W)
        qualifications_lbl.grid(row=2, column=0, sticky=W)
        experience_lbl.grid(row=3, column=0, sticky=W)

        # Positionning the Entry Fields
        fname_entry.grid(row=0, column=1)
        lname_entry.grid(row=1, column=1)
        qualifications_entry.grid(row=2, column=1)
        experience_entry.grid(row=3, column=1)



        def enter():
            fname_teachers = fname_entry.get()
            lname_teachers = lname_entry.get()
            qualifications_teachers = qualifications_entry.get()
            experience_teachers = experience_entry.get()

            def registered_lbl():
                registered_lbl = Label(register_teacher_frame, text="REGISTERED", bg="#2e2e2d", foreground="white",font=corbel_13)
                registered_lbl.grid(row=7, columnspan=2)

            registering_lbl = Label(register_teacher_frame, text="REGISTERING...", font=corbel_13, bg="#2e2e2d",foreground="white")
            registering_lbl.grid(row=5, columnspan=2)

            course_register_progress_bar = ttk.Progressbar(register_teacher_frame, orient=HORIZONTAL, length=300,mode="determinate")
            course_register_progress_bar.grid(row=6, columnspan=2)

            for i in range(5):
                course_register_progress_bar['value'] += 20
                root.update_idletasks()
                time.sleep(1)

            registered_lbl()

            teachers.register_teacher(fname_teachers, lname_teachers, qualifications_teachers, experience_teachers)

        def back():
            register_teacher_frame.grid_forget()

        Enter_button = HoverButton(register_teacher_frame, text="Enter", font=font_style_enter_button, command=enter,bg="#1aeb8d", foreground="black", width=40, borderwidth=0,activebackground=enter_button_hover_color)
        Enter_button.grid(row=4, column=1, padx=10, pady=10)

        back_button = HoverButton(register_teacher_frame, text="Back", font=font_style_enter_button, command=back, bg="#e84d1a",foreground="white", width=10, borderwidth=0, activebackground=back_button_hover_color)
        back_button.grid(row=4, column=0, padx=10, pady=10)

    @staticmethod
    def view_teacher_details():
        view_teacher_details_frame = create_frame(root, "#2e2e2d", row=0, column=2)

        teacher_ID_lbl = Label(view_teacher_details_frame, text="TEACHER ID:", font=corbel_13, bg="#2e2e2d", fg='white')
        teacher_ID_entry = Entry(view_teacher_details_frame, bg=dark_bg, fg='white', borderwidth=0, width=30)

        teacher_ID_lbl.grid(row=0, column=0, padx=5, pady=5)
        teacher_ID_entry.grid(row=0, column=1, padx=5, pady=5)

        def enter():
            teacher_ID = teacher_ID_entry.get()

            details = teachers.view_details(teacher_ID)

            details_frame = create_frame(view_teacher_details_frame, '#2e2e2d', row=1, columnspan=2)

            #These are the labels for the teacher details
            first_name_lbl = Label(details_frame, text="FIRST NAME", font=corbel_bold_13, bg="#2e2e2d", fg='white')
            last_name_lbl = Label(details_frame, text='LAST NAME', font=corbel_bold_13, bg='#2e2e2d', fg='white')
            qualifications_lbl = Label(details_frame, text="QUALIFICATIONS", font=corbel_bold_13, bg='#2e2e2d', fg='white')
            experience_lbl = Label(details_frame, text="EXPERIENCE", font=corbel_bold_13, bg='#2e2e2d', fg='white')

            first_name_result = Label(details_frame, text=details[1], font=corbel_13, bg='#2e2e2d', fg='white')
            last_name_result = Label(details_frame, text=details[2], font=corbel_13, bg='#2e2e2d', fg='white')
            qualifications_result = Label(details_frame, text=details[3], font=corbel_13, bg='#2e2e2d', fg='white')
            experience_result = Label(details_frame, text=details[4], font=corbel_13, bg='#2e2e2d', fg='white')


            #positioning the teacher labels
            first_name_lbl.grid(row=0, column=0, sticky=W)
            last_name_lbl.grid(row=1, column=0, sticky=W)
            qualifications_lbl.grid(row=2, column=0, sticky=W)
            experience_lbl.grid(row=3, column=0, sticky=W)

            first_name_result.grid(row=0, column=1, sticky=E, padx=10)
            last_name_result.grid(row=1, column=1, sticky=E, padx=10)
            qualifications_result.grid(row=2, column=1, sticky=E, padx=10)
            experience_result.grid(row=3, column=1, sticky=E, padx=10)

        def back():
            view_teacher_details_frame.grid_forget()

        Enter_button = HoverButton(view_teacher_details_frame, text="Enter", font=font_style_enter_button, command=enter,bg="#1aeb8d", foreground="black", width=19, borderwidth=0,activebackground=enter_button_hover_color)
        Enter_button.grid(row=2, column=1, padx=10, pady=10)

        back_button = HoverButton(view_teacher_details_frame, text="Back", font=font_style_enter_button, command=back, bg="#e84d1a",foreground="white", width=10, borderwidth=0, activebackground=back_button_hover_color)
        back_button.grid(row=2, column=0, padx=10, pady=10)

    @staticmethod
    def remove_teacher():
        remove_teacher_frame = create_frame(root, "#2e2e2d", row=0, column=2)

        # Assigning the Entry Fields
        teacher_ID_entry = Entry(remove_teacher_frame, width=40, font=corbel_13, bg=dark_bg, foreground="white",borderwidth=0)
        teacher_ID_lbl = Label(remove_teacher_frame, text="TEACHER ID:", font=corbel_13, bg="#2e2e2d", foreground="white")

        teacher_ID_lbl.grid(row=0, column=0, sticky=W)
        teacher_ID_entry.grid(row=0, column=1)

        def enter():
            teacher_ID = teacher_ID_entry.get()

            teachers.remove_teacher(teacher_ID)

            removed_lbl = Label(remove_teacher_frame, text="REMOVED", font=corbel_13, bg="#2e2e2d", fg='white')
            removed_lbl.grid(row=3, columnspan=2, padx=10, pady=10)

        def back():
            remove_teacher_frame.grid_forget()

        Enter_button = HoverButton(remove_teacher_frame, text="Enter", font=font_style_enter_button, command=enter,bg="#1aeb8d", foreground="black", width=40, borderwidth=0,activebackground=enter_button_hover_color)
        Enter_button.grid(row=2, column=1, padx=10, pady=10)

        back_button = HoverButton(remove_teacher_frame, text="Back", font=font_style_enter_button, command=back, bg="#e84d1a",foreground="white", width=10, borderwidth=0, activebackground=back_button_hover_color)
        back_button.grid(row=2, column=0, padx=10, pady=10)

    @staticmethod
    def view_grades():
        pass

class admin_second_screen:

    @staticmethod
    def student_page():

        admin_students_frame = create_frame(root, dark_bg, row=0, column=1)

        register_student_button = HoverButton(admin_students_frame, text="REGISTER STUDENTS", width=72, font=corbel_15, bg=bg_colour1, foreground="white", command=admin_functions.register_students, borderwidth=0, activebackground=sidebar_button_hover_color)
        view_student_details_button = HoverButton(admin_students_frame, text="VIEW DETAILS", width=35, font=corbel_15, bg=bg_colour1, foreground="white", command=admin_functions.view_student_details, borderwidth=0, activebackground=sidebar_button_hover_color)
        remove_student_button = HoverButton(admin_students_frame, text="UNREGISTER STUDENT", width=35, font=corbel_15, bg=bg_colour1, foreground="white", borderwidth=0, command=admin_functions.remove_student, activebackground=sidebar_button_hover_color)
        view_grades_button = HoverButton(admin_students_frame, text="VIEW GRADES", width=72, font=corbel_15, bg=bg_colour1, foreground="white", borderwidth=0, activebackground=sidebar_button_hover_color)

        # register_button = HoverButton(courses_frame, text="ENROLL", font=font_style_button, command=register,borderwidth=0, bg=bg_colour1, foreground="white", width=71,activebackground=sidebar_button_hover_color)


        register_student_button.grid(row=0, columnspan=2, padx=5, pady=5)
        view_student_details_button.grid(row=1, column=0, padx=5, pady=5)
        remove_student_button.grid(row=1, column=1, padx=5, pady=5)
        view_grades_button.grid(row=2, columnspan=2, padx=5, pady=5)

        def back():
            admin_students_frame.grid_forget()

        back_button = HoverButton(admin_students_frame, text="BACK", width=80, font=font_style_enter_button, bg="#e84d1a",foreground="white", borderwidth=0, command= back, activebackground=back_button_hover_color)
        back_button.grid(columnspan= 2, pady =10, padx= 10)

    @staticmethod
    def teacher_page():
        admin_teachers_frame = create_frame(root, dark_bg, row=0, column=1)

        register_teachers_button = HoverButton(admin_teachers_frame, text="REGISTER LECTURER", width=70, font=corbel_15, bg=bg_colour1, foreground="white", borderwidth=0, activebackground=sidebar_button_hover_color, command=admin_functions.register_teacher)
        view_teacher_details_button = HoverButton(admin_teachers_frame, text="VIEW DETAILS", width=34, font=corbel_15, bg=bg_colour1, foreground="white", borderwidth=0, activebackground=sidebar_button_hover_color, command=admin_functions.view_teacher_details)
        remove_teacher_button = HoverButton(admin_teachers_frame, text="REMOVE LECTURER", width=34, font=corbel_15, bg=bg_colour1, foreground="white", borderwidth=0, activebackground=sidebar_button_hover_color, command=admin_functions.remove_teacher)

        register_teachers_button.grid(row=0, columnspan=2, padx=5, pady=5)
        view_teacher_details_button.grid(row=1, column=0, padx=5, pady=5)
        remove_teacher_button.grid(row=1, column=1, padx=5, pady=5)


        def back():
            admin_teachers_frame.grid_forget()

        back_button = Button(admin_teachers_frame, text="BACK", width=78, font=font_style_enter_button, bg="#e84d1a",foreground="white", borderwidth=0, command= back)
        back_button.grid(columnspan= 2, pady =10, padx= 10)

    @staticmethod
    def course_page():
        pass

    @staticmethod
    def clubs_page():
        pass


def admin_button_root_rest():

    passwd_frame.grid_forget()

    admin_buttons_frame = create_frame(root, dark_bg, row=0, column=1)
    task_lbl = Label(admin_buttons_frame, text= "WHAT IS YOUR TASK RELATED TO:", font = font_style_popup_button, bg= dark_bg, foreground= "white")

    Students_button = HoverButton(admin_buttons_frame, text= "STUDENTS", width=35, font=corbel_15, bg=bg_colour1, foreground="white", command=admin_second_screen.student_page, borderwidth=0, activebackground=sidebar_button_hover_color)
    Teachers_button = HoverButton(admin_buttons_frame, text= "TEACHERS", width=35, font=corbel_15, bg=bg_colour1, foreground="white",command=admin_second_screen.teacher_page, borderwidth=0, activebackground=sidebar_button_hover_color)
    Courses_button = HoverButton(admin_buttons_frame, text= "COURSES", width=35, font=corbel_15, bg=bg_colour1, foreground="white", borderwidth=0, activebackground=sidebar_button_hover_color)
    Clubs_button = HoverButton(admin_buttons_frame, text= "CLUBS", width=35, font=corbel_15, bg=bg_colour1, foreground="white", borderwidth=0, activebackground=sidebar_button_hover_color)
    # terminal_button = Button(root, text= "TERMINAL", width=20, font=font_style_button, bg="#545352",foreground="white", borderwidth=0, command= admin_functions.open_terminal)


    task_lbl.grid(columnspan = 4)
    Students_button.grid(row=10, column=0, padx=5, pady=5)
    Teachers_button.grid(row=10, column=1, padx=5, pady=5)
    Courses_button.grid(row=11, column=0, padx=5, pady=5)
    Clubs_button.grid(row=11, column=1, padx=5, pady=5)
    # terminal_button.grid(row=10, column=4, padx=7, pady=10)


    def admin_screen_back():
        admin_buttons_frame.grid_forget()
        home()

    back_button = HoverButton(admin_buttons_frame, text="BACK", width=80, font=font_style_enter_button, bg="#e84d1a", foreground="white",borderwidth=0, command= admin_screen_back, activebackground=back_button_hover_color)
    back_button.grid(columnspan=4, pady=10)

def admin_button_root_password():
    global passwd_frame

    passwd_frame = Frame(root,bg= "#4f4f4d" )
    passwd_frame.grid(row=0, column=1, padx= 10, pady= 10)
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(2, weight=1)

    password_label = Label(passwd_frame, text= "PLEASE ENTER YOUR PASSWORD", font= corbel_13, bg="#4f4f4d", foreground="#FFFFFF")
    password_entry = Entry(passwd_frame, bg="#2e2e2d", foreground= "#FFFFFF",borderwidth= 0, width = 50, font=font_style_passwd_entry_field, show="*")

    password_label.grid(columnspan= 4, pady= 10)
    password_entry.grid(columnspan= 3, padx= 10)

    def toggle_password():
        if password_entry.cget('show') == "":
            password_entry.config(show="*")
            hide_view_button['image'] = close_eye_image
        else:
            password_entry.config(show='')
            hide_view_button['image'] = open_eye_image

    hide_view_button = HoverButton(passwd_frame, image=close_eye_image, bg="#4f4f4d", command=toggle_password, borderwidth=0, activebackground=sidebar_button_hover_color)
    hide_view_button.grid(row=1, column=3, padx=5)

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

    enter_button = HoverButton(passwd_frame, text="ENTER", font=font_style_enter_button, borderwidth=0, width=13, command= password_verify, bg="#1aeb8d", activebackground=enter_button_hover_color)
    enter_button.grid(row=1, column=4, pady= 10, padx= 10)




home()
root.mainloop()
