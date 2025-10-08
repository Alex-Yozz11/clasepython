numero = int(input("Ingrese un numero:"))
if (numero > 1):
    es_primo = True

    for i in range(2, numero):
        if (numero % i == 0):
            es_primo = False
            break

    if es_primo:
        print("El numero", numero, "es primo")
    else:
        print("El numero", numero, "no es primo")
else:
    print("El numero debe ser mayor a 1")