from datetime import date as dt
from datetime import timedelta

BORROW_LIMIT = 3


class Library:


    def __init__(self, name):
        self.name = name
        self.fine_per_day = 5
        self.books = []
        self.members = []


    def list_books(self):

        if not self.books:
            print("\nNo books available!")
            return

        print("\nBOOKS AVAILABLE:\n")

        for book in self.books:
            print(book)


    def list_members(self):

        if not self.members:
            print("\nNo members found!")
            return

        print("\nCURRENT MEMBERS:\n")

        for member in self.members:
            print(member)


    def find_book(self, keyword):

        found = False

        for book in self.books:

            if (
                keyword.lower() in book.title.lower()
                or keyword.lower() in book.author.lower()
            ):
                print(book)
                found = True

        if not found:
            print("\nBook not found!")


    def find_member(self, keyword):

        found = False

        for member in self.members:

            if (
                keyword.lower() in member.name.lower()
                or keyword.lower() in member.mem_id.lower()
            ):
                print(member)
                found = True

        if not found:
            print("\nMember not found!")



class Book:

    next_id = 1000

    def __init__(self, title, author, rate, copies):

        self.id = Book.next_id
        Book.next_id += 1

        self.title = title
        self.author = author
        self.rate = rate
        self.copies = copies
        self.available_copies = copies


    def __str__(self):

        return (
            f"ID:{self.id} | "
            f"{self.title.title()} by {self.author.title()} | "
            f"Available: {self.available_copies}/{self.copies} | "
            f"Rate: ${self.rate}/day"
        )


class Member:

    next_id = 1


    def __init__(self, name):

        self.name = name
        self.mem_id = f"MEM{Member.next_id:04d}"
        Member.next_id += 1

        self.num_borrowed = 0
        self.borrowed_books = {}


    def borrow_book(self, library, book):

        if self not in library.members:
            print(f"\n{self.name} is not a member!")
            return

        if book not in library.books:
            print("\nBook not found!")
            return

        if self.num_borrowed >= BORROW_LIMIT:
            print(
                f"\nBorrow limit reached! "
                f"Maximum allowed: {BORROW_LIMIT}"
            )
            return

        if book.available_copies <= 0:
            print("\nNo copies available!")
            return

        if book.title.upper() in self.borrowed_books:
            print("\nYou already borrowed this book!")
            return


        due_date = dt.today() + timedelta(days=7)

        self.borrowed_books[book.title.upper()] = due_date.isoformat()

        self.num_borrowed += 1
        book.available_copies -= 1

        print(
            f"\n{book.title.upper()} borrowed successfully!"
            f"\nDue Date: {due_date}"
        )


    def return_book(self, library, book):

        if book.title.upper() not in self.borrowed_books:
            print("\nThis member has not borrowed that book!")
            return

        due_date = dt.fromisoformat(
            self.borrowed_books[book.title.upper()]
        )


        today = dt.today()

        days_late = (today - due_date).days

        book.available_copies += 1
        self.num_borrowed -= 1

        del self.borrowed_books[book.title.upper()]

        if days_late > 0:

            fine = days_late * library.fine_per_day

            print(
                f"\nLate by {days_late} days."
                f"\nFine: ${fine}"
            )

        print(
            f"\n{book.title.upper()} returned successfully!"
        )


    def __str__(self):

        return (
            f"{self.name.title()} | "
            f"{self.mem_id} | "
            f"Borrowed: {self.num_borrowed}"
        )


class Librarian:

    def __init__(self, name, library):

        self.name = name
        self.library = library

    def add_book(self, new_book):

        for book in self.library.books:

            if (
                book.title.lower() == new_book.title.lower()
                and book.author.lower() == new_book.author.lower()
            ):

                book.copies += new_book.copies
                book.available_copies += new_book.copies

                print(
                    f"\nAdded {new_book.copies} more copies of "
                    f"{book.title.title()}"
                )
                return

        self.library.books.append(new_book)

        print(
            f"\n{new_book.title.title()} added successfully!"
        )


    def remove_book(self, book_to_remove):

        for book in self.library.books:

            if book.id == book_to_remove.id:

                if book.available_copies != book.copies:
                    print(
                        "\nCannot remove book."
                        " Some copies are currently borrowed!"
                    )
                    return

                self.library.books.remove(book)

                print(
                    f"\n{book.title.title()} removed successfully!"
                )
                return

        print("\nBook not found!")


    def add_member(self, member):

        for existing_member in self.library.members:

            if existing_member.name.lower() == member.name.lower():
                print("\nMember already exists!")
                return

        self.library.members.append(member)

        print(
            f"\n{member.name.title()} "
            f"({member.mem_id}) added successfully!"
        )


    def remove_member(self, member):

        for existing_member in self.library.members:

            if existing_member.mem_id == member.mem_id:

                if existing_member.num_borrowed > 0:
                    print(
                        "\nMember still has borrowed books!"
                    )
                    return

                self.library.members.remove(existing_member)

                print(
                    f"\n{existing_member.name.title()} removed successfully!"
                )
                return

        print("\nMember not found!")


    def list_members(self):

        self.library.list_members()


#TESTING

library = Library("City Library")

librarian = Librarian("Alex", library)

book1 = Book("Atomic Habits", "James Clear", 2, 4)
book2 = Book("Incognito", "David Eagleman", 1, 2)
book3 = Book("Harry Potter", "J.K. Rowling", 3, 5)

librarian.add_book(book1)
librarian.add_book(book2)


member1 = Member("John")
member2 = Member("Lisa")

librarian.add_member(member1)
librarian.add_member(member2)

library.list_books()

member1.borrow_book(library, book1)
member1.borrow_book(library, book2)

member1.return_book(library, book3)

library.find_book("atomic")
library.find_member("john")

librarian.list_members()