# # ## project3 libraries
# # ## implement the student library system using oops where student can borrow a book from the list of books.
# # ## create a seprate library and student class Your program must be menu driven 
# # ## you are free to choose method and attributes of your choice to implement this functionality

class Library :
    def __init__(self, listOfBooks) :
        self.listOfBooks = listOfBooks

    def displayAvailableBooks (self) :
        print("Books present in the library are")
        for list in self.listOfBooks:
            print(" ->" + list)
        
    def borrowBooks (self, bookName) :
        if bookName in self.listOfBooks:
            print(f"You have been issued {bookName} Please keep it safe and return it within 30 days")
            self.listOfBooks.remove(bookName)
            return True
        else :
            print("Sorry, This book is ethier not available has already been issued to someone else. Please wait untill the book is available")
            return False

    def returnBook (self, bookName) :
        self.listOfBooks.append(bookName)
        print("Thanks for returning the book! Have a great day")


class Student :
    def requestBooks (self) : 
        self.books = input("Enter a name of the book you want to borrow :  ")
        return self.books

    def returnBook (self) :
        self.books = input("Enter the name of the book you want to return :  ")
        return self.books

if __name__ == "__main__" :
    centralLibrary = Library(["python", "javascript", "css", "html"])
    student = Student ()
    # centralLibrary.displayAvailableBooks()   ## This will show the list of the books
    

    while True :

        welcomeMsg = '''
        ---** WellCome To Central Library **---
        Please Choose An Option :
        1. Listing All The Books
        2. Request A Book
        3. Add/AReturn A Book
        4. Exit The Library
        '''
        
        print(welcomeMsg)

        a = int(input("Enter A Choice :  "))

        if a == 1 :
            centralLibrary.displayAvailableBooks ()

        elif a == 2 : 
            centralLibrary.borrowBooks (student.requestBooks())

        elif a == 3 :
            centralLibrary.returnBook (student.returnBook())
        
        elif a == 4 :
            print("Thanks For Choosing Central Library. Have A Great Day")
            exit()

# #############################################################################################################################################        

class Library :
    def __init__(self, bookList) :
        self.booklist = bookList

    def availableBooks (self) :
        print("Books available in Library")
        for book in self.booklist :
            print(" *" + book)

    def bookBorrow (self , nameOfBook) :
        if nameOfBook in self.booklist : 
            print(f"You have been issued {nameOfBook} return with in 30 days")
            self.booklist.remove(nameOfBook)
            return True

        else :
            print("Sorry! Book is either not available or issued to someone else please wait untill available")
            return False

    def bookReturn (self, nameOfBook) : 
        print("Thanks for returning the book")
        self.booklist.append(nameOfBook)

class Student :
    def requestsForBook (self) :
        self.bookname = input("Enter a book name which you want :  ")
        return self.bookname

    def addreturnBook (self) :
        self.bookname = input("Enter a book name you want to add or return :  ")
        return self.bookname

if __name__ == "__main__" :
    freeLibrary = Library (["Algorithims", "Data Structure", "Tree","Django"])
    student = Student()

    while True :
        welcome_message = '''~~~~~~~~** Welcome To Free Library **~~~~~~~~
        1. * Availabe Book list
        2. * Request For Borrow Books
        3. * Add / Return Books
        4. * Exit
        '''

        print(welcome_message)

        a = int(input("choose a number :  "))

        if a == 1 :
            freeLibrary.availableBooks()

        elif a == 2 :
            freeLibrary.bookBorrow(student.requestsForBook())

        elif a == 3 :
            freeLibrary.bookReturn(student.addreturnBook())

        elif a == 4 :
            print("THANKS FOR CHOOSING FREE LIBRARY!")
            exit()

# ##############################################################################################################################################

class Library :
    def __init__(self, booksList) :
        self.booksList = booksList

    def availableBooks (self) :
        for list in self.booksList :
            print(" => " + list)

    def borrowBook (self, nameOfBook) :
        if nameOfBook in self.booksList :
            print(f"you issued {nameOfBook} return it with in 30 days") 
            self.booksList.remove(nameOfBook)
            # return True
        
        else :
            print(f"sorry! currently this book is not available wait untill available")
            # return False
            
    def addorreturnBook (self, nameOfBook) :
        print("Thanks for returning the book")
        self.booksList.append(nameOfBook)

class Student :
    def requestsForBook (self) :
        self.bookName = input("Enter a Book name you want :  ")
        return self.bookName

    def returnBook (self) :
        self.bookName = input("Enter a book name you want to return or add :  ")
        return self.bookName

if __name__ == "__main__" :
    internetLibrary = Library(["Frontend", "Web3", "Stock Market", "Blockchain"])
    student = Student ()

    while True :
        print(''' ------'' WellCome TO Internet Library ''------
        1. * press 1 -> To See The Available List Of Books 
        2. * press 2 -> Borrow The Book 
        3. * press 3 -> Add / Return Book 
        4. * press 4 -> Exit Library
        ''')
        
        a = int(input("Enter a choice :  "))
        
        if a == 1 :
            internetLibrary.availableBooks ()

        elif a == 2 :
            internetLibrary.borrowBook (student.requestsForBook ())

        elif a == 3 :
            internetLibrary.addorreturnBook (student.returnBook ())

        elif a == 4 :
            print ("Thanks! Have A Nice Day")
            exit()
