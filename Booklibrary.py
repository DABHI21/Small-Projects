
# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book
# HarryLibrary = Library(listofbooks, library_name)
#dictionary (books-nameofperson)
# create a main function and run an infinite while loop asking
# users for their input


class Library:
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have following books in our {self.name} library: ")
        for book in self.booksList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated. You can take the book now")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addBook(self, book):
        self.booksList.append(book)
        print("Book has been added to the book list")

    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    Dabhi = Library(['Python', 'Rich Daddy Poor Daddy', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'], "JD")

    while(True):
        print(f"Welcome to the {Dabhi.name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        choice = int(input())
        
        if choice == 1:
            Dabhi.displayBooks()

        elif choice == 2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name :")
            Dabhi.lendBook(user, book)

        elif choice == 3:
            book = input("Enter the name of the book you want to add:")
            Dabhi.addBook(book)

        elif choice == 4:
            try : 
                book = input("Enter the name of the book you want to return:")
                Dabhi.returnBook(book)
                print("Thank you for returnig this book")
            except :
                print("You not lend this book from our library")
                
        else:
            print("Enter a valid option")


        print("Press q to quit and c to continue")
        user_choice = ""
        while(user_choice!="c" and user_choice!="q"):
            user_choice = input()
            if user_choice == "q":
                exit()

            elif user_choice == "c":
                continue


