from monster_main import *
from monster_workshop import *
from student_class import *
from teacher_class import *


# As a Receptionist of the University, I should be able to create a Student with only first and last name

# Creating an empty list
teachers_list = []
student_list = []
list_of_workshop = []
list_of_attendees = []
list_all_workshops = []

# create a student_id_counter
student_id = 0
# create a teacher_id_counter
staff_id = 0
#
f_name_student = ' '
l_name_student = ' '
workshop_subject = ' '
user_input = ' '

# While loop:
while (user_input != '5'):
        user_input = input("Select value 1-5 to enter a menu option.\n 1) Create a new student: \n 2) Create a new teacher: "
                           "\n 3) Create a new workshop: \n 4) View list: \n 5) End programme: \n Your Selection is: ") # Creating the Menu
        if user_input == '1': # If the user enters 1
            # increment the student_id_counter1
            get_Students_student_id = student_id + 109483 # Creates a student ID

            get_Students_f_name = input("Enter first name of student \n") # ask for user to input their first names)
            get_Students_l_name = input("Enter last name of student \n") # ask for user to input their last names)

            student = Students(get_Students_f_name, get_Students_l_name, get_Students_student_id)

            student_list.append(student_list)  # add that student to the list of students
            print(f"Student name: {get_Students_f_name} {get_Students_f_name} {get_Students_student_id}") # print first, last name, + student id

            print("Number of students in list: " + str(len(student_list)))
            # print(list_of_students)r

# As a Receptionist of the University, I should be able to create a Teacher
# With every iteration of the while loop:
        # make condition for teacher

        if user_input == '2':
            # increment the teacher_id_counter
            get_teachers_staff_id = staff_id + 1
            # ask for user input (names)
            get_teachers_f_name = input("Enter first name of teacher \n")
            get_teachers_l_name = input("Enter last name teacher \n")
            # create a teacher from those inputs
            teacher_list = teacher_list(teachers.f_name, teachers.l_name, teachers.staff_id)
            # add that student to the list of students
            list_of_teacher.append(teacher_list)
            print(f"Teacher name: {teachers.f_name} {teachers.l_name} {teachers.staff_id}")
            # print(list_of_students)
            print("Number of teacher in list: " + str(len(teacher_list)))

        # As a Receptionist of the University, I should be able to list all workshops
        # As a Receptionist of the University, I should be able to create a workshop

        if user_input == '3':
            get_Workshop_scary_subject = input('What subject will the class be in ?\n')
            get_Workshop_scary_teacher = input("what teacher will be educating that class ?\n")
            workshop_list_of_attendees = input("Enter list of Student Attendees\n")
            print("Subject: ", Workshop_scary.subject)
            print("Teacher:", Workshop_scary.teacher)
            print("Attendees:", Workshop_scary.list_attendees)

        # if user_input == '4':
        #     list_all_workshops = [subject: {workshop_subject}]

        if user_input == '5':
            print("Programme ended")
            break





# # As a Receptionist of the University,
# # I should be able to create a Student with only first and last name
#
# # Student info
# student1 = Students('Fred', 'babak', 1, ['Interpersonal skills', 'Scrum Master', 'Software Developer'])
# student2 = Students('Ayman', 'yousfi', 2, ['Json', 'Project Manager'])
# student3 = Students('Frenchy', 'Montana', 3, ['Agile values', 'Trading Analyst'])
#
# # Teacher info
# teachers1 = teachers('Filipe', 'python', 3213934, ['Communication', 'Team Leader'])
# teachers2 = teachers('Astha', 'Shaw', 525827, ['SQL', 'Python', 'CSS'])
# teachers3 = teachers('Edmund', 'Young', 967996, ['Public speaking'])
#
# # WorkShop info
# workshop1 = Workshop_scary('Science', 'Astha', ['Fred', 'Ayman'])
# workshop2 = Workshop_scary('Maths', 'Edmund', ['Frenchy', 'Fred', 'Ayman'])
# workshop3 = Workshop_scary('English', 'Filipe', ['Ayman', 'Frenchy'])
#
#
# print(student1)
# print(student1.first_name, student1.last_name, student1.student_id, student1.skills)
#
# print(student2)
# print(student2.first_name, student1.last_name, student2.student_id, student2.skills)
#
# print(student3)
# print(student3.first_name, student1.last_name, student3.student_id, student3.skills)
#
# # student_list = []
# # student_list.append(student1)
# # student_list.append(student2)
# # student_list.append(student3)
#
# # Output for teacher info
# print(teachers1)
# print(teachers1.first_name, teachers1.last_name, teachers1.staff_id, teachers1.skills)
#
# print(teachers2)
# print(teachers2.first_name, teachers2.last_name, teachers2.staff_id, teachers2.skills)
#
# print(teachers3)
# print(teachers3.first_name, teachers3.last_name, teachers3.staff_id, teachers3.skills)
#
# # Output for workshop info
# print(workshop1)
# print(workshop1.subject, workshop1.teacher, workshop1.list_attendees)
#
# print(workshop2)
# print(workshop2.subject, workshop2.teacher, workshop2.list_attendees)
#
# print(workshop3)
# print(workshop3.subject, workshop3.teacher, workshop3.list_attendees)
