library = {}

print("---- Library Management System ----")

while True:
    print("\n1.Add  2.Display  3.Issue  4.Return  5.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        bid = input("Enter Book ID: ")
        name = input("Enter Book Name: ")
        library[bid] = [name, False]
        print("Book added successfully")

    elif ch == "2":
        if not library:
            print("Library is empty")
        else:
            print("\nID   Name        Status")
            for b in library:
                status = "Issued" if library[b][1] else "Available"
                print(b, library[b][0], status)

    elif ch == "3":
        bid = input("Enter Book ID to issue: ")
        if bid in library and not library[bid][1]:
            library[bid][1] = True
            print("Book issued successfully")
        else:
            print("Book not available or not found")

    elif ch == "4":
        bid = input("Enter Book ID to return: ")
        if bid in library and library[bid][1]:
            library[bid][1] = False
            print("Book returned successfully")
        else:
            print("Invalid book ID or book not issued")

    elif ch == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again")
