#if

edad = 13 
if edad < 13:
    print("Eres un niño")
elif edad < 18: #Caso contrario Si
    print("Eres un adolescente")
else: #Caso contrario
    print("Eres un adulto")


edad = 17
tiene_permiso = False

if edad >= 18:
    print("Puedes entrar")
else:
    if tiene_permiso:
        print("Puedes entrar con permiso")
    else:
        print("No puedes entrar")