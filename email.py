print("*** Generador de email ***")

nombre = input("Ingresa tu nombre: ")
apellido = input ("Ingresa tu apellido: ")
empresa = input("Ingresa fecha de empresa: ")
extension_dominio = input("Ingresa extension de dominio: ")

nombre = nombre.strip().lower().replace("" ,".")
apellido = apellido.strip().lower().replace("" ,".")
empresa = empresa.strip().lower().replace("" ,".")
extension_dominio = extension_dominio.strip().lower().replace(" " ,"")

#Numero de id ramndon
email = print(f"{nombre}.{apellido}@{empresa}{extension_dominio}")

print(f"""
    tu email nuevo es:
    {email}
""")