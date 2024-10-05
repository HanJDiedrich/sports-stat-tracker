#import psycopg2
import sqlite3

conn=sqlite3.connect('sample.db')
# Create a cursor object
cursor= conn.cursor()
# Example query
#creating table
def create_table():
    cursor.execute('''
    CREATE TABLE playerStats(
            PlayerName TEXT NOT NULL,
            PlayerNumber INT NOT NULL PRIMARY KEY,
            X2PM INT DEFAULT 0,
            X3PM INT DEFAULT 0,
            X2PA INT DEFAULT 0 ,
            X3PA INT DEFAULT 0,
            FTM DEFAULT 0,
            FTA DEFAULT 0 ,
                   CHECK (X2PA>=X2PM),
                   CHECK (X3PA>=X3PM),
                   CHECK (FTA>=FTM)
            )         
    ''')
    conn.commit()

def insert_player_stats(player_name, player_number, made_2pt, made_3pt, att_2pt, att_3pt, ft_made, ft_attempted):
    cursor.execute('''
        INSERT INTO playerStats (PlayerName, PlayerNumber, X2PM, X3PM, X2PA, X3PA, FTM, FTA)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (player_name, player_number, made_2pt, made_3pt, att_2pt, att_3pt, ft_made, ft_attempted))
    conn.commit()
create_table()
# Example of inserting a player using the function
insert_player_stats('John Doe', 23, 5, 2, 10, 5, 4, 6)

# Fetch and print all data
cursor.execute("SELECT * FROM playerStats")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close the connection
conn.close()
