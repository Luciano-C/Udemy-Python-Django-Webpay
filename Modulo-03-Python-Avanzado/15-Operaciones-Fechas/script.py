from datetime import datetime, date, time, timedelta
import time as t
""" 
En la mayoría de los sistemas de bases de datos, las fechas se guardan con el formato Año-Mes-Día 
"""

ahora = datetime.now()
hoy = datetime.today()
hora = t.strftime("%H:%M:%S")
fecha = date.today()
formate_date = "%d-%m-%Y"

#print(ahora, hoy)
#print(hora)
#print(ahora.utcnow())
#print(fecha)
#print(f"Año: {ahora.year}")
#print(f"Fecha: {ahora.day}-{ahora.month}-{ahora.year}")
#print(hoy.strftime(formate_date))
#print(f"Fecha {hoy} | timestamp = {datetime.timestamp(hoy)}")
#print(f"Fecha {fecha} menos 10 días: {fecha - timedelta(days=10)}")

# Weekday: Día 0 => Lunes
#print(f"Día de la semana {datetime.weekday(fecha)}")

# Restar fechas
#fechaCadena = "2021-08-02 00:00:00"
#fechaCadenaFormateada = datetime.strptime(fechaCadena, "%Y-%m-%d %H:%M:%S")
#print(ahora - fechaCadenaFormateada)




