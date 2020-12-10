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
5. Add Students to courses""")

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

        students.register_students(student_ID, fname, lname, DoB, gender, guardian_name, guardian_telephone, address)

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

        student_ID = input('Student_ID:')
        course_ID = input('Course ID: ')

        g1 = input("Grade 1 mark:")
        g2 = input('Grade 2 mark:')
        g3 = input('Grade 3 mark: ')

