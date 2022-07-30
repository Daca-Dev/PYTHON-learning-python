import psycopg2 as db

conexion = db.connect(user='postgres',
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

cursor = conexion.cursor()
sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
valores = (
    ('Marcos','Cantu','macantu@mail.com'),
    ('Angel','Quintana','aquintana@mail.com'),
    ('Maria','Gonzalez','mgonazalez@mail.com')    
)
cursor.executemany(sentencia, valores)
#guardamos la información en la base de datos
conexion.commit()
registros_insertados = cursor.rowcount
print(f'Registros insertados: {registros_insertados}')
cursor.close()
conexion.close()