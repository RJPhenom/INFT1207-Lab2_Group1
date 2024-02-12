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


def add_book(reading_list):
    # Build book to add as dict obj
    book = {
        "Title" : input("Enter the title of your book: ")
        ,"Author" : input("Enter the author of your book: ")
        ,"Date" : input("Enter the date of your book's publication: ")
    }

    # Add it to the reading list
    reading_list.append(book)

    # Write the new dict to the .csv file to track and save the reading list
    with open('books.csv', 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Title", "Author", "Date"])
        writer.writerow(book)

    # Print confirmation message on execution complete
    print("Book added successfully")

