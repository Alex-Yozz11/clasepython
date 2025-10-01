contador = 0
while contador <= 5:
    print("Contador:", contador)
    contador += 1

isMayorEdad = True
edad = 25
while isMayorEdad:
    if edad < 18:
        print("Eres menor de edad")
        isMayorEdad = False
                        
    edad -= 1
    print("edad:", edad)

print("Fin del ciclo")