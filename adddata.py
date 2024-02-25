import sqlite3
import csv

# Connect to SQLite database (creates it if not existing)
conn = sqlite3.connect('rentalshop.db')
cursor = conn.cursor()

# Open and read the CSV file
with open('./data/Contact.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # Get the header row
    head = next(csv_reader, None)
    if head is not None:
        # Construct the SQL query string
        placeholders = ','.join(['?'] * len(head))
        print(placeholders)
        query = f"INSERT INTO Contact ({','.join(head)}) VALUES ({placeholders})"
        print(query)
        # Insert data from the CSV file into the table
        for row in csv_reader:
            cursor.execute(query, row)

# Commit changes and close connection
conn.commit()
conn.close()