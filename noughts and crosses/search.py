import sqlite3

# Connect to the database
conn = sqlite3.connect('training.db')
cursor = conn.cursor()

# Execute the delete query
cursor.execute("SELECT * FROM game_data WHERE pos0 = 0 AND pos1 = 0 AND pos2 = 0 AND pos3 = 0 AND pos4 = 0 AND pos5 = 0 AND pos6 = 0 AND pos7 = 0 AND pos8 = 0")

# Commit the changes
result = cursor.fetchall()
print(result)

# Close the connection
conn.close()