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

class students:

    student_ID = []
    fname = []
    lname = []
    DoB = []
    gender = []
    guardian_names = []
    guardian_telephone = []
    address = []

    def __init__(self, student_ID, fname, lname, DoB, gender, guardian_names, guardian_telephone, address):
        self.student_ID = student_ID
        self.fname = fname
        self.lname = lname
        self.DoB = DoB
        self.gender = gender
        self.guardian_names = guardian_names
        self.guardian_telephone = guardian_telephone
        self.address = address

    @classmethod
    def register_students(cls, student_ID, fname, lname, DoB, gender, guardian_names, guardian_telephone, address):

        cls.student_ID.append(student_ID)
        cls.fname.append(fname)
        cls.lname.append(lname)
        cls.DoB.append(DoB)
        cls.gender.append(gender)
        cls.guardian_names.append(guardian_names)
        cls.guardian_telephone.append(guardian_telephone)
        cls.address.append(address)


        list_index = cls.student_ID.index(student_ID)

        ws["A" + str(student_row)] = cls.student_ID[list_index]
        ws["B" + str(student_row)] = cls.fname[list_index]
        ws["C" + str(student_row)] = cls.lname[list_index]
        ws["D" + str(student_row)] = cls.DoB[list_index]
        ws["E" + str(student_row)] = cls.gender[list_index]
        ws["F" + str(student_row)] = cls.guardian_names[list_index]
        ws["G" + str(student_row)] = cls.guardian_telephone[list_index]
        ws["H" + str(student_row)] = cls.address[list_index]

        ws['J3'] = num_students + 1
        wb.save(filename="university.xlsx")

    @classmethod
    def view_student_details(cls, ID):
        list_index = cls.student_ID.index(ID)

        print('student id: ', cls.student_ID[list_index])
        print('First Name:', cls.fname[list_index])
        print('Last Name:', cls.lname[list_index])
        print('Date of Birth:', cls.DoB[list_index])
        print('Gender:', cls.gender[list_index])
        print('Guardian Names:', cls.guardian_names[list_index])
        print('Guardian Telephone:', cls.guardian_telephone[list_index])
        print('Address: ', cls.address[list_index])
      

class courses(students):

    course_id = []
    course_name = []
    course_duration = []
    prerequisistes = []
    instructors = []

    def __init__(self, course_ID, course_name, course_duration, prerequisistes, instructors):
        self.course_ID = course_ID
        self.course_name = course_name
        self.course_duration = course_duration
        self.prerequisistes = prerequisistes
        self.instructors = instructors

    @classmethod
    def register_course(cls, course_ID, course_name, course_duration, prerequisites, instructors):
        cls.course_id.append(course_ID)
        cls.course_name.append(course_name)
        cls.course_duration.append(course_duration)
        cls.prerequisistes.append(prerequisites)
        cls.instructors.append(instructors)

        list_index = cls.course_id.index(course_ID)

        ws_courses["A" + str(course_row)] = cls.course_id[list_index]
        ws_courses["B" + str(course_row)] = cls.course_name[list_index]
        ws_courses["C" + str(course_row)] = cls.course_duration[list_index]
        ws_courses["D" + str(course_row)] = cls.prerequisistes[list_index]
        ws_courses["E" + str(course_row)] = cls.instructors[list_index]

        ws_courses['F4'] = num_courses + 1
        wb.save(filename="university.xlsx")

    @classmethod
    def view_course_details(cls, course_ID):
        list_index = cls.course_id.index(course_ID)

        print(f'Course ID: {cls.course_id[list_index]}')
        print(f'Course Name: {cls.course_name[list_index]}')
        print(f'Course Duration: {cls.course_duration[list_index]}')
        print(f'Prerequisites: {cls.prerequisistes[list_index]}')
        print(f'Instructors: {cls.instructors[list_index]}')

    @classmethod
    def add_student_courses(cls, student_ID, Course_ID, g1, g2, g3, g4, g5):
        list_index_students = cls.student_ID.index(student_ID)
        list_index_courses = cls.course_id.index(Course_ID)


        ws_student_courses["A" + str(student_course_row)] = cls.student_ID[list_index_students]
        ws_student_courses["B" + str(student_course_row)] = cls.fname[list_index_students]
        ws_student_courses["C" + str(student_course_row)] = cls.lname[list_index_students]

        ws_student_courses["D" + str(student_course_row)] = cls.course_id[list_index_courses]
        ws_student_courses["E" + str(student_course_row)] = cls.course_name[list_index_courses]

        ws_student_courses["F" + str(student_course_row)] = g1
        ws_student_courses["G" + str(student_course_row)] = g2
        ws_student_courses["H" + str(student_course_row)] = g3
        ws_student_courses["I" + str(student_course_row)] = g4
        ws_student_courses["J" + str(student_course_row)] = g5

        ws_student_courses["L4"] = num_student_courses + 1
        wb.save(filename="university.xlsx")




    #this function is not done yet
    @staticmethod
    def remove_student_courses(student_ID, Course_ID):
        print('Function')
        print(num_student_courses)
        for i in range(2, num_student_courses + 2):
            print('For loop')
            if ws_student_courses["A" + str(i)].value == student_ID and ws_student_courses["D" + str(i)].value == Course_ID:

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
