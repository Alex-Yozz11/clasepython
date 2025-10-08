persona = {"Nombre": "Alex", "edad": 19, "Ciudad": "Guayaquil"}
print(f"Diccionario inicial: {persona}")

print("Edad", persona.get("edad"))
persona ["profesion"] = "Ingeniero"
print ("Persona con profesion:", persona)

print("Claves", persona.keys()) #claves
print("Valores", persona.values()) #valores

persona["Ciudad"] = "Quito"
print("Ciudad modificada", persona)