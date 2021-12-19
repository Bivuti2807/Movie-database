import sqlite3
connection=sqlite3.connect('store_movie.db')
cursor=connection.cursor()
command1="""CREATE TABLE IF NOT EXISTS Movies(Movie_name VARCHAR,Actor VARCHAR,Actress VARCHAR,Year_of_release INTEGER,Director_name VARCHAR)"""
cursor.execute(command1)
cursor.execute("INSERT INTO Movies Values('Spider','TOM','MJ',2021,'Tony')")
cursor.execute("INSERT INTO Movies Values('Orphan','Thomson','Jacquline',2016,'John')")
cursor.execute("INSERT INTO Movies Values('End Game','Stark','Wanda',2019,'Russo')")
cursor.execute("INSERT INTO Movies Values('Civil war','TOM','Scarlett',2017,'Kelvin')")
cursor.execute("INSERT INTO Movies Values('Dont Breathe','Bob','Melina',2011,'Rhoades')")
cursor.execute("SELECT * FROM Movies")
cursor.execute("SELECT Movie_name From Movies WHERE Actor ='TOM'")
results=cursor.fetchall()
print(results)