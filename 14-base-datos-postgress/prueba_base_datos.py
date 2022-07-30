"""

"""

import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password="admin",
    host="127.0.0.1",
    port="5432",
    database="test_db"
)

# nos permitira ejecutar sentencias SQL
cursor = conexion.cursor()
sentencia_sql = 'SELECT * FROM persona'

cursor.execute(sentencia_sql)
registros = cursor.fetchall()

print(registros)

sentencia_sql = 'SELECT * FROM persona ORDER BY id_persona DESC'
cursor.execute(sentencia_sql)
registros = cursor.fetchall()

print(registros)

cursor.close()
conexion.close()