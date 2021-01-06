import openpyxl as xl
from tkinter import *
from tkinter.font import Font

wb = xl.load_workbook("university.xlsx")
ws = wb['students']
ws_courses = wb['courses']
ws_student_courses = wb['student_courses']
ws_student_clubs = wb['student_clubs']
ws_removed_students = wb["removed_students"]

num_courses = ws_courses["F4"].value
course_row = num_courses + 2

num_student_courses = ws_student_courses["L4"].value
student_course_row = num_student_courses + 2

num_student_clubs = ws_student_clubs["H4"].value
student_club_row = num_student_clubs + 2

column_headers = ["A", "B", "C", "D", "E", "F","G", "H","I"]

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

        num_students = ws["J3"].value
        student_row = num_students + 2

        ws["B" + str(student_row)] = fname
        ws["C" + str(student_row)] = lname
        ws["D" + str(student_row)] = DoB
        ws["E" + str(student_row)] = gender
        ws["F" + str(student_row)] = guardian_names
        ws["G" + str(student_row)] = guardian_telephone
        ws["H" + str(student_row)] = address

        ws["J3"] = num_students + 1

        ws["A" + str(student_row)] = ws['J3'].value
        wb.save(filename="university.xlsx")

    @staticmethod
    def view_student_details(ID):

        num_students = ws["J3"].value
        student_row = num_students + 2

        for i in range(2, num_students + 2):
            if ws["A" + str(i)].value == int(ID):
                student_ID = ws["A" + str(i)].value
                fname = ws["B" + str(i)].value
                lname = ws["C" + str(i)].value
                DoB = ws["D" + str(i)].value
                gender = ws["E" + str(i)].value
                guardian_names = ws["F" + str(i)].value
                guardian_telephone = ws["G" + str(i)].value
                address = ws["H" + str(i)].value


                return student_ID, fname, lname, DoB, gender, guardian_names, guardian_telephone, address
                break

            else:
                continue

    @staticmethod
    def remove_student_function(ID):

        num_students = ws["J3"].value
        student_row = num_students + 2

        num_students_removed = ws_removed_students["J3"].value

        print('Function Works')
        for i in range(2, num_students + 2):
            print("For Loop Works")
            try:
                if int(ws["A" + str(i)].value) == ID:
                    print("IF statement Works")

                    ws_removed_students["A" + str(i)] =  ws["A" + str(i)].value
                    ws_removed_students["B" + str(i)] = ws["B" + str(i)].value
                    ws_removed_students["C" + str(i)] = ws["C" + str(i)].value
                    ws_removed_students["D" + str(i)] = ws["D" + str(i)].value
                    ws_removed_students["E" + str(i)] = ws["E" + str(i)].value
                    ws_removed_students["F" + str(i)] = ws["F" + str(i)].value
                    ws_removed_students["G" + str(i)] = ws["G" + str(i)].value
                    ws_removed_students["H" + str(i)] = ws["H" + str(i)].value

                    ws_removed_students["J3"] = num_students_removed + 1

                    ws["A" + str(i)] = ""
                    ws["B" + str(i)] = ""
                    ws["C" + str(i)] = ""
                    ws["D" + str(i)] = ""
                    ws["E" + str(i)] = ""
                    ws["F" + str(i)] = ""
                    ws["G" + str(i)] = ""
                    ws["H" + str(i)] = ""

                    for x in range(i, num_students + 2):
                        ws["A" + str(x)] = ws["A" + str(x + 1)].value
                        ws["B" + str(x)] = ws["B" + str(x + 1)].value
                        ws["C" + str(x)] = ws["C" + str(x + 1)].value
                        ws["D" + str(x)] = ws["D" + str(x + 1)].value
                        ws["E" + str(x)] = ws["E" + str(x + 1)].value
                        ws["F" + str(x)] = ws["F" + str(x + 1)].value
                        ws["G" + str(x)] = ws["G" + str(x + 1)].value
                        ws["H" + str(x)] = ws["H" + str(x + 1)].value

                    current_num_students = ws["J3"].value
                    ws["J3"] = current_num_students - 1
                    wb.save(filename="university.xlsx")
                    break

            except:
                continue
        

class courses(students):



    def __init__(self, course_ID, course_name, course_duration, prerequisistes, instructors):
        self.course_ID = course_ID
        self.course_name = course_name
        self.course_duration = course_duration
        self.prerequisistes = prerequisistes
        self.instructors = instructors

    @classmethod
    def register_course(cls, course_ID, course_name, course_duration, prerequisites, instructors):

        ws_courses["A" + str(course_row)] = course_ID
        ws_courses["B" + str(course_row)] = course_name
        ws_courses["C" + str(course_row)] = course_duration
        ws_courses["D" + str(course_row)] = prerequisites
        ws_courses["E" + str(course_row)] = instructors

        ws_courses['F4'] = num_courses + 1
        wb.save(filename="university.xlsx")

    @classmethod
    def view_course_details(cls, course_ID):

        for i in range(2, num_students + 2):
            if ws["A" + str(i)] == course_ID:
                course_ID = ws["A" + str(i)].value
                course_name = ws["B" + str(i)].value
                course_duration = ws["B" + str(i)].value
                prerequisites = ws["B" + str(i)].value
                instructors = ws["B" + str(i)].value
                break

            else:
                continue

    @classmethod
    def add_student_courses(cls, student_ID, Course_ID, g1, g2, g3, g4, g5):
        pass


        # ws_student_courses["A" + str(student_course_row)] =
        # ws_student_courses["B" + str(student_course_row)] =
        # ws_student_courses["C" + str(student_course_row)] =
        #
        # ws_student_courses["D" + str(student_course_row)] =
        # ws_student_courses["E" + str(student_course_row)] =
        #
        # ws_student_courses["F" + str(student_course_row)] = g1
        # ws_student_courses["G" + str(student_course_row)] = g2
        # ws_student_courses["H" + str(student_course_row)] = g3
        # ws_student_courses["I" + str(student_course_row)] = g4
        # ws_student_courses["J" + str(student_course_row)] = g5
        #
        # ws_student_courses["L4"] = num_student_courses + 1
        # wb.save(filename="university.xlsx")

    @staticmethod
    def remove_student_courses(student_ID, Course_ID):
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

                wb.save(filename="university.xlsx")
                break

            else:
                continue



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

        ws["F4"] = num_student_clubs + 1

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
