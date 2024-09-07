import sqlite3

conn = sqlite3.connect('training.db')
c = conn.cursor()

# Create table  
c.execute('''CREATE TABLE IF NOT EXISTS game_data
             (id INTEGER PRIMARY KEY,
              board TEXT UNIQUE,
              pos0 INTEGER,
              pos1 INTEGER,
              pos2 INTEGER,
              pos3 INTEGER,
              pos4 INTEGER,
              pos5 INTEGER,
              pos6 INTEGER,
              pos7 INTEGER,
              pos8 INTEGER)''')

conn.commit()