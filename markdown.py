import os
import pandas as pd

# Specify the folder containing CSV files
folder_path = r"C:\Users\sanskar\Desktop\labels\archivedata"  # Change this to your folder path

# Function to convert CSV to Markdown and save as .md file
def convert_csv_to_markdown(csv_file, md_file):
    df = pd.read_csv(csv_file)  # Read CSV into DataFrame
    markdown_data = df.to_markdown(index=False)  # Convert DataFrame to Markdown format
    
    # Save as .md file
    with open(md_file, "w", encoding="utf-8") as f:
        f.write(markdown_data)
    
    print(f"Converted {csv_file} -> {md_file}")

# Process all CSV files in the folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

if len(csv_files) == 5:  # Ensure exactly 3 CSV files
    for csv_file in csv_files:
        csv_path = os.path.join(folder_path, csv_file)
        md_path = os.path.join(folder_path, os.path.splitext(csv_file)[0] + ".md")
        convert_csv_to_markdown(csv_path, md_path)

    print("All CSV files converted to Markdown successfully!")
else:
    print("Error: The folder must contain exactly 3 CSV files.")
