library = {}

while True:
    print("1.Add 2.Display 3.Issue 4.Return 5.Exit")
    ch = input("Choice: ")

    if ch == "1":
        bid = input("Book ID: ")
        name = input("Book Name: ")
        library[bid] = [name, False]
        print("Book Added\n")

    elif ch == "2":
        for b in library:
            status = "Issued" if library[b][1] else "Available"
            print(b, library[b][0], status)
        print()

    elif ch == "3":
        bid = input("Book ID: ")
        if bid in library and not library[bid][1]:
            library[bid][1] = True
            print("Book Issued\n")
        else:
            print("Not Available\n")

    elif ch == "4":
        bid = input("Book ID: ")
        if bid in library and library[bid][1]:
            library[bid][1] = False
            print("Book Returned\n")
        else:
            print("Invalid\n")

    elif ch == "5":
        break

    else:
        print("Wrong Choice\n")
