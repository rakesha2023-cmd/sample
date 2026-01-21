library = {}

print("---- Library Management System ----")

while True:
    print("\n1.Add  2.Display  3.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        bid = input("Enter Book ID: ")
        if bid in library:
            print("Book ID already exists")
        else:
            name = input("Enter Book Name: ")
            library[bid] = name
            print("Book added successfully")

    elif ch == "2":
        if not library:
            print("Library is empty")
        else:
            print("\nID   Book Name")
            print("-" * 25)
            for b in library:
                print(b, library[b])

    elif ch == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again")
