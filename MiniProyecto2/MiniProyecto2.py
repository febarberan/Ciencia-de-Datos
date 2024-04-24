import mysql.connector

conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123asdzxc",
    database = "cine"
)

# Crea un cursor
cursor = conexion.cursor()

create_table_movie = "CREATE TABLE movies (id INTEGER PRIMARY KEY,title VARCHAR(255) NOT NULL,released_year INTEGER NOT NULL,runtime INTEGER NOT NULL,genre VARCHAR(255) NOT NULL,overview TEXT);"
create_table_reviews = "CREATE TABLE reviews (id INTEGER PRIMARY KEY,movie_id INTEGER NOT NULL,overview TEXT NOT NULL,stars INTEGER NOT NULL,FOREIGN KEY (movie_id) REFERENCES movies(id));"

select = "Select * from movie"
cursor.execute(create_table_movie)
cursor.execute(create_table_reviews)
cursor.execute(select)

conexion.commit()