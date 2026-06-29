class Student:

    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))

        student = {
            "name": name,
            "age": age
        }

        self.students.append(student)
        print("Student Added Successfully!")

    def view_students(self):
        if not self.students:
            print("No Students Found")
            return

        print("\nStudent List")
        for student in self.students:
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("----------------")

    def search_student(self):
        name = input("Enter student name: ")

        for student in self.students:
            if student["name"].lower() == name.lower():
                print("Student Found")
                print(student)
                return

        print("Student Not Found")


system = Student()

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        system.add_student()

    elif choice == "2":
        system.view_students()

    elif choice == "3":
        system.search_student()

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")