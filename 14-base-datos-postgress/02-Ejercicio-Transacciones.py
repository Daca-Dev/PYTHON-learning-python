import psycopg2 as db

conexion = db.connect(user='postgres',
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')
try:
    #conexion.autocommit = True
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    valores = ('Maria','Esparza','mesparza@mail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    valores = ('Juan1','Perez2','jperez3@mail.com', 1)
    cursor.execute(sentencia, valores)

    #guardamos la información en la base de datos
    conexion.commit()
    print('Concluyó con éxito la transacción')
except Exception as e:
    #rollback da marcha atras a todas las operaciones pendientes
    conexion.rollback()
    print(f'Ocurrió un error en la transacción: {e}')
finally:
    cursor.close()
    conexion.close()