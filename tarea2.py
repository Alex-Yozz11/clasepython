print("Primer parte de la tarea-filtrar y ordenar")
entrada = [4, 7, 2, 4, 9, 2, 8, 6, 7]
#No repetir numeros
sin_repetir = list(set(entrada)) #Set elimina los valores repetidos 
print("Números sin repetir:", sin_repetir)

#Numeros ordenados
num_ordenado = sorted(sin_repetir) #Sorted ordema de manera ascendente
print("Números ordenados:", num_ordenado)
#Mostrar numeros pares
num_par = [n for n in num_ordenado if n % 2 == 0]
print("Números pares:", num_par)

print("\nSegunda parte de la tarea-tuplas")
numeros = (5, 8, 12, 3, 9, 5, 2)
# Calcular el maximo y el minimo
maximo = max(numeros)
minimo = min(numeros)

print("Máximo:", maximo)
print("Mínimo:", minimo)

#Sacar promedio
promedio = sum(numeros) / len(numeros)
print("Promedio:", round(promedio, 2)) #round = redondeo

#Verificar si un número está dentro de la tupla
num = int(input("Ingrese un número: "))

if num in numeros:
    print(f"El número {num} sí está en la tupla.")
else:
    print(f"El número {num} no está en la tupla.")

print("\nTercera parte de la tarea-diccionarios")
# Diccionario inicial
inventario = {"manzanas": 10, "peras": 3, "naranjas": 8}
print("Inventario inicial:", inventario)

#Agregar un nuevo producto
nuevo_producto = input("Ingrese el nombre del nuevo producto: ").lower()
cantidad = int(input("Ingrese la cantidad en stock: "))
inventario[nuevo_producto] = cantidad
print("Inventario actualizado:", inventario)
#Actualizar cantidad de un producto existente
producto_actualizar = input("Ingrese el nombre del producto que desea actualizar: ").lower()

if producto_actualizar in inventario:
    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
    inventario[producto_actualizar] = nueva_cantidad
else:
    print(f"El producto '{producto_actualizar}' no está en el inventario.")

print("Inventario actualizado:", inventario)

#Mostrar productos con stock menor a 5
print("\nProductos con stock bajo:")
for producto, stock in inventario.items():
    if stock < 5:
        print(f"{producto} - {stock}")


print("\nFin de la tarea 2")

                                            


