import sqlite3
from datetime import date

def add_member(name, email, phone):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    join_date = str(date.today())

    cursor.execute("""
    INSERT INTO members (name, email, phone, join_date)
    VALUES (?, ?, ?, ?)
    """, (name, email, phone, join_date))

    conn.commit()
    conn.close()
    print(f"Member '{name}' added successfully!")


def view_members():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM members")
    rows = cursor.fetchall()

    conn.close()

    if not rows:
        print("No members registered yet.")
        return

    print(f"{'ID':<5}{'Name':<20}{'Email':<25}{'Phone':<15}{'Join Date':<12}")
    for row in rows:
        print(f"{row[0]:<5}{row[1]:<20}{row[2]:<25}{row[3]:<15}{row[4]:<12}")


if __name__ == "__main__":
    add_member("Rahul Sharma", "rahul@email.com", "9876543210")
    add_member("Priya Singh", "priya@email.com", "9123456789")
    view_members()