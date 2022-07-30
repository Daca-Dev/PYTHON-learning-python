import datetime

# Imprime la fecha y hora en el moemnto exacto en que fue invocada
# la función. (Hora local de la maquina)
my_time = datetime.datetime.now()
print(my_time)

# obtener solo el día
my_day = datetime.datetime.today()
print(f'year: {my_day.year}')
print(f'month: {my_day.month}')
print(f'day: {my_day.day}')

# Formateo de fechas
date_str = datetime.datetime.now().strftime('El día es %Y/%m/ %d y la hora es %H:%M:%S')
print(date_str)