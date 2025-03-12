import os
import sqlite3
import pandas as pd

# Folder containing CSV files
folder_path = r"C:\Users\sanskar\Desktop\labels\archivedata"

# SQLite database file
db_path = "database.db"

# Connect to SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Get list of CSV files in the folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

for file in csv_files:
    file_path = os.path.join(folder_path, file)
    
    # Read CSV into DataFrame
    df = pd.read_csv(file_path)

    # Use filename (without .csv) as table name
    table_name = os.path.splitext(file)[0]

    # Store data in SQLite (creates table if not exists)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    
    print(f"Stored {file} in table '{table_name}'.")

# Close connection
conn.close()

print("All CSV files have been stored in the SQLite database.")
