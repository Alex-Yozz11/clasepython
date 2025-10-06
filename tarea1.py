
#Tarea_AlexYoza
#Par e impar
print("Par o Impar")
numero = int (input("Ingresa un numero:"))

if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

print()

#Numero primo
print("Numero primo")
num_primo = int (input("Ingresa un numero:"))
es_primo = True

if num_primo <= 1:
    es_primo = False
else:
    for i in range(2, num_primo):
        if num_primo % i == 0:
            es_primo = False
            break

if es_primo:
    print("El numero es primo")
else:
    print("El numero no es primo")

print()

#Serie Fibonacci
n = int(input("Ingrese la cantidad de términos de la serie de Fibonacci que desea generar: "))

a, b = 0, 1

print("Serie de Fibonacci:")
for i in range  (1, n + 1):
    print(a, end = " ")
    c = a + b
    a = b
    b = c
print()
print("Fin del programa")
