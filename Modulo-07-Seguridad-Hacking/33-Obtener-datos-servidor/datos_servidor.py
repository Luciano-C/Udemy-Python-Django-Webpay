import platform
import psutil
import multiprocessing
import sys

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
    



print(f"Número de CPU del sistema: {psutil.cpu_count()}")
print(f"Número de CPU del sistema: {multiprocessing.cpu_count()}")
print(f"Tipo de máquina: {platform.machine()}")
print(f"Tipo de máquina: {platform.architecture()[0]}")
print(f"Tipo de software: {platform.python_compiler()}")
print(f"Modelo o liberación del sistema: {platform.release()}")
print(f"Hostname: {platform.node()}")
print(f"Plataforma base: {platform.platform()}")
print(f"Tipo de SO: {platform.version()}")
print(f"Tipo de procesador: {platform.processor()}")
print(f"Información del sistema: {platform.uname()}")
print(f"Versión Python: {platform.python_version()}")

print("----------Datos de la memoria---------")
svmem = psutil.virtual_memory()
print(
    f"Total: {get_size(svmem.total)} | Disponible: {get_size(svmem.available)} | Usada: {get_size(svmem.used)} | Porcentaje: {svmem.percent}%"
    )
swap = psutil.swap_memory()
print(
    f"Total: {get_size(swap.total)} | Libre: {get_size(swap.free)} | Usada: {get_size(swap.used)} | Porcentaje: {swap.percent}%"
)