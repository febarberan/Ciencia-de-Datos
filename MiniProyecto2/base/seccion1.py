# Importar librerías necesarias
import mysql.connector as db
import mysql.connector
import csv

# Conexión a la base de datos
conn = db.connect(
  host="localhost",
  user="root",
  password="123asdzxc",
  database="cine"
)

# Crear cursor
cursor = conn.cursor()

# Eliminar tablas si están creadas
cursor.execute("DROP TABLE IF EXISTS reviews")
cursor.execute("DROP TABLE IF EXISTS movies")
conn.commit()

#Crear tablas
create_table_movie = "CREATE TABLE movies (id INTEGER PRIMARY KEY,title VARCHAR(255) NOT NULL,released_year INTEGER NOT NULL,runtime INTEGER NOT NULL,genre VARCHAR(255) NOT NULL,overview TEXT);"
create_table_reviews = "CREATE TABLE reviews (id INTEGER PRIMARY KEY,movie_id INTEGER NOT NULL,overview TEXT NOT NULL,stars INTEGER NOT NULL, FOREIGN KEY (movie_id) REFERENCES movies(id));"

cursor.execute(create_table_movie)
cursor.execute(create_table_reviews)

# # Importar archivos a sus respectivas tablas
with open('C:\\Users\\Felipe\\Desktop\\Ciencia de datos\\MiniProyecto2\\base\\data\\movies.csv') as file:
    csvreader = csv.reader(file , delimiter=',')
    next(csvreader)
    filas = []
    for fila in csvreader:
        filas.append(fila)
insertar_movies = '''INSERT INTO movies (id, title , released_year, runtime, genre, overview) VALUES (%s, %s, %s, %s, %s, %s)'''
cursor.executemany(insertar_movies,filas)

with open('C:\\Users\\Felipe\\Desktop\\Ciencia de datos\\MiniProyecto2\\base\\data\\reviews.csv') as file:
    csvreader = csv.reader(file, delimiter=',')
    next(csvreader)
    filas = []
    for fila in csvreader:
      filas.append(fila)
insertar_reviews = '''INSERT INTO reviews (id, movie_id, overview, stars) VALUES (%s, %s, %s, %s)'''
cursor.executemany(insertar_reviews,filas)

conn.commit()
# Insertar una nueva película: id: 1001, title: 'A Walk to Remember', released_year: 2002, runtime: 102, genre: 'Romance', overview: 'The story of two North Carolina teens, Landon Carter and Jamie Sullivan, who are thrown together after Landon gets into trouble and is made to do community service.'
insert_movies = "INSERT INTO movies (id, title , released_year, runtime, genre, overview) VALUES (%s, %s, %s, %s, %s, %s)"

tuplas = [

        (1001, "A Walk to Remember", 2022, 102, "Romance", "The story of two North Carolina teens, Landon Carter and Jamie Sullivan, who are thrown together after Landon gets into trouble and is made to do community service."),
        
]

cursor.executemany(insert_movies, tuplas)
conn.commit()

# Insertar una nueva review para la película 'A Walk to Remember': id:54321, movie_id: 1001, overview: 'Great movie!', stars: 5

insert_reviews = "INSERT INTO reviews (id, movie_id, overview, stars) VALUES (%s, %s, %s, %s)"

tuplas = [

        (54321, 1001, "Great movie!", 5),
        
]

cursor.executemany(insert_reviews, tuplas)
conn.commit()

# NO TOCAR NI CERRAR CONEXIONES, YA ESTÁ IMPLEMENTADO
if __name__ == "__main__":
    # Cerrar conexiones
    cursor.close()
    conn.close()
