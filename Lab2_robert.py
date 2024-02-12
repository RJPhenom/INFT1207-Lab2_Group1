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

# CONSTS

# VARS

# FUNCS
# mandatory linebreaks for asinine pep8 requirements in JetBrain(les)s


# Function add_book prompts user input for Title, Author, Date to build a book dict, which is then written to books.csv
# to track and save that books as part of the reading list
def add_book(reading_list):
    # Build book to add as dict obj
    book = {
        "Title": input("Enter the title of your book: "),
        "Author": input("Enter the author of your book: "),
        "Date": input("Enter the date of your book's publication: ")
    }

    # Add it to the reading list
    reading_list.append(book)

    # Write the new dict to the .csv file to track and save the reading list
    with open('books.csv', 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Title", "Author", "Date"])
        writer.writerow(book)

    # Print confirmation message on execution complete
    print("Book added successfully")


# Function retrieve_books retrieves all books in books.csv, essentially acting as a "print all books in the reading
# list" function.
def retrieve_books(reading_list):
    # Build a dict reader using the .csv
    with open('books.csv', 'a', newline='') as file:
        reader = csv.DictReader(file, fieldnames=["Title", "Author", "date"])

        # Print each row using dict struct
        for row in reader:
            print(row["Title"], ", by ", row["Author"], ". Published ", row["Date"])


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
        case 2:
            print("\nYou selected 'View Books!\n")
        case 3:
            print("\nYou selected 'Search Book!\n")
        case 4:
            print("\nYou selected 'Quit!\nGoodbye...")
            application_quit = True
