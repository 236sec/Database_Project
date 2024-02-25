import sqlite3
import csv

# Connect to SQLite database (creates it if not existing)
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Create a table (replace 'your_table' and 'column1', 'column2', etc. with actual names)
cursor.execute('''CREATE TABLE IF NOT EXISTS your_table (
                    column1 TEXT,
                    column2 TEXT,
                    column3 INTEGER,
                    ...
                    )''')

# Open and read the CSV file
with open('your_file.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # Skip the header row if it exists
    next(csv_reader)
    # Insert data from the CSV file into the table
    for row in csv_reader:
        cursor.execute('''INSERT INTO your_table (column1, column2, column3, ...) 
                          VALUES (?, ?, ?, ...)''', row)

# Commit changes and close connection
conn.commit()
conn.close()