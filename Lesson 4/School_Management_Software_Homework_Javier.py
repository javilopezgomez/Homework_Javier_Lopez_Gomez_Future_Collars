#School Management Software - Homework

students = {}
teachers = {}
homeroom_teachers = {}


while True:

    print("\nWhich action do you want to perform?: \n"
          "\n1. Create user \n"
          "2. Manage users \n"
          "3. End the program\n")

    choice = input("Choice: ").lower()

    if choice in ("1", "create user"):
        while True:
            print("\nPlease, choose the user type to create and write the option chosen:")
            print("\nStudent \n"
                  "Teacher \n"
                  "Homeroom teacher \n"
                  "End \n")
            user_create = str(input("User type: ")).lower()

            if user_create == "student":
                student_name = str(input("Student name and surname: "))
                student_class = str(input("Student class: "))
                students[student_name] = {"class": student_class}
                print(f"\n{student_name} has been successfully added to the database.")

            elif user_create == "teacher":
                teacher_name = str(input("Teacher name and surname: "))
                teacher_subject = str(input("Teacher subject: "))
                teacher_classes = []
                while True:
                    teacher_class = str(input("Teacher class (press enter if there are no more classes): "))
                    if teacher_class == "":
                        break
                    teacher_classes.append(teacher_class)

                teachers[teacher_name] = {
                    "subject": teacher_subject,
                    "classes": teacher_classes
                }
                print(f"\n{teacher_name} has been successfully added to the database.")

            elif user_create == "homeroom teacher":
                homeroom_teacher_name = str(input("Homeroom teacher name and surname: "))
                homeroom_teacher_class = str(input("Homeroom teacher class: "))
                homeroom_teachers[homeroom_teacher_name] = {"class": homeroom_teacher_class}
                print(f"\n{homeroom_teacher_name} has been successfully added to the database.")

            elif user_create == "end":
                break

            else:
                print("Invalid input. Please enter a correct user type.")

    elif choice in ("2", "manage users"):
        while True:
            print("\nPlease, choose the element to manage and write the option chosen: ")
            print("\nClass \n"
                  "Student \n"
                  "Teacher \n"
                  "Homeroom teacher \n"
                  "End \n")
            user_manage = str(input("Element to manage: ")).lower()

            if user_manage == "class":
                class_manage = str(input("Which class do you want to display?: "))
                print(f"\nTutor of class {class_manage}:")
                for homeroom_teacher, data in homeroom_teachers.items():
                    if data["class"] == class_manage:
                        print(homeroom_teacher)

                print(f"\nStudents in class {class_manage}:")
                for student, data in students.items():
                    if data["class"] == class_manage:
                        print(student)

            elif user_manage == "student":
                while True:
                    student_manage = str(input("Which student do you want to display?: "))
                    if student_manage in students:
                        print(f"\nCLasses that {student_manage} attends:")
                        print(students[student_manage]["class"])

                        print(f"\nTeachers that participate in class " + students[student_manage]["class"] + ":")
                        for teacher, data in teachers.items():
                            if students[student_manage]["class"] in data["classes"]:
                                print(teacher)

                        print(f"\nTutor of the class " + students[student_manage]["class"] + ":")
                        for homeroom_teacher, data in homeroom_teachers.items():
                            if data["class"] == students[student_manage]["class"]:
                                print(homeroom_teacher)
                        break
                    else:
                        print("The student was not found. Please, write a correct name.")

            elif user_manage == "teacher":
                while True:
                    teacher_manage = str(input("Which teacher do you want to display?: "))
                    if teacher_manage in teachers:
                        print(f"\nCLasses that {teacher_manage} teaches:")

                        for classes in teachers[teacher_manage]["classes"]:
                            print(classes)
                        break
                    else:
                        print("The teacher was not found. Please, write a correct name.")

            elif user_manage == "homeroom teacher":
                while True:
                    homeroom_teacher_manage = str(input("Homeroom teacher do you want to display?: "))
                    if homeroom_teacher_manage in homeroom_teachers:
                        print(f"\nStudents that {homeroom_teacher_manage} leads:")
                        for student, data in students.items():
                            if data["class"] == homeroom_teachers[homeroom_teacher_manage]["class"]:
                                print(student)
                        break
                    else:
                        print("The Homeroom Teacher was not found. Please, write a correct name.")


            elif user_manage == "end":
                break

            else:
                print("Invalid input. Please, enter a correct element to manage.")

    elif choice in ("3", "end the program", "end"):
        break

    else:
        print("Invalid choice. Please enter a correct option.")