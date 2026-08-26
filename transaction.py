import sqlite3
from datetime import date, timedelta

def issue_book(book_id, member_id):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # Check if book has available copies
    cursor.execute("SELECT available_copies FROM books WHERE book_id = ?", (book_id,))
    result = cursor.fetchone()

    if not result:
        print("Book not found.")
        conn.close()
        return

    available = result[0]

    if available <= 0:
        print("No copies available to issue.")
        conn.close()
        return

    # Record the transaction
    issue_date = str(date.today())
    due_date = str(date.today() + timedelta(days=14))  # 14 days to return

    cursor.execute("""
    INSERT INTO transactions (book_id, member_id, issue_date, due_date)
    VALUES (?, ?, ?, ?)
    """, (book_id, member_id, issue_date, due_date))

    # Reduce available copies by 1
    cursor.execute("""
    UPDATE books SET available_copies = available_copies - 1 WHERE book_id = ?
    """, (book_id,))

    conn.commit()
    conn.close()
    print(f"Book issued successfully! Due date: {due_date}")


def return_book(transaction_id):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # Get the transaction details
    cursor.execute("SELECT book_id, due_date, return_date FROM transactions WHERE transaction_id = ?", (transaction_id,))
    result = cursor.fetchone()

    if not result:
        print("Transaction not found.")
        conn.close()
        return

    book_id, due_date, return_date = result

    if return_date is not None:
        print("This book was already returned.")
        conn.close()
        return

    today = date.today()
    return_date_str = str(today)

    # Calculate fine if returned late (₹5 per day late)
    due_date_obj = date.fromisoformat(due_date)
    fine = 0
    if today > due_date_obj:
        days_late = (today - due_date_obj).days
        fine = days_late * 5

    # Update the transaction
    cursor.execute("""
    UPDATE transactions SET return_date = ?, fine = ? WHERE transaction_id = ?
    """, (return_date_str, fine, transaction_id))

    # Increase available copies by 1
    cursor.execute("""
    UPDATE books SET available_copies = available_copies + 1 WHERE book_id = ?
    """, (book_id,))

    conn.commit()
    conn.close()

    if fine > 0:
        print(f"Book returned. Late by {days_late} days. Fine: ₹{fine}")
    else:
        print("Book returned on time. No fine.")


def view_transactions():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()

    conn.close()

    if not rows:
        print("No transactions yet.")
        return

    print(f"{'TxnID':<7}{'BookID':<8}{'MemberID':<10}{'IssueDate':<12}{'DueDate':<12}{'ReturnDate':<12}{'Fine':<6}")
    for row in rows:
        return_date = row[5] if row[5] else "Not returned"
        print(f"{row[0]:<7}{row[1]:<8}{row[2]:<10}{row[3]:<12}{row[4]:<12}{return_date:<12}{row[6]:<6}")


if __name__ == "__main__":
    issue_book(1, 1)     # issue book_id 1 to member_id 1
    view_transactions()
    return_book(1)        # return transaction_id 1
    view_transactions()