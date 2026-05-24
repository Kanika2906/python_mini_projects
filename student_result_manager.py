#add student,check result, view all students and exit
student = {}
while True:
    print("\n-----STUDENT MANAGER APP-----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Check Result")
    print("4. Delete Student")
    print("5. Update marks")
    print("6. Save Results")
    print("7. Exit")

    choice = input("Enter your choice ")

    #Add student 
    if choice == "1":
        name = input("Enter Student name: ")
        marks = int(input("Enter marks:"))
        student[name] = marks
        print(f"{name} Successfully Added!")

    #view students
    elif choice == "2":
        if not student:
            print("No Student Found!")
        else:
            for name,marks in student.items():
                print(name, " : ", marks)
    
    #check result 
    elif choice == "3":
        name = input("Enter student name: ")

        if name in student:
            marks = student[name]
            if marks>=40 :
                print("Pass")
            else:
                print("Fail")
        else:
            print("Student not Found.")
    
    #delete a student
    elif choice == "4":
        name = input("Enter Student name to delete:")
        if name in student.keys():
            del student[name]
            print("Deleted Successfully.")
        else:
            print("Student Not Found.")
    
    #update marks
    elif choice == "5":
        name = input("Enter name to update:")
        marks = int(input("enter new marks"))
        if name in student:
            student[name]=marks
            print("Successfully Updated")
        else:
            print("Student Not Found")

    #save result
    elif choice == "6":
        with open("students.txt", "a") as file:
            for name, marks in student.items():
                file.write(f"{name}:{marks}\n")
            print("Saved Successfully")
    
    #exit
    elif choice == "7":
        print("Exiting...")
        break
    
    else:
        print("Invalid input")
