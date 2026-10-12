nombre_sistema = "MBUCHVERS"
# Reemplazamos el número 5 por una Lista real de clientes (Strings entre comillas)
fila_clientes = ["Andrés", "Camila", "Javier", "Paola"]

print(f"Bienvenido a {nombre_sistema}. Sistema en línea.")

# El bucle 'for' extrae cada nombre de la lista, uno por uno
for cliente in fila_clientes:
    print(f"Asignando a un asesor el caso de: {cliente}")

print("La fila está vacía. Todos los clientes fueron atendidos.")