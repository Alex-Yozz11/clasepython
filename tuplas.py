# Tuplas = datosInmutables
ciudades = ("Quito", "Guayaquil", "Cuenca") #Simepre partes de cero, lista y tuplas

print(f"Segunda ciudad: {ciudades[1]}")

try: 
    ciudades[0] = "Ambato"
except TypeError as e: 
    print(f"Error: {e}")

#Transformar de tupla a lista y luego viceversa
ciudades_lista = list(ciudades)
ciudades_lista.append("Ambato")
ciudades = tuple(ciudades_lista)
print(f"Nueva tupla: {ciudades}")

