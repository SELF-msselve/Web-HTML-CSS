
import pandas as pd
import sqlite3

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')

# Write the DataFrame to a SQLite table
df.to_sql('people', conn, if_exists='replace', index=False)

# Close the connection
conn.close()
