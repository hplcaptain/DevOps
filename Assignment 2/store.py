students = {}

while True:
    print("1. Add student")
    print("2. View students")
    print("3. View student details")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        students[name] = age
        grade = input("Enter student grade: ")
        students[name] = {'age': age, 'grade': grade}

        print("Student added successfully!")

    elif choice == '2':
        if not students:
            print("No students found.")
        else:
            print("Students:")
            for name in students:
                print(name)

    elif choice == '3':
        name = input("Enter student name: ")
        if name in students:
            print(f"Name: {name}, Age: {students[name]}")
        else:
            print("Student not found.")
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

