"""
The CSU Global Bookstore has a book club that awards points to its students based on the number of books purchased each month. The points are awarded as follows:

If a customer purchases 0 books, they earn 0 points.
If a customer purchases 2 books, they earn 5 points.
If a customer purchases 4 books, they earn 15 points.
If a customer purchases 6 books, they earn 30 points.
If a customer purchases 8 or more books, they earn 60 points.
Write a program that asks the user to enter the number of books that they have purchased this month and then display the number of points awarded.

"""

"""
Return the number of points given the number of books purchased
"""
def points(books):

    if books <= 1:
        return 0
    elif books <= 3:
        return 5
    elif books <= 5:
        return 15
    elif books <= 7:
        return 30
    elif books >= 8:
        return 60
    

def main():
    books = int(input("Enter the number of books you purchased this month:\n"))
    print(f"\nYou have earned {points(books)} points because you purchased {books} books this month.")


if __name__ == "__main__":
    main()
