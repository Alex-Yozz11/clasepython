frutas = ["Manzana", "Banana", "Cereza"] #Arrays o arreglo es en plural

for fruta in frutas:
    print(fruta)

for i in range(5): #del 0 al 4
    print(i) 

for i in range(len(frutas)): #len = dimension
    print(frutas[i])

for i in range(4): 
    if i == 5:
        break
    if i % 2 == 0:
        continue
    print(i)
else:
    print("El bucle termino sin break")


    