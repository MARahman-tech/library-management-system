import sqlite3

def create_tables():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        isbn TEXT UNIQUE,
        total_copies INTEGER NOT NULL,
        available_copies INTEGER NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS members (
        member_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT,
        phone TEXT,
        join_date TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER,
        member_id INTEGER,
        issue_date TEXT,
        due_date TEXT,
        return_date TEXT,
        fine INTEGER DEFAULT 0,
        FOREIGN KEY (book_id) REFERENCES books (book_id),
        FOREIGN KEY (member_id) REFERENCES members (member_id)
    )
    """)

    conn.commit()
    conn.close()
    print("Tables created successfully!")

if __name__ == "__main__":
    create_tables()