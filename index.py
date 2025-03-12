import os
import sqlite3
import pandas as pd

# Specify the folder containing CSV files
folder_path = r"C:\Users\sanskar\Desktop\labels\archivedata"  # Change this to your folder path
database_name = "archive_store.db"

# Connect to SQLite database (or create if it doesn't exist)
conn = sqlite3.connect(database_name)
cursor = conn.cursor()

# Function to create a table and insert CSV data
def store_csv_to_sqlite(csv_file, table_name):
    df = pd.read_csv(csv_file)  # Read CSV into DataFrame
    
    # Create table dynamically based on DataFrame columns
    columns = ", ".join([f'"{col}" TEXT' for col in df.columns])
    create_table_query = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns});'
    cursor.execute(create_table_query)

    # Insert data into the table
    df.to_sql(table_name, conn, if_exists='append', index=False)

# Process all CSV files in the folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

if len(csv_files) == 5:  # Ensure only 3 CSV files are processed
    for csv_file in csv_files:
        csv_path = os.path.join(folder_path, csv_file)
        table_name = os.path.splitext(csv_file)[0]  # Use filename as table name
        store_csv_to_sqlite(csv_path, table_name)

    # Commit and close connection
    conn.commit()
    print("CSV data successfully stored in SQLite database!")
else:
    print("Error: The folder must contain exactly 3 CSV files.")

conn.close()
