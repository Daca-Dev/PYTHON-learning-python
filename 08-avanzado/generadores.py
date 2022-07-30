# Crear un generador

def gen(n):
    for element in range(n):
        print('estoy en el For')
        yield element
    
    print('Ya casi termino :D')
    yield n + 1
    
    print('Ya todo termino')


for item in gen(5):
    print(item)