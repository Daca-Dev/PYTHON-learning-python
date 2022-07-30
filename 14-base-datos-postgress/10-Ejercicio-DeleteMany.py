import psycopg2 as db

conexion = db.connect(user='postgres',
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

cursor = conexion.cursor()
sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
entrada = input("Proporciona las pk a eliminar (separado por comas): ")
tupla = tuple(entrada.split(','))
valores = (tupla,)
cursor.execute(sentencia, valores)
#guardamos la información en la base de datos
conexion.commit()
registros_eliminados = cursor.rowcount
print(f'Registros eliminados: {registros_eliminados}')
cursor.close()
conexion.close()