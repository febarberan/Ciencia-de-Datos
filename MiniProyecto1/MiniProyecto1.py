import mysql.connector

conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123asdzxc",
    database = "infoaeropuertos"
)

# Crea un cursor
cursor = conexion.cursor()

insert_airport = "INSERT INTO airports (id, ident, type,  name,elevation_ft, municipality, iata_code, score) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

tuplas = [

        (39340, "SHCC", "heliport", "Clinica Las Condes Heliport", 2461, "Santiago", " " ,25),
        (39379, "SHMA", "heliport", "Clinica Santa Maria Heliport", 2028, "Santiago"," " ,25),
        (39390, "SHPT", "heliport", "Portillo Heliport", 9000, "Los Andes", " " ,25)
]


cursor.executemany(insert_airport, tuplas)
conexion.commit()



query = "Select name, type, municipality, elevation_ft from airports where elevation_ft > 5000"

cursor.execute(query)
resultados = cursor.fetchall()

for i in resultados:
    name = i[0]
    type = i[1]
    municipality = i[2]
    elevation_ft = i[3]
    print("Name:", name)
    print("Type:", type)
    print("Municipality:", municipality)
    print("elevarion_ft:", elevation_ft)
    print()



       
