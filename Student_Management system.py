students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("\nStudents List:")
            for i, student in enumerate(students, start=1):
                print(f"{i}. {student}")

    elif choice == "3":
        name = input("Enter student name to delete: ")

        if name in students:
            students.remove(name)
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")