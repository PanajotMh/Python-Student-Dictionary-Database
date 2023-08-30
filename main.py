AdminLogin = 'Admin'
AdminPassword = 'Cool123'

Students = ['Bob', 'Adenalina', 'Panajot', 'Spongebob']
Student_Address = ['6 Sesame Street', '6 Sesame Street', '8 Kings Way', '15 Trinity Avenue']
Student_Gender = ['Male', 'Female', 'Male', 'Male']


# New Student Name Subroutine.    (Function!)
def NewStudentName(Students, Student_Address, Student_Gender, FinishedProcess):
    NewName = input("Enter the new Students name: ")
    Students.append(NewName)
    New_Address = input("Enter the students address: ")
    Student_Address.append(New_Address)
    New_Gender = input("Enter the students gender: ")
    Student_Gender.append(New_Gender)
    NextProcess = input("Would you like to print this students details?  Yes/No :")
    if NextProcess == 'Yes' or NextProcess == 'y':
        newStudentIndex = len(Students) - 1

        print(f"Student Name: {Students[newStudentIndex]}")
        print(f"Student Address: {Student_Address[newStudentIndex]}")
        print(f"Student Gender: {Student_Gender[newStudentIndex]}")

        NewProcess = input("Would you like another service? Yes/No ")
        if NewProcess == 'Yes' or NewProcess == 'y':
          print(FinishedProcess)

          return FinishedProcess == True
        else:
            return
    else:
        NewProcess = input("Would you like another service? Yes/No")
        print(FinishedProcess)
        if NewProcess == 'Yes' or NewProcess == 'y':
            return
        else:
            return FinishedProcess == False


# Student Remover Database

def StudentExterminator(Students, Student_Address, Student_Gender):
    RemoveName = input("Enter the Students details to remove: ")
    Student_Address.remove([Students, RemoveName])
    Student_Gender.remove([Students, RemoveName])
    Students.remove(RemoveName)
    NextProcess = input("Would you like to print the current students remaining?  (1)Yes  (2)No")
    if NextProcess == '1':
        print(Students)
        NewProcess = input("Would you like another service? (1)Yes  (2)No")
        if NewProcess == '1':
            return
        else:
            return FinishedProcess == False
    else:
        NewProcess = input("Would you like another service? (1)Yes  (2)No")
        if NewProcess == '1':
            return
        else:
            return FinishedProcess == False


# Student Database Subroutine
def studentdatabase(Students, Student_Address, Student_Gender, FinishedProcess):
    correctnum = False
    Finished = False
    while correctnum == False or not Finished:
        command = input("""What would you like to do?
                •Add a student(1)
                •Remove a student(2)
                •Update a student's details(3)
                •Output student list(4)
                •Check a students current details(5) """)
        if command == '1':
            NewStudentName(Students, Student_Address, Student_Gender, FinishedProcess)
            correctnum = True
        elif command == '2':
            process = input("Enter the students name to remove: ")
            Students.remove(process)
            print(Students)
            correctnum = True

        elif command == '3':
            print("This is underway!")
            # process = input("Enter the students name to update")
            # Students.update(process)
        elif command == '4':
            print(Students)
        elif command == '':
            print("Please type a number!")
        elif command == '5':
            StudentName = input("Enter the students name: ")
            StudentName.capitalize()
            if StudentName in Students:
                student_index = Students.index(StudentName)
                student_address = Student_Address[student_index]
                student_gender = Student_Gender[student_index]
                print(f"Student Name: {StudentName}")
                print(f"Address: {student_address}")
                print(f"Gender: {student_gender}")
            else:
                print(f"Student '{StudentName}' not found.")
        else:
            print("Something went wrong, Try again!")


Correct_Password = False
while not Correct_Password:
    LoginGuess = input("Please enter your login:")
    PasswordGuess = input("Please enter your password:")
    if LoginGuess == AdminLogin and PasswordGuess == AdminPassword:
        Correct_Password = True
    elif LoginGuess == '':
        print("Please enter something!")
    else:
        print("Wrong Try again!")

FinishedProcess = False
while not FinishedProcess:
    process = input("""Welcome to the database handler what would you like to do?
                    •Manage Students(1)
                    •Manage School Staff(2)
                    •Log off(3): """)
    if process == '1':
        studentdatabase(Students, Student_Address, Student_Gender, FinishedProcess)
    elif process == '2':
        print("Okay")
    elif process == '3':
        print("Logging off!")
        break
    elif process == '':
        print("Please enter something!")


