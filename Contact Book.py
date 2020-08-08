print("Welcome to the phone book!")

# An empty dictionary to store our entries in
book = {}

# Repeat this loop until they exit
while True:
    # Print the menu options
    print("What would you like to do?")
    print("    1 - Add an entry")
    print("    2 - Lookup an entry")
    print("    3 - Delete an entry")
    print("    4 - Load entries from file")
    print("    5 - Save entries to file")
    print("    6 - Display all entries")
    print("    7 - Exit")
    choice = input("Enter an option: ")

    # Add entry -- unchanged
    if choice == '1':
        name = input('Name: ')
        phone = input('Telephone Number: ')
        book[name] = phone

    # Lookup -- unchanged
    elif choice == '2':
        name = input('Name: ')
        if name in book:
            print("Their number is:", book.get(name))
        else:
            print("There is no entry with " + name)
    # Delete -- unchanged
    elif choice == '3':
        name = input('Name: ')
        del book[name]

    # Load from file -- new
    elif choice == '4':
        # prompt user for filename
        fn = input("Filename: ")

        # open the file for reading
        f = open(fn, "r")

        # for each line in the file
        for line in f:
            # read the line as a colon separated list
            line = line.split(':')

            # the name is the first list item
            name = line[0]

            # the phone number is the second list item
            phone = line[1]

            # put the entry into the phone book
            book[name] = phone

        # close the file when finished
        f.close()

    # Save to file -- new
    elif choice == '5':
        # prompt user for filename
        fn = input("Filename: ")

        # open the file for writing
        f = open(fn, "w")

        # for each entry in the phone book
        for name in book.keys():
            # write the name, then a colon, then the number to a line
            f.write(name + ":" + book[name] + "\n")

        # close the file when finished
        f.close()
    # Displays all entries
    elif choice == '6':
        print("All the entries are:")
        for key, value in sorted(book.items()):
            print(key, ':', value)
        print('*' * 100)
        
    # Quit -- unchanged
    elif choice == '7':
        # exit the loop
        break

    else:
        print('Invalid option.')
