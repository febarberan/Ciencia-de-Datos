# NO MODIFICAR

# Importar librerías necesarias
from seccion1 import cursor

def check_table_exist(cursor, database, table_name):
    cursor.execute(f"SELECT COUNT(*) FROM information_schema.tables  WHERE table_schema = '{database}'  AND table_name = '{table_name}';")
    if cursor.fetchone()[0] == 1:
        print(f"Tabla {table_name} existe")
        return True
    else:
        print(f"Tabla {table_name} NO existe")
        raise Exception()

def check_table_description_correctness(cursor, table_name, expected_cols):
    for col in expected_cols:
        try:
            cursor.execute(f"SELECT {col} from {table_name} limit 1")
            cursor.fetchall()
        except Exception as e:
            print(f"Tabla {table_name} tiene fallos en su definición, revisa que la query que crea la tabla cumpla con todos los requisitos")
            raise Exception("La definición de la tabla no coincide con el esquema correcto.")

def check_table_import_correctness(cursor, table_name, last_id, total_rows):
  cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE id <= {last_id}")
  if cursor.fetchone()[0] != total_rows:
    print(f"Tabla {table_name} tiene errores en la importación de datos, no tiene la cantidad de filas esperadas")
    raise Exception()
  print(f"Tabla {table_name} tiene la cantidad de filas importadas esperadas")

def check_table_insert_correctness(cursor, table_name, id):
    cursor.execute(f"SELECT * from {table_name} WHERE id = {id}")
    row = cursor.fetchone()
    if row is None:
        print(f"La fila con id {id} no fue insertada en la tabla {table_name}")
        raise Exception()
    print(f"Fila con id {id} insertada en la tabla {table_name} correctamente")


score = 0
try:
    print("\n\nComprobando que las tablas existan...")
    check_table_exist(cursor, 'cine', 'movies')
    check_table_exist(cursor, 'cine', 'reviews')

    print("\nTablas existentes")

    print("\nComprobando que las tablas tengan la definición correcta...")

    check_table_description_correctness(cursor, 'movies', ["id", "title", "released_year", "runtime", "genre", "overview"])
    check_table_description_correctness(cursor, 'reviews', ["id", "movie_id", "stars", "overview"])

    score += 10
    print("\nTablas con definición correcta, +10 puntos\n")

    print("\nRevisando que se hayan importado los archivos correctamente...")

    check_table_import_correctness(cursor, 'movies', 1000, 1000)
    check_table_import_correctness(cursor, 'reviews', 50000, 45340)

    print("\nArchivos importados correctamente, +10 puntos\n")
    score += 10

    print("\nRevisando que se hayan insertado los datos nuevos correctamente...")

    check_table_insert_correctness(cursor, 'movies', 1001)

    print("\nFila insertada a movies correctamente, +5 puntos")
    score += 5

    check_table_insert_correctness(cursor, 'reviews', 54321)

    print("\nFila insertada a reviews correctamente, +5 puntos")
    score += 5


    print(f"\n\nTODO CORRECTO :) Tienes la sección 1 correcta con puntaje máximo: {score} puntos.\n")
    

except Exception as e:
  print(e)
  print("\n\nERROR: Se encontraron errores, no se puede seguir hasta que sean arreglados.\n")
  print(f"\nHasta ahora llevas {score} puntos\n")
