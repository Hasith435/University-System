import openpyxl as xl
from student_functions import students
from student_functions import courses

wb = xl.load_workbook("university.xlsx")
ws = wb.active

action = ("""These are the actions that you can perform:
1. Register students to the university
2. View student Details
3. Add new courses
4. View Course Details
5. Add Students to courses
6. Remove Students from a Course
7. Add clubs to the university
8. View club details
9. Add students to clubs""")

print('')
print(action)
print('')

while 1:
    action = str(input("What action do you want to perform:"))

    if action == "1":
        print("Please Enter the below Details:")
        student_ID = input('student_id:')
        fname = input('First Name:')
        lname = input('Last Name: ')
        DoB = input('Date of Birth (dd/mm/yyyy): ')
        gender = input('Gender (M or F): ')
        guardian_name = input('Guardian Names (seperate the names by commas): ')
        guardian_telephone = input('Guardian Telephone Number: ')
        address = input('Address: ')

        students.register_students(student_ID,fname, lname, DoB, gender, guardian_name, guardian_telephone, address)

    if action == "2":
        student_id = input('Student ID:')

        students.view_student_details(student_id)

    if action == "3":
        print('Please enter the below information:')
        print('')

        course_ID = input('Course ID:')
        course_name = input('Course Name:')
        course_duration = input('Course Duration: ')
        prerequisistes = input('Prerequisistes for Students:')
        instructors = input('Instructors:')

        courses.register_course(course_ID, course_name, course_duration, prerequisistes, instructors)

    if action == "4":
        course_ID = input('Course ID:')

        courses.view_course_details(course_ID)

    if action == "5":
        print("Please enter the below details:")

        student_ID = int(input('Student_ID:'))
        course_ID = int(input('Course ID: '))

        g1 = float(input("Term 1 mark:"))
        g2 = float(input('Term 2 mark:'))
        g3 = float(input('Term 3 mark: '))
        g4 = float(input('Term 4 mark:'))
        g5 = float(input('Term 5 mark:'))

        courses.add_student_courses(student_ID,course_ID, g1, g2, g3, g4, g5)

    if action == "6":
        student_ID = input('Student ID:')
        course_ID = input("Course ID:")
    
        courses.remove_student_courses(student_ID, course_ID)

    if action == "7":
        print('')
        print('Please fill in this information')
        print('')

        club_id = input('Club ID:')
        club_name = input('Club Name:')
        subject =  input('Subject:')
        description = input('Description: ')

        clubs.register_club(club_id, club_name, subject,  description)

