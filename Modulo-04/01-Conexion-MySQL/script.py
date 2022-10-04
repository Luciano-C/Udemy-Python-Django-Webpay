from conectar import *

datos = get_datos("SELECT * FROM productos;")
for dato in datos:
    print(f"{dato[0]} - {dato[1]} - {dato[3]}")


# Modificar datos
set_datos("UPDATE productos SET precio=97897 WHERE id=1;")
# Insertar dato
set_datos("INSERT INTO productos VALUES(null, 'Cuadro de mi mamá', 'Descripción del cuadro', 12345);")
# Borrar dato
set_datos("DELETE from productos WHERE id=1;")
