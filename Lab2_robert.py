###############################################################################
#   Class:          INFT1207
#   Authors:        Robert Macklem
#   Date:           February 11 2024
#   Title:          Reading List Tracker
#   File:           Lab1_robert.py
#   Description:    Reading list program. The program takes in and/or returns
#                   books from a user's reading list, which is stored in .csv
#                   format.
###############################################################################
import csv

# FUNCS
# Function add_book prompts user input for Title, Author, Date to build a book dict, which is then written to books.csv
# to track and save that books as part of the reading list
def add_book():
    # Build book to add as dict obj
    # Use boolean to validate inputs and check for duplicate
    book_valid = False
    duplicate = False

    while not book_valid:
        book = {
            "Title": input("Enter the title of your book: "),
            "Author": input("Enter the author of your book: "),
            "Date": input("Enter the date of your book's publication: ")
        }

        # Boolean tracks if errors were hit
        errors = False
        try:
            # Validate date formatting and not future dated
            int_date = int(book["Date"])

            # If valid format, check if date is greater than current year
            if int_date > 2024:
                print("\n***INPUT ERROR***\nDates cannot be in the future.\nPlease try again.\n")
                errors = True

        # Exception handling for date formatting errors
        except:
            print("\n***INPUT ERROR***\nInvalid date format. (Please use YYYY)\n")
            errors = True

        # Check for null values error
        for key in book:
            if book[key] == "":
                print("\n***INPUT ERROR***\nBook details cannot be null. Please try again.\n")
                errors = True

        # Finally, perform a duplicate check
        duplicate = retrieve_book_title_search(book["Title"])

        book_valid = not errors

    # If not a duplicate, write the new dict to the .csv file to track and save the reading list
    if not duplicate:
        with open('books.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Title", "Author", "Date"])
            writer.writerow(book)

        # Print confirmation message on execution complete
        print("\nBook added successfully")

    # Else, print duplicate warning
    else:
        print("\nDuplicate Detected: Book not added.\n")


# Function retrieve_books retrieves all books in books.csv, essentially acting as a "print all books in the reading
# list" function.
def retrieve_books():
    # Build a dict reader using the .csv
    with open('books.csv', 'r+', newline='') as file:
        reader = csv.DictReader(file, fieldnames=["Title", "Author", "Date"])

        # Print each row using dict struct
        for row in reader:
            print(row["Title"] + ", by " + row["Author"] + ". Published " + row["Date"] + ".")


# Function retrieve_books retrieves all books in books.csv, essentially acting as a "print all books in the reading
# list" function.
def retrieve_book_title_search(title: str):
    # Define return boolean that also tracks if a title was found
    title_found = False

    # Build a dict reader using the .csv
    with open('books.csv', 'r+', newline='') as file:
        reader = csv.DictReader(file, fieldnames=["Title", "Author", "Date"])

        # Search for a matching title using a for loop
        for row in reader:
            if row["Title"].upper() == title.upper():
                print("\n" + row["Title"] + ", by " + row["Author"] + ". Published " + row["Date"] + ".")
                title_found = True  # Title found

        # If a matching title is not found, print notice to user
        if not title_found:
            print("\nSearch Complete: No match found.")

    return title_found


def go_again():
    # Print prompt
    print("\nWould you like to perform another task?\n\nYes (Input any characters)\nNo (Press enter to quit)\n")
    decision = input("")
    not_again = decision == ""
    if not_again:
        return quit_application()

    else:
        return False


# Function quit prints an exit message and returns a bool that, if set to application_quit in mainloop, causes the
# program to exit.
def quit_application():
    print("You selected 'Quit'!\nGoodbye...\n")
    return True


# PROGRAM
# Welcome message
print("\nWelcome to the Reading List Tracker!\n")
print("I would be happy to help you store and track all the wonderful books\nyou would like to read!")

# Program main loop
# Use boolean to keep application running
application_quit = False
while not application_quit:

    # Use boolean to loop while in main menu, waiting for valid operation option (selection var)
    main_menu = True
    selection = 0

    while main_menu:
        print("\nMain Menu")
        print("Please choose from one of the four options:\n\n1:\tAdd Book\n2:\tView Books\n3:\tBook Search\n4:\tQuit")

        # Ensure option selected is valid.
        try:
            selection = int(input("\nInput selection: "))
            if selection in (1, 2, 3, 4):
                main_menu = False
            else:
                print("\n***INVALID SELECTION*** Please enter a number corresponding to the option you wish to select.")

        except:
            print("\n***INPUT ERROR*** Please enter the number corresponding to the option you wish to select.")

    # Switch execution mode based on selection
    match selection:
        case 1:
            print("\nYou selected 'Add Book!\n")
            add_book()
            application_quit = go_again()

        case 2:
            print("\nYou selected 'View Books!\n")
            retrieve_books()
            application_quit = go_again()

        case 3:
            print("\nYou selected 'Search Book!\n")
            retrieve_book_title_search(input("Please enter the title of the book you would like to search for: "))
            application_quit = go_again()

        case 4:
            application_quit = quit_application()


