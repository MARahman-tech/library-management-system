import sqlite3

def add_book(title, author, isbn, total_copies):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO books (title, author, isbn, total_copies, available_copies)
    VALUES (?, ?, ?, ?, ?)
    """, (title, author, isbn, total_copies, total_copies))
    # available_copies starts equal to total_copies since none are borrowed yet

    conn.commit()
    conn.close()
    print(f"Book '{title}' added successfully!")


def view_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()

    conn.close()

    if not rows:
        print("No books in the library yet.")
        return

    print(f"{'ID':<5}{'Title':<20}{'Author':<20}{'ISBN':<15}{'Total':<8}{'Available':<10}")
    for row in rows:
        print(f"{row[0]:<5}{row[1]:<20}{row[2]:<20}{row[3]:<15}{row[4]:<8}{row[5]:<10}")


if __name__ == "__main__":
    add_book("Harry Potter", "J.K. Rowling", "123456", 5)
    add_book("Atomic Habits", "James Clear", "789012", 2)
    view_books()