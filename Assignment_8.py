'''Task 1: The Basic Book
--> Create a class named Book.
--> Define the constructor (__init__) to accept title, author, and isbn (International Standard Book Number).
--> Set title and author as public attributes (self.title).
--> Set the isbn as a private attribute (self.__isbn).
--> Add a public method called get_isbn that safely returns the private __isbn attribute.
-------> Test: Create a Book object and try to access its title and its isbn (show why direct access to __isbn fails).'''

print("---------------------------------------------------------------------------------Task-1")

class Book:
    def __init__(self, title, author, isbn):
        self.title = title #public attribute
        self.author = author  #public attribute 
        self.__isbn = isbn
    
    def get_isbn(self):
        return self.__isbn #safely returns the private __isbn attribute

book1 = Book("The Fault in Our Stars", "John Michael Green", "978-0-525-47881-7")
print(book1.title)
print(book1.author)
#print(book1.__isbn) # private kora hoyche , tai __isbn naam-er kono attribute khuje pabe na
print(book1.get_isbn()) # ei "getter method" holo public method, class er baire theke safely private data ber kore. 

'''Task 2: The Library Catalog
--> Create a class named Library.
--> Define the constructor (__init__) that initializes a protected attribute called self._catalog to an empty list (this list will store Book objects).
--> Add a method add_book(book) that takes a Book object and appends it to the self._catalog list.
--> Add a method get_total_books that returns the length of the self._catalog list.
----> Test: Create 3 Book objects, create a Library object, add the books to the library, and print the total count.'''

print("---------------------------------------------------------------------------------Task-2")

class Library:
    def __init__(self):
        self._catalog = [] #protected attribute
    
    def add_book(self, book):
        self._catalog.append(book) # book obj. list-e add hobe
    
    def get_total_books(self):
        return len(self._catalog)
    
book2 = Book("The Impossible", "Joyce Smith", "9781786540-065")
book3 = Book("Titanic", "Walter Lord", "9780006490-609")
book4 = Book("Tarzan", "Edgar Rice Burroughs", "9783844904-833")

library_obj = Library()

library_obj.add_book(book2)
library_obj.add_book(book3)
library_obj.add_book(book4)

print("The total amount of books are :", library_obj.get_total_books())


'''Task 3: Specialized Book Types
--> Create a class named Magazine that inherits from Book.
--> Define the Magazine constructor to accept title, author, isbn, and a new, unique attribute called issue_number.
--> Inside Magazine.__init__:
--> Use super().__init__(...) to pass the title, author, and isbn up to the Book parent class.
--> Initialize the unique issue_number attribute.
----> Add a method get_type to Magazine that returns the string "Magazine"Test: Create one Book and one Magazine. Show that the Magazine object can still call the inherited get_isbn method.'''

print("---------------------------------------------------------------------------------Task-3")

        
class Magazine(Book):
    def __init__(self, title, author, isbn, issue_number):
        super().__init__(title, author, isbn)
        self.issue_number = issue_number
    
    def get_type(self):
        return "Magazine"

book5 = Book("The Lord of the Rings", "John Ronald Reuel Tolkien", "9788845292-613")
magazine1 = Magazine("The New Yorker", "David Remnick", "9780593801-918", 42)

print(book5.get_isbn())
print(magazine1.get_isbn())
        


'''Task 4: The Patron (User)
--> Create a class named Person.
--> Define the constructor to accept and set name and member_id.
--> Create a class named Librarian that inherits from Person.
--> The Librarian constructor should:Use super() to handle name and member_id.
--> Add a unique attribute called hire_date.
----> Test: Create a Librarian object and confirm it correctly initializes both the inherited member_id and the unique hire_date.'''

print("---------------------------------------------------------------------------------Task-4")

class Person:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

class Librarian(Person):
    def __init__(self, name, member_id, hire_date):
        super().__init__(name, member_id)
        self.hire_date = hire_date

librarian_obj = Librarian("Ute Hansan", "20251130001", "30-November-2025")
print("Librabian's Name :", librarian_obj.name)
print("Librarian's Member ID :", librarian_obj.member_id)
print("Hire date :", librarian_obj.hire_date)


'''Task 5: The Checkout Protocol (Overriding)
--> In the original Book class (the parent), add a public method called display_info(). This method should print: "Title: {title} by {author}".
--> In the inherited Magazine class (the child), override the display_info() method.
--> The overridden method should:Call the parent's display_info() method using super().display_info() to print the title and author.
--> Then, print the unique attribute: "Issue Number: {issue_number}".
----> Test: Create a Book object and a Magazine object, and call display_info() on both to show the different outputs from the same method name.'''

print("---------------------------------------------------------------------------------Task-5")

class Book:
    def __init__(self, title, author, isbn):
        self.title = title #public attribute
        self.author = author  #public attribute 
        self.__isbn = isbn
    
    def get_isbn(self):
        return self.__isbn #safely returns the private __isbn attribute
    
    def display_info(self):
        print(f"Title: {self.title} by {self.author}")    



class Magazine(Book):
    def __init__(self, title, author, isbn, issue_number):
        super().__init__(title, author, isbn)
        self.issue_number = issue_number
    
    def get_type(self):
        return "Magazine"
    
    def display_info(self):
        super().display_info()  # pchile override korle parent run hoy na, tai abar super() diye parent method ke run korano holo
        print(f"Issue Number: {self.issue_number}") # child-specific info
        

book6 = Book("Harry Potter", "J. K. Rowling", "978-0545162-074")
magazine2 = Magazine("Time", "Briton Hadden", "0040-781X", 56)

# print("Book no 6 :", book6.display_info())
# print("Magazine no 2 :", magazine2.display_info())

print("Book no 6:")
book6.display_info()

print("Magazine no 2:")
magazine2.display_info()



'''Task 6: The Abstract Loan Processor
--> In the Library class, add a method called loan_item(item) that takes either a Book or a Magazine object.
--> This method should polymorphically call the object's display_info() method.
--> Use a list called inventory = [book_instance, magazine_instance].
--> Use a for loop to iterate over the inventory list and call loan_item(item) for each one.
----> Goal: This loop should seamlessly call the correct, customized display_info() for each type of item, demonstrating that the code works generally (polymorphically).'''
print("---------------------------------------------------------------------------------Task-6")


class Library:
    def __init__(self):
        self._catalog = [] #protected attribute
    
    def add_book(self, book):
        self._catalog.append(book) # book obj. list-e add hobe
    
    def get_total_books(self):
        return len(self._catalog)
    
    def loan_item(self, item):
        print("Loaned item info:")
        item.display_info()  # polymorphic call kora holo

book_instance = book6
magazine_instance = magazine2

inventory = [book_instance, magazine_instance]

library = Library()

for item in inventory:
    library.loan_item(item)
    
    
'''Task 7: The Abstract Library Item

===> Goal: Create an abstract blueprint that forces all inventory items to have a unique ID and a method for checking availability.
--> Import ABC and abstractmethod from the abc module.
--> Define an Abstract Base Class (ABC) called LibraryItem that inherits from ABC.
--> Define a regular method in LibraryItem called get_unique_id(self) that simply returns the item's ID (e.g., self.isbn or some other internal ID).
--> Define an abstract method using the @abstractmethod decorator called check_availability(self). This method should contain only pass (as it has no implementation here).
----> Test: Try to create an object directly from LibraryItem (e.g., item = LibraryItem()). The student should observe that this correctly raises a TypeError.'''

print("---------------------------------------------------------------------------------Task-7")

from abc import ABC, abstractmethod

class LibraryItem(ABC):
    @abstractmethod
    def get_unique_id(self):
        return self.isbn
    
    @abstractmethod
    def check_availability(self):
        pass
item = LibraryItem()

    
'''Task 8: Implementing the Abstract Protocol

===> Goal: Modify the existing Book class to adhere to the abstract contract and demonstrate that the system now enforces it.
--> Modify the Book class from Task 1 so that it inherits from LibraryItem (e.g., class Book(LibraryItem):).
--> Implement the abstract method check_availability(self) inside the Book class. This method should return a simple boolean value, like True for available.

Test 1 (Success): Create a Book object and call the inherited non-abstract method get_unique_id() and the implemented abstract method check_availability().
Test 2 (Failure): Create a new class, DVD, that inherits from LibraryItem but fails to implement check_availability(). Attempt to instantiate a DVD object 
        and observe that it correctly raises a TypeError, proving the abstract contract is enforced.'''

print("---------------------------------------------------------------------------------Task-8")

from abc import ABC, abstractmethod


class LibraryItem(ABC):
    def get_unique_id(self):
        return self.isbn

    @abstractmethod
    def check_availability(self):
        pass
    

class Book(LibraryItem):
    def __init__(self, title, author, isbn):
        self.title = title #public attribute
        self.author = author  #public attribute 
        self.isbn = isbn


    def check_availability(self):
        return True  

book7 = Book("Clean Code", "Robert C. Martin", "9780132350884")

print("Book Unique ID:", book7.get_unique_id())        # inherited method
print("Book Available?", book7.check_availability())  # implemented abstract method


class DVD(LibraryItem):
    def __init__(self, code):
        self.isbn = code
    
try:
    dvd1 = DVD("DVD-249530001")

except TypeError as e:
    print("Error:", e)


