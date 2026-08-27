# Library Management System

A command-line based Library Management System built with Python and SQLite. Allows library staff to manage books, members, and track book issues/returns with automatic fine calculation for late returns.

## Features

- **Book Management**: Add new books and view all books with available copy counts
- **Member Management**: Register new members and view all registered members
- **Issue/Return System**: Issue books to members, track due dates, and process returns
- **Fine Calculation**: Automatically calculates late fees (₹5/day) for overdue returns
- **Interactive Menu**: Simple command-line interface for all operations

## Tech Stack

- **Language**: Python
- **Database**: SQLite

## Database Schema

The system uses 3 relational tables:
- `books` — stores book details and copy availability
- `members` — stores member details
- `transactions` — links books and members, tracking issue/due/return dates and fines

## How to Run

1. Clone this repository
```bash
git clone https://github.com/MARahman-tech/library-management-system.git
cd library-management-system
```

2. Run the database setup (creates the tables, only needed once)
```bash
python database.py
```

3. Run the main program
```bash
python main.py
```

4. Follow the on-screen menu to add books, register members, issue/return books, and view records

## Project Structure