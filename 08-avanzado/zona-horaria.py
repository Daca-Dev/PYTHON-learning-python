from datetime import datetime
import pytz

# Para extraer la zona horaria de un lugar en especifico debes de tener el código
# de la siguiente página
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

bogota_tz = pytz.timezone('America/Bogota')
bogota_date = datetime.now(bogota_tz)
new_york_tz = pytz.timezone('America/New_York')
new_york_date = datetime.now(new_york_tz)

print(bogota_date.strftime('%H-%m-%d %H:%M:%S'))
print(new_york_date.strftime('%H-%m-%d %H:%M:%S'))
