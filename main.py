students = {}

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    students[roll] = {"name": name, "marks": marks}
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
        return
    for roll, data in students.items():
        print(f"Roll: {roll}, Name: {data['name']}, Marks: {data['marks']}")

def search_student():
    roll = input("Enter Roll No to search: ")
    if roll in students:
        data = students[roll]
        print(f"Name: {data['name']}, Marks: {data['marks']}")
    else:
        print("Student not found.")

def delete_student():
    roll = input("Enter Roll No to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted successfully!")
    else:
        print("Student not found.")

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
