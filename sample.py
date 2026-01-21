library = {}

print("---- Library Management System ----")

while True:
    print("\n1.Add  2.Display  5.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        bid = input("Enter Book ID: ")
        if bid in library:
            print("Book ID already exists")
        else:
            name = input("Enter Book Name: ")
            library[bid] = [name, False, ""]
            print("Book added successfully")

    elif ch == "2":
        if not library:
            print("Library is empty")
        else:
            print("\nID   Name        Status      Issued To")
            for b in library:
                status = "Issued" if library[b][1] else "Available"
                issued_to = library[b][2] if library[b][1] else "-"
                print(b, library[b][0], status, issued_to)

    

    elif ch == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again")
