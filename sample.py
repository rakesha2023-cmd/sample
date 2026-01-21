library = {}

print("---- Library Management System ----")

while True:
    print("\n1.Add  2.Display  3.Search  4.Update  5.Delete  6.Exit")
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
            print("-" * 30)
            for b in library:
                print(f"{b}   {library[b]}")

    elif ch == "3":
        bid = input("Enter Book ID to search: ")
        if bid in library:
            print("Book Found:", library[bid])
        else:
            print("Book not found")

    elif ch == "4":
        bid = input("Enter Book ID to update: ")
        if bid in library:
            new_name = input("Enter New Book Name: ")
            library[bid] = new_name
            print("Book updated successfully")
        else:
            print("Book not found")

    elif ch == "5":
        bid = input("Enter Book ID to delete: ")
        if bid in library:
            confirm = input("Are you sure (y/n)? ")
            if confirm.lower() == "y":
                del library[bid]
                print("Book deleted successfully")
        else:
            print("Book not found")

    elif ch == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again")
