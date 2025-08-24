#Write a program to create a menu-driven Library Management System that can do these four tasks - display a book, lend or return a book and add a book. Make use of OOPs concepts, loops and conditional statements wherever required.

class Library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lendDict = {}
    def displayBooks(self):
        print("We have the following books in our library", self.name)
        for book in self.booklist:
            print(book)
    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender book database has been updated, you may take the book now")
        else:
            print("The book has been already used by", self.lendDict[book])
    def addbook(self, book):
        self.booklist.append(book)
        print("The book has been added to the booklist")
    def returnbook(self, book):
        self.lendDict.pop(book)

#Main programme

if __name__ == "__main__":
    books = Library(["Science book", "Math book", "Python book", "Story book", "Biology book"], "MyLibrary")
    while True:
        print("Welcome to the library, enter your choise to continue.")
        print("Press 1 to display books, 2 to lend a book, 3 to add a book, 4 to return a book.")
        userchoise = input()

        if userchoise not in ['1', '2', '3', '4']:
            print("That is not an option. Enter a valid option")
            continue
        else:
            userchoise = int(userchoise)
        if userchoise == 1:
            books.displayBooks()
        elif userchoise == 2:
            book = input("Enter the name of the book")
            user = input("Enter their name.")
            books.lendBook(user, book)
        elif userchoise == 3:
            book = input("Enter the name of the book")
            books.addbook(book)
        elif userchoise == 4:
            book = input("Enter the name of the book")
            books.returnbook(book)
        else:
            print("NOT A VALID OPTION!")
        print("Press 'Q' to quit and 'C' to continue")
        
        userchoise2 = ""
        while userchoise2 != "C" and userchoise2 != "Q":
            userchoise2 = input()
            if userchoise2 == "Q":
                exit()
            elif userchoise2 == 'C':
                continue

    