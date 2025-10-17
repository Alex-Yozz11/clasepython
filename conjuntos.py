frutas = [ "manzana", "pera", "naranja", "manzana"]
print(frutas)
#print(frutas[0]) #esto no se hace en un conjunto

numeros = set([1, 2, 3, 3, 4])
print(numeros)

numeros.add(5)
print(numeros)

numeros.remove(2)
print(numeros)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("Unión", a | b) #union
print("Interseccion", a & b) #interseccion
print("Diferencia", a - b) #diferencia
print("Diferencia simetrica", a ^ b) #diferencia simetrica