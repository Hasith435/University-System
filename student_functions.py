import openpyxl as xl
from tkinter import *
from tkinter.font import Font


wb = xl.load_workbook("university.xlsx")
ws_students = wb['students']
ws_courses = wb['courses']
ws_student_courses = wb['student_courses']
ws_student_clubs = wb['student_clubs']
ws_removed_students = wb["removed_students"]
ws_student_psswd = wb["student_pswd"]
ws_teachers = wb["Teachers"]
ws_notifications = wb["notifications"]
ws_teacher_passwd = wb["teacher_psswd"]


num_student_clubs = ws_student_clubs["H4"].value
student_club_row = num_student_clubs + 2

num_students = ws_students["J3"].value
num_courses = ws_courses["F4"].value

column_headers = ["A", "B", "C", "D", "E", "F","G", "H","I"]

#THESE ARE THE GLOBAL FUNCTIONS THAT ARE GONNA BE USEFUL AT THE END
def get_student_name(student_id):
    for i in range(2, num_students + 2):
        if ws_students["A" + str(i)].value == student_id:
            student_name = ws_students["B" + str(i)].value
            return student_name

def get_instructor_name(course_name):
    for i in range(2, num_courses + 2):
        if ws_courses["B" + str(i)].value == course_name:
            instructor_name = ws_courses["E" + str(i)].value
            return instructor_name


#THESE ARE THE CLASSES THAT ARE RELATED TO THE STUDENTS
class students:

    #For Registering Students
    def __init__(self,fname, lname, DoB, gender, guardian_names, guardian_telephone, address):
        self.fname = fname
        self.lname = lname
        self.DoB = DoB
        self.gender = gender
        self.guardian_names = guardian_names
        self.guardian_telephone = guardian_telephone
        self.address = address

        #THIS SECTION IS TO ADD THE STUDENT TO THE STUDENT WORKSHEET
        num_students = ws_students["J3"].value
        student_row = num_students + 2

        ws_students["B" + str(student_row)] = fname
        ws_students["C" + str(student_row)] = lname
        ws_students["D" + str(student_row)] = DoB
        ws_students["E" + str(student_row)] = gender
        ws_students["F" + str(student_row)] = guardian_names
        ws_students["G" + str(student_row)] = guardian_telephone
        ws_students["H" + str(student_row)] = address

        ws_students["J3"] = num_students + 1

        ws_students["A" + str(student_row)] = ws_students['J3'].value

        #THIS SECTION IS TO ADD THE STUDENT TO THE STUDENT_PSSWD WORKSHEET
        num_student_psswd = ws_student_psswd["G6"].value
        student_psswd_row = num_student_psswd + 2

        student_index = ws_students["A" + str(student_row)].value

        # This is the student ID
        ws_student_psswd["A" + str(student_psswd_row)] = student_index
        # This is the student password
        ws_student_psswd["B" + str(student_psswd_row)] = f"student{student_index}"
        # This is the student's First Name
        ws_student_psswd["C" + str(student_psswd_row)] = fname

        ws_student_psswd["G6"] = num_student_psswd + 1

        wb.save(filename="university.xlsx")

    @staticmethod
    def view_student_details(ID):

        num_students = ws_students["J3"].value
        student_row = num_students + 2

        for i in range(2, num_students + 2):
            if ws_students["A" + str(i)].value == int(ID):
                student_ID = ws_students["A" + str(i)].value
                fname = ws_students["B" + str(i)].value
                lname = ws_students["C" + str(i)].value
                DoB = ws_students["D" + str(i)].value
                gender = ws_students["E" + str(i)].value
                guardian_names = ws_students["F" + str(i)].value
                guardian_telephone = ws_students["G" + str(i)].value
                address = ws_students["H" + str(i)].value


                return student_ID, fname, lname, DoB, gender, guardian_names, guardian_telephone, address
                break

            else:
                continue

    @staticmethod
    def remove_student_function(ID):

        num_students = ws_students["J3"].value
        student_row = num_students + 2

        num_students_removed = ws_removed_students["J3"].value

        print('Function Works')
        for i in range(2, num_students + 2):
            print("For Loop Works")
            try:
                if int(ws_students["A" + str(i)].value) == ID:
                    print("IF statement Works")

                    ws_removed_students["A" + str(i)] =  ws_students["A" + str(i)].value
                    ws_removed_students["B" + str(i)] = ws_students["B" + str(i)].value
                    ws_removed_students["C" + str(i)] = ws_students["C" + str(i)].value
                    ws_removed_students["D" + str(i)] = ws_students["D" + str(i)].value
                    ws_removed_students["E" + str(i)] = ws_students["E" + str(i)].value
                    ws_removed_students["F" + str(i)] = ws_students["F" + str(i)].value
                    ws_removed_students["G" + str(i)] = ws_students["G" + str(i)].value
                    ws_removed_students["H" + str(i)] = ws_students["H" + str(i)].value

                    ws_removed_students["J3"] = num_students_removed + 1

                    ws_students["A" + str(i)] = ""
                    ws_students["B" + str(i)] = ""
                    ws_students["C" + str(i)] = ""
                    ws_students["D" + str(i)] = ""
                    ws_students["E" + str(i)] = ""
                    ws_students["F" + str(i)] = ""
                    ws_students["G" + str(i)] = ""
                    ws_students["H" + str(i)] = ""

                    for x in range(i, num_students + 2):
                        ws_students["A" + str(x)] = ws_students["A" + str(x + 1)].value
                        ws_students["B" + str(x)] = ws_students["B" + str(x + 1)].value
                        ws_students["C" + str(x)] = ws_students["C" + str(x + 1)].value
                        ws_students["D" + str(x)] = ws_students["D" + str(x + 1)].value
                        ws_students["E" + str(x)] = ws_students["E" + str(x + 1)].value
                        ws_students["F" + str(x)] = ws_students["F" + str(x + 1)].value
                        ws_students["G" + str(x)] = ws_students["G" + str(x + 1)].value
                        ws_students["H" + str(x)] = ws_students["H" + str(x + 1)].value

                    current_num_students = ws_students["J3"].value
                    ws_students["J3"] = current_num_students - 1
                    wb.save(filename="university.xlsx")
                    break

            except:
                continue


    @staticmethod
    def get_name_for_password(student_ID):

        num_student_psswd = ws_student_psswd["G6"].value
        print(num_student_psswd)

        for i in range(2, num_student_psswd + 2):
            if ws_student_psswd["A" + str(i)].value == student_ID:
                return ws_student_psswd["C" + str(i)].value

            else:
                print('invalid_student_ID')

    @staticmethod
    def change_password(student_ID, currentPassword, newPassword):
        print('change password functioln')

        num_student_psswd = ws_student_psswd["G6"].value
        student_psswd_row = num_student_psswd + 2

        for i in range(2, num_student_psswd + 2):
            print('for loop change password')
            if ws_student_psswd["A" + str(i)].value == student_ID :

                if ws_student_psswd["B" + str(i)].value == currentPassword:
                    ws_student_psswd["B" + str(i)] = newPassword
                    wb.save(filename="university.xlsx")
                    break

                else:
                    print('problem1')
                    return False

            else:
                print('Problem2')
                return False


class courses(students):


    def __init__(self, course_name, course_duration, prerequisistes, instructors):
        self.course_name = course_name
        self.course_duration = course_duration
        self.prerequisistes = prerequisistes
        self.instructors = instructors

        num_courses = ws_courses["F4"].value
        course_row = num_courses + 2

        ws_courses["B" + str(course_row)] = course_name
        ws_courses["C" + str(course_row)] = course_duration
        ws_courses["D" + str(course_row)] = prerequisistes
        ws_courses["E" + str(course_row)] = instructors

        ws_courses["F4"] = num_courses + 1

        ws_courses["A" + str(course_row)] = ws_courses['F4'].value
        wb.save(filename="university.xlsx")


    @staticmethod
    def view_course_details(Course_ID):

        num_courses = ws_courses["F4"].value
        print(num_courses)

        for i in range(2, num_courses + 2):
            if ws_courses["A" + str(i)].value == Course_ID:
                course_ID = ws_courses["A" + str(i)].value
                course_name = ws_courses["B" + str(i)].value
                course_duration = ws_courses["C" + str(i)].value
                prerequisites = ws_courses["D" + str(i)].value
                instructors = ws_courses["E" + str(i)].value

                print(course_ID)
                print(course_name)
                print(course_duration)
                print(prerequisites)
                print(instructors)

                return course_ID, course_name, course_duration, prerequisites, instructors

            else:
                print('Invalid')

    @staticmethod
    def view_all_course_names():
        num_courses = ws_courses["F4"].value
        course_names = []

        for i in range(2, num_courses + 2):
            course_name = ws_courses["B" + str(i)].value
            course_names.append(course_name)

        return course_names

    @staticmethod
    def add_student_courses(student_id,course_name):

        print('function start')
        num_student_courses = ws_student_courses["L4"].value
        student_courses_row = num_student_courses + 2

        num_notifications = ws_notifications["H1"].value
        notifications_row = num_notifications + 2

        num_students = ws_students["J3"].value
        student_row = num_students + 2

        num_courses = ws_courses["F4"].value
        course_row = num_courses + 2

        fname=""
        lname=""
        for i in range(2, num_students + 2):
            print(student_id)
            if ws_students["A" + str(i)].value == student_id:
                print('for loop')
                fname = ws_students["B" + str(i)].value
                lname = ws_students["C" + str(i)].value

            else:
                print('student if does not work')

        ws_student_courses["B" + str(student_courses_row)] = fname
        ws_student_courses["C" + str(student_courses_row)] = lname
        print(fname, lname)
        print('student if works')


        for k in range(2, num_courses + 2):
            if ws_courses["B" + str(k)].value == course_name:
                course_id = ws_courses["A" + str(k)].value
                ws_student_courses["D" + str(student_courses_row)] = course_id


            else:
                print('Courses if does not work')


        ws_student_courses["A" + str(student_courses_row)] = student_id
        ws_student_courses["E" + str(student_courses_row)] = course_name


        ws_student_courses["L4"] = num_student_courses + 1

        wb.save(filename="university.xlsx")






    @staticmethod
    def remove_student_courses(student_ID, Course_ID):

        num_student_courses = ws_student_courses["L4"].value

        print('Function')
        print(num_student_courses)
        for i in range(2, 100000):
            print('For loop')
            if int(ws_student_courses["A" + str(i)].value) == student_ID and int(ws_student_courses["D" + str(i)].value) == Course_ID:
                print('works')
                ws_student_courses["A" + str(i)] = ""
                ws_student_courses["B" + str(i)] = ""
                ws_student_courses["C" + str(i)] = ""
                ws_student_courses["D" + str(i)] = ""
                ws_student_courses["E" + str(i)] = ""
                ws_student_courses["F" + str(i)] = ""
                ws_student_courses["G" + str(i)] = ""
                ws_student_courses["H" + str(i)] = ""
                ws_student_courses["I" + str(i)] = ""
                ws_student_courses["J" + str(i)] = ""

                ws_student_courses["L4"] = num_student_courses - 1

                wb.save(filename="university.xlsx")
                break

            else:
                continue



    @staticmethod
    def add_student_grades(student_ID, g1, g2, g3, g4, g5):

        num_student_courses = ws_student_courses["L4"].value
        student_course_row = num_student_courses + 2

        for i in range(0, num_student_courses + 2):
           if ws_courses["A" + str(i)].value == student_ID:
               ws_courses["F" + str(i)] = g1
               ws_courses["G" + str(i)] = g2
               ws_courses["H" + str(i)] = g3
               ws_courses["I" + str(i)] = g4
               ws_courses["J" + str(i)] = g5

        ws_courses["L3"] = num_student_courses + 1
        wb.save(filename= "university.xlsx")


    @staticmethod
    def view_grades(student_ID, course_ID):

        num_student_courses = ws_student_courses["L4"].value
        student_course_row = num_student_courses + 2

        for i in range(2, num_student_courses + 2):
            if ws_student_courses["A" + str(i)].value == student_ID and ws_student_courses["D" + str(i)].value == course_ID:
                g1 = ws_student_courses["F" + str(i)].value
                g2 = ws_student_courses["G" + str(i)].value
                g3 = ws_student_courses["H" + str(i)].value
                g4 = ws_student_courses["I" + str(i)].value
                g5 = ws_student_courses["J" + str(i)].value

                print(g1)
                print(g2)
                print(g3)
                print(g4)
                print(g5)

                return g1, g2, g3, g4, g5

            else:
                print('Student ID or course ID is wrong!')



    #THESE ARE THE FUNCTIONS THAT ARE GOING TO BE USED UP
    @staticmethod
    def get_student_name():
        pass


class clubs(students):

    club_id = []
    club_name = []
    subject = []
    description = []

    @classmethod
    def register_club(cls, club_id, club_name, subject, description):
        cls.club_id.append(club_id)
        cls.club_name.append(club_name)
        cls.subject.append(subject)
        cls.description.append(description)

        list_index = cls.club_id.index(club_id)

        ws_student_clubs["A" + str(student_club_row)] = cls.club_id[list_index]
        ws_student_clubs["B" + str(student_club_row)] = cls.club_name[list_index]
        ws_student_clubs["C" + str(student_club_row)] = cls.subject[list_index]
        ws_student_clubs["D" + str(student_club_row)] = cls.description[list_index]

        ws_students["F4"] = num_student_clubs + 1

        wb.save(filename="university.xlsx")

    @classmethod
    def view_club_details(cls, club_id):
        list_index = cls.club_id.index(club_id)

        print('')
        print(f"Club ID: {cls.club_id[list_index]}")
        print(f"Club Name: {cls.club_name[list_index]}")
        print(f"Subject: {cls.subject[list_index]}")
        print(f"Description: {cls.description[list_index]}")

    @classmethod
    def add_student_club(cls, student_ID, club_ID):
        list_index_students = cls.student_ID.index(student_ID)
        list_index_club = cls.club_id.index(club_ID)

        ws_student_clubs["A" + str(student_club_row)] = cls.student_ID[list_index_students]
        ws_student_clubs["B" + str(student_club_row)] = cls.fname[list_index_students]
        ws_student_clubs["C" + str(student_club_row)] = cls.lname[list_index_students]

        ws_student_clubs["D" + str(student_club_row)] = cls.club_id[list_index_club]
        ws_student_clubs["E" + str(student_club_row)] = cls.club_name[list_index_club]

        ws_student_clubs["H4"] = num_student_clubs + 1

        wb.save(filename = "university.xlsx")


#THESE ARE THE CLASSES THAT ARE RELEATED TO THE TEACHERS IN THE UNIVERSITY
class teachers:

    num_teachers = ws_teachers["H4"].value
    teacher_row = num_teachers + 2

    @classmethod
    def register_teacher(cls, first_name, last_name, qualifications, experience):

        ws_teachers["B" + str(cls.teacher_row)] = first_name
        ws_teachers["C" + str(cls.teacher_row)] = last_name
        ws_teachers["D" + str(cls.teacher_row)] = qualifications
        ws_teachers["E" + str(cls.teacher_row)] = experience

        print(first_name)

        ws_teachers["H4"] = cls.num_teachers + 1
        #teacher index number
        ws_teachers["A" + str(cls.teacher_row)] = ws_teachers["H4"].value

        #This is the section to add the teacher to the teahcer_passwd sheet
        num_teacher_psswd = ws_teacher_passwd["F4"].value
        teacher_psswd_row = num_teacher_psswd + 2

        teacher_index = ws_teachers["A" + str(cls.teacher_row)].value

        # This is the student ID
        ws_teacher_passwd["A" + str(teacher_psswd_row)] = teacher_index
        # This is the student password
        ws_teacher_passwd["B" + str(teacher_psswd_row)] = f"lecturer{teacher_index}"
        # This is the student's First Name
        ws_teacher_passwd["C" + str(teacher_psswd_row)] = first_name

        ws_teacher_passwd["F4"] = num_teacher_psswd + 1

        wb.save(filename="university.xlsx")

    @staticmethod
    def remove_teacher(teacher_id):
        num_teachers = ws_teachers["H4"].value
        num_teachers_row = num_teachers + 2

        print('Function Works')
        for i in range(2, num_teachers + 2):
            print("For Loop Works")
            try:
                if int(ws_teachers["A" + str(i)].value) == int(teacher_id):
                    print("IF statement Works")

                    ws_teachers["A" + str(i)] = ""
                    ws_teachers["B" + str(i)] = ""
                    ws_teachers["C" + str(i)] = ""
                    ws_teachers["D" + str(i)] = ""
                    ws_teachers["E" + str(i)] = ""
                    ws_teachers["F" + str(i)] = ""
                    ws_teachers["G" + str(i)] = ""
                    ws_teachers["H" + str(i)] = ""

                    for x in range(i, num_teachers + 2):
                        ws_students["A" + str(x)] = ws_students["A" + str(x + 1)].value
                        ws_students["B" + str(x)] = ws_students["B" + str(x + 1)].value
                        ws_students["C" + str(x)] = ws_students["C" + str(x + 1)].value
                        ws_students["D" + str(x)] = ws_students["D" + str(x + 1)].value
                        ws_students["E" + str(x)] = ws_students["E" + str(x + 1)].value
                        ws_students["F" + str(x)] = ws_students["F" + str(x + 1)].value
                        ws_students["G" + str(x)] = ws_students["G" + str(x + 1)].value
                        ws_students["H" + str(x)] = ws_students["H" + str(x + 1)].value

                    current_num_teachers = ws_teachers["H4"].value
                    ws_teachers["H4"] = current_num_teachers - 1
                    wb.save(filename="university.xlsx")
                    break

            except:
                continue

    @staticmethod
    def view_details(teacher_id):
        num_teachers = ws_teachers["H4"].value

        for i in range(2, num_teachers + 2):
            if ws_teachers["A" + str(i)].value == int(teacher_id):
                teacher_ID = ws_teachers["A" + str(i)].value
                fname = ws_teachers["B" + str(i)].value
                lname = ws_teachers["C" + str(i)].value
                qualifications = ws_teachers["D" + str(i)].value
                experience = ws_teachers["E" + str(i)].value

                return teacher_ID, fname, lname, qualifications, experience

            else:
                continue

    @staticmethod
    def get_name_for_password (teacher_id):
        num_teacher_passwd = ws_teacher_passwd["F4"].value
        print(num_teacher_passwd)

        for i in range(2, num_teacher_passwd + 2):
            if ws_teacher_passwd["A" + str(i)].value == teacher_id:
                return ws_teacher_passwd["C" + str(i)].value

            else:
                print('invalid teacher id')

class notifications:
    notification_info = []

    #These are some of the methods that may be useful further on
    @staticmethod
    def get_sender_name(name):
        num_notifications = ws_notifications["H1"].value


        for i in range(2, num_notifications + 2):
            sender_name = ws_notifications["C" + str(i)].value

            if sender_name == name:
                return sender_name
            else:
                continue

    @staticmethod
    def get_receiver_name(name):
        num_notifications = ws_notifications["H1"].value

        for i in range(2, num_notifications + 2):
            receiver_name = ws_notifications["E" + str(i)].value

            if name == receiver_name:
                return receiver_name

            else:
                continue

    @staticmethod
    def get_description(course_name):
        num_notifications = ws_notifications["H1"].value

        for i in range(2, num_notifications + 2):
            description = ws_notifications["E" + str(i)].value
            splited_description = description.split()
            print(splited_description)

            if splited_description[7] == course_name:
                course_name_description = splited_description[7]
                return course_name_description

            else:
                continue

    @classmethod
    def check_name_validity(cls, login_name):
        num_notifications = ws_notifications["H1"].value
        print(f"num_notifications in check_name_validity: {num_notifications}")
        print('comes into the check name function')

        for i in range(2, num_notifications + 2):
            print('comes in for loop')
            receiver_name = ws_notifications["D" + str(i)].value
            print(f"login name: {login_name}")
            print(f"Receiver_name: {receiver_name}")

            print(f"login_name type is: {type(login_name)}")
            print(f"Receiver_name type is: {type(receiver_name)}")

            if login_name == receiver_name:

                print("login_name = receiver name")
                topic = ws_notifications["B" + str(i)].value
                description = ws_notifications["E" + str(i)].value
                appending_list = [topic, description]

                cls.notification_info.append(appending_list)

                return True, num_notifications, cls.notification_info
            else:
                print('login_name does not = receiver_name')
                continue


    #These are the functions for enrollment
    @staticmethod
    def add_notification_details(student_id, course_name):

        print('Notification function is called')

        num_notifications = ws_notifications["H1"].value
        notifications_row = num_notifications + 2

        student_name = get_student_name(student_id)
        instructor_name = get_instructor_name(course_name)

        # for i in range(2, num_notifications + 2):
        description = f"{student_name} would like to enroll in the {course_name}"

        ws_notifications["B" + str(notifications_row)] = "COURSE ENROLLMENT"
        ws_notifications["C" + str(notifications_row)] = student_name
        ws_notifications["D" + str(notifications_row)] = instructor_name
        ws_notifications["E" + str(notifications_row)] = description

        ws_notifications["H1"] = num_notifications + 1
        notification_id = ws_notifications["H1"].value

        ws_notifications["A" + str(notifications_row)] = notification_id
        wb.save(filename="university.xlsx")


    @staticmethod
    def remove_notification(sender_name):
        num_notifications = ws_notifications["H1"].value
        sender_name = notifications.get_sender_name(sender_name)
        print(f'Sender Name: {sender_name}')

        for i in range(2, num_notifications + 2):
            if sender_name == ws_notifications["C" + str(i)].value:
                row=i
                print('remove notification for  loop works')

                ws_notifications.delete_rows(row)

                ws_notifications["H1"] = num_notifications - 1
                wb.save(filename='university.xlsx')
                break

            else:
                continue

    # @staticmethod
    # def remove_notification(student_name, course_name):
    #     num_notifications = ws_notifications["H3"].value
    #
    #     # receiver_name = notifications.get_receiver_name(login_name)
    #
    #     columns = ["A", "B", "C", "D", "E"]
    #
        # sender_name = notifications.get_sender_name(student_name)
        # course_name_description = notifications.get_description(course_name)
    #
    #     for i in range(2, num_notifications + 2):
    #         if sender_name == student_name:
    #             if course_name_description == course_name:
    #                 ws_notifications["A" + str(i)] = ""
    #                 ws_notifications["B" + str(i)] = ""
    #                 ws_notifications["C" + str(i)] = ""
    #                 ws_notifications["D" + str(i)] = ""
    #                 ws_notifications["E" + str(i)] = ""
    #
    #                 ws_notifications["H3"] = num_notifications - 1
    #
    #                 wb.save(filename="university.xlsx")
    #
    #             else:
    #                 print('Course_name wrong')
    #
    #         else:
    #             print('student name wrong')