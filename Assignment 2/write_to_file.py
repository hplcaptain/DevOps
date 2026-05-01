while True:
    print ("1. Write to file")
    print ("2. read from file")
    print ("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        filename = input("Enter filename: ")
        content = input("Enter content to write: ")
        with open(filename, 'w') as file:
            file.write(content)
        print("Content written to file successfully!")

    elif choice == '2':
        filename = input("Enter filename: ")
        try:
            with open(filename, 'r') as file:
                content = file.read()
                print("File content:")
                print(content)
        except FileNotFoundError:
            print("File not found. Please check the filename and try again.")

    elif choice == '3':
        print("Exiting...")
        break   

    else:
        print("Invalid choice. Please try again.")
        
