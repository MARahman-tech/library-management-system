from book import add_book, view_books
from member import add_member, view_members
from transaction import issue_book, return_book, view_transactions

def menu():
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Add Member")
        print("4. View Members")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. View Transactions")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            copies = int(input("Enter total copies: "))
            add_book(title, author, isbn, copies)

        elif choice == "2":
            view_books()

        elif choice == "3":
            name = input("Enter member name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            add_member(name, email, phone)

        elif choice == "4":
            view_members()

        elif choice == "5":
            book_id = int(input("Enter book ID: "))
            member_id = int(input("Enter member ID: "))
            issue_book(book_id, member_id)

        elif choice == "6":
            transaction_id = int(input("Enter transaction ID: "))
            return_book(transaction_id)

        elif choice == "7":
            view_transactions()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()