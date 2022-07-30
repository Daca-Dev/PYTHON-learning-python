import psycopg2 as db

conexion = db.connect(user='postgres',
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
entrada = input("Proporciona las pk a buscar (separado por comas): ")
tupla = tuple(entrada.split(','))
#print(tupla)
llaves_primarias = (tupla,)
cursor.execute(sentencia, llaves_primarias)
registros = cursor.fetchall()
for registro in registros:
    print(registro)

cursor.close()
conexion.close()