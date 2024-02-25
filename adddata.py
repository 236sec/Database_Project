import sqlite3
import csv

# Connect to SQLite database (creates it if not existing)
conn = sqlite3.connect('rentalshop.db')
cursor = conn.cursor()

# Open and read the CSV file
with open('./data/category.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # Skip the header row if it exists
    next(csv_reader)
    # Insert data from the CSV file into the table
    for row in csv_reader:
        # Remove the last element from each row (last_update)
        row.pop()  # Remove the last element (last_update)
        cursor.execute('''INSERT INTO Category (CategoryId, CategoryName) 
                          VALUES (?, ?)''', row)


# Commit changes and close connection
conn.commit()
conn.close()