# Importar librerías necesarias
import mysql.connector as db

# Conexión a la base de datos
conn = db.connect(
  host="localhost",
  user="root",
  password="123asdzxc",
  database="cine"
)

# Crear cursor
cursor = conn.cursor()

# Consultas

# 1. Obtener el título de las películas que tengan una duración mayor a 180 minutos, y ordenarlos por id de forma ascendente
query1 = "Select title from movies where runtime > 180 order by id asc"
cursor.execute(query1)
rows = cursor.fetchall()
print("1. Películas con duración mayor a 180 minutos:")
for row in rows:
    print(row)

# 2. Obtener toda la información de las reviews para la película '12 Angry Men' y ordenarlas por id de forma ascendente
query2 = "Select rs.id, rs.movie_id, rs.overview , rs.stars from reviews rs join movies mv on (rs.movie_id = mv.id) where mv.title = '12 Angry Men' order by id asc  "
cursor.execute(query2)
rows = cursor.fetchall()
print("\n2. Películas con calificación de 5 estrellas:")
for row in rows:
    print(row)

# 3. Obtener el promedio de stars para la película 'Pulp Fiction'
query3 = "Select Round(AVG(stars),2) from reviews rs join movies mv on(rs.movie_id = mv.id ) where title = 'Pulp Fiction'"
cursor.execute(query3)
rows = cursor.fetchall()
print("\n3. Promedio de estrellas para la película Pulp Fiction:")
for row in rows:
    print(row)

# 4. Obtener el título y el promedio de stars para las 10 películas con el promedio de stars más alto, debe estar ordenado de mayor a menor promedio
query4 = "Select mv.title, ROUND(AVG(rs.stars),2) from movies mv JOIN reviews rs on(rs.movie_id = mv.id) Group by mv.title order by AVG(rs.stars) asc LIMIT 10  "
cursor.execute(query4)
rows = cursor.fetchall()
print("\n4. Película con el promedio de estrellas más alto:")
for row in rows:
    print(row)

# 5. Obtener el número de reviews con 5 stars que tiene la película 'The Shawshank Redemption'
query5 = "Select Count(rs.id) from reviews rs JOIN movies mv on(rs.movie_id = mv.id) where rs.stars = 5 and mv.title = 'The Shawshank Redemption' "
cursor.execute(query5)
rows = cursor.fetchall()
print("\n5. Número de reviews con 5 estrellas para la película The Shawshank Redemption:")
for row in rows:
    print(row)



# NO TOCAR NI CERRAR CONEXIONES, YA ESTÁ IMPLEMENTADO
if __name__ == "__main__":
    print("cerrando conexiones")
    # Cerrar conexiones
    cursor.close()
    conn.close()