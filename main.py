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
            X2PA INT DEFAULT 0 ,
            X2PP FLOAT DEFAULT 0,       
            X3PM INT DEFAULT 0,
            X3PA INT DEFAULT 0,
            X3PP FLOAT DEFAULT 0,
            FGA INT DEFAULT 0,
            FGM INT DEFAULT 0,
            FGP FLOAT DEFAULT 0,
            FTM INT DEFAULT 0,
            FTA INT DEFAULT 0 ,
            FTP FLOAT DEFAULT 0,
            TOTAL_REBS INT DEFAULT 0,
            DR INT DEFAULT 0,
            OR INT DEFAULT 0,
            FOULS INT DEFAULT 0,
            FD INT DEFAULT 0,
            PF INT DEFAULT 0,
            ASSISTS INT DEFAULT 0,
            STEALS INT DEFAULT 0,
            TO INT DEFAULT 0,
            PTS INT DEFAULT 0,
                   CHECK (X2PA>=X2PM),
                   CHECK (X3PA>=X3PM),
                   CHECK (FTA>=FTM)
            );
    UPDATE playerStats
    SET X2PP = ROUND(CAST(X2PM AS DECIMAL)/CAST(X2PA AS DECIMAL)*100,1);
    
    UPDATE playerStats
    SET X3PP = ROUND(CAST(X3PM AS DECIMAL)/CAST(X3PA AS DECIMAL)*100,1);
                   
    UPDATE playerStats
    SET FGA = X2PA + X3PA;
    
    UPDATE playerStats
    SET FGM = X2PM + X3PM;
        
    UPDATE playerStats
    SET FTP = ROUND(CAST(FTM AS DECIMAL)/CAST(FTA AS DECIMAL)*100,1);
    
    UPDATE playerStats
    SET FGP = ROUND(CAST(FGM AS DECIMAL)/CAST(FGA AS DECIMAL)*100,1);
                   
    UPDATE playerStats
    SET PTS = (2*(X2PM)) + (3*(X3PM));
                     
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
