numeros = [1, 2, 3, 4, 5]
print("Tecer elemento: ", numeros[2])

numeros.append(6) #agrega elemento a la lista
print("Despues de append:", numeros)

numeros.remove(3) #elimina numero de la lista, no elemento
print(f"Despues de remove(3): {numeros}") #Ejecucuion con f"texto: {variable}"

numeros.sort() #Ejecuta 1, 2, 3...
print(f"Ordenados ascendentes: {numeros}")

numeros.sort(reverse = True) #Ejecuta 3, 2, 1
print(f"Ordenados descendentes: {numeros}")

print(f"Dos primeros elementos: {numeros[:2]}") #Toma lo dos primeros elementos

print(F"Dimension de la lista: {len(numeros)}") #len para sabe dimension 

