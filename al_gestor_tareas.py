from datetime import datetime

"""
*** SISTEMA DE LISTA DE TAREA PERSONAL ***
Estudiantes: Alex Yoza T y Vivian Moran M
El sistema utiliza una lista para almacenar tareas
y aplica operaciones CRUD (Crear, Leer, Actualizar, Eliminar).
"""

print("*** SISTEMA DE LISTA DE TAREA PERSONAL ***")

#Lista en donde se almacenaran todas las tareas
tareas = []

#Creacion de variable para asignar un ID unico cada tarea
siguiente_id = 1


def mostrar_menu():
    print("\n*** GESTOR DE TAREAS PERSONALES ***")
    print("1. Agregar nueva tarea")
    print("2. Ver todas las tareas")
    print("3. Ver solo tareas pendientes")
    print("4. Ver solo tareas completadas")
    print("5. Marcar tarea como completada")
    print("6. Editar tarea")
    print("7. Eliminar tarea")
    print("8. Buscar tareas")
    print("9. Salir")

def agregar_tarea():
    """
    Crea una nueva tarea y la agrega a la lista global 'tareas'.

    Parámetros:
        No recibe parámetros directamente, pero solicita datos al usuario:
        - título (str): nombre de la tarea
        - descripción (str): detalle opcional
        - prioridad (str): nivel de importancia (Alta/Media/Baja)
        - fecha_limite (str): fecha en formato YYYY-MM-DD

    Retorno:
        No retorna nada. Agrega un diccionario con la información de la tarea
        a la lista global 'tareas' y muestra un mensaje de confirmación.
    """
    global siguiente_id
    
    # Solicitar datos al usuario
    print("\nAGREGAR NUEVA TAREA")
    titulo = input("Ingresa titulo de la tarea: ")
    descripcion = input("Ingresa una descripcion opcional: ")
    prioridad = input("Ingresa la prioridad (Alta/Media/Baja): ")
    fecha_limite = input("Ingresa la fecha limite (YYYY-MM-DD) o deja vacio: ")

    # Diccionario creado con la informacion de la tarea
    tarea = {
        "id": siguiente_id,
        "titulo": titulo,
        "descripcion": descripcion,
        "prioridad": prioridad,
        "estado": "Pendiente",
        "fecha_creacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "fecha_limite": fecha_limite
    }

    #Agregar la tarea a la lista principal
    tareas.append(tarea)
    siguiente_id += 1 #Incrementa el ID para la proxima tarea
    print("Tarea agregada correctamente.")

#agregar funcion al punto 2 (poder ver todas las tareas que se asigne)
def ver_todas_tareas():
    """
    Muestra todas las tareas registradas en el sistema.

    Parámetros:
        Ninguno

    Retorno:
        Ninguno. Imprime en pantalla la lista completa de tareas.
    """
    if not tareas:
        print("No hay tareas registradas.")
        return #return devuelve el valor de la funcion
    print("\n*** LISTA DE TAREAS ***")

    for tarea in tareas:
        print("ID:", tarea["id"])
        print("Titulo:", tarea["titulo"])
        print("Descripcion:", tarea["descripcion"])
        print("Prioridad:", tarea["prioridad"])
        print("Estado:", tarea["estado"])
        print("Fecha creacion:", tarea["fecha_creacion"])
        print("Fecha limite:", tarea["fecha_limite"])
        print()

#agregar funcion al punto 3 (observar las tareas que no se han realizado)
def ver_tareas_pendientes():
    """
    Muestra únicamente las tareas que están en estado 'Pendiente'.

    Parámetros:
        Ninguno

    Retorno:
        Ninguno. Imprime en pantalla las tareas pendientes.
    """
    if not tareas:
        print("No hay tareas registradas.")
        return
    print("\n*** TAREAS PENDIENTES ***")
    encontradas = False

    for tarea in tareas:
        if tarea["estado"] == "Pendiente":
            print("ID:", tarea["id"])
            print("Titulo:", tarea["titulo"])
            print("Descripcion:", tarea["descripcion"])
            print("Prioridad:", tarea["prioridad"])
            print("Estado:", tarea["estado"])
            print("Fecha creacion:", tarea["fecha_creacion"])
            print("Fecha limite:", tarea["fecha_limite"])
            print()
            encontradas = True

    if not encontradas:
        print("No hay tareas pendientes.")

#agregar funcion al punto 4 (poder agregar las tareas completadas)
def ver_tareas_completadas():
    """
    Muestra únicamente las tareas que están en estado 'Completada'.

    Parámetros:
        Ninguno

    Retorno:
        Ninguno. Imprime en pantalla las tareas completadas.
    """
    if not tareas:
        print("No hay tareas registradas.")
        return # aquí la función se detiene y no sigue ejecutando el resto
    print("\n*** TAREAS COMPLETADAS ***")
    encontradas = False

    for tarea in tareas:
        if tarea["estado"] == "Completada":
            print("ID:", tarea["id"])
            print("Titulo:", tarea["titulo"])
            print("Descripcion:", tarea["descripcion"])
            print("Prioridad:", tarea["prioridad"])
            print("Estado:", tarea["estado"])
            print("Fecha creacion:", tarea["fecha_creacion"])
            print("Fecha limite:", tarea["fecha_limite"])
            print()
            encontradas = True

    if not encontradas:
        print("No hay tareas completadas.")

#agregar funcion al punto 5 (esta funcion confirma que la tarea ha sido completada)
def marcar_tarea_completada():
    """
    Cambia el estado de una tarea a 'Completada'.

    Parámetros:
        Solicita al usuario el ID de la tarea (int).

    Retorno:
        Ninguno. Actualiza el estado de la tarea seleccionada.
    """
    if not tareas:
        print("No hay tareas registradas.")
        return
    id_buscado = int(input("Ingresa el ID de la tarea a completar: "))
    encontrada = False

    for tarea in tareas:
        if tarea["id"] == id_buscado:
            tarea["estado"] = "Completada"
            print("Tarea marcada como completada.")
            encontrada = True
            break

    if not encontrada:
        print("No se encontro una tarea con ese ID.")

#agregar funcion al punto 6 (Permite modificar lo datos de una tarea exitente)
def editar_tarea():
    """
    Permite modificar los datos de una tarea existente.

    Parámetros:
        Solicita al usuario el ID de la tarea (int).
        Luego pide nuevos valores para título, descripción, prioridad y fecha límite.

    Retorno:
        Ninguno. Actualiza los campos de la tarea seleccionada.
    """
    if not tareas:
        print("No hay tareas registradas.")
        return
    id_buscado = int(input("Ingresa el ID de la tarea que deseas editar: "))
    encontrada = False

    for tarea in tareas:
        if tarea["id"] == id_buscado:
            print("Deja el campo vacio si no deseas cambiarlo.")
            nuevo_titulo = input("Nuevo titulo: ")
            nueva_descripcion = input("Nueva descripcion: ")
            nueva_prioridad = input("Nueva prioridad (Alta/Media/Baja): ")
            nueva_fecha_limite = input("Nueva fecha limite (YYYY-MM-DD): ")
            if nuevo_titulo != "":
                tarea["titulo"] = nuevo_titulo
            if nueva_descripcion != "":
                tarea["descripcion"] = nueva_descripcion
            if nueva_prioridad != "":
                tarea["prioridad"] = nueva_prioridad
            if nueva_fecha_limite != "":
                tarea["fecha_limite"] = nueva_fecha_limite
            print("Tarea editada correctamente.")
            encontrada = True
            break #break rompe el ciclo

    if not encontrada:
        print("No se encontro una tarea con ese ID.")

#agregar funcion al punto 7 (Permite eliminar tarea si hay algo erroneo)
def eliminar_tarea():
    """
    Elimina una tarea de la lista según su ID.

    Parámetros:
        Solicita al usuario el ID de la tarea (int).
        Pide confirmación antes de eliminar.

    Retorno:
        Ninguno. Elimina la tarea si el usuario confirma.
    """
    if not tareas:
        print("No hay tareas registradas.")
        return
    id_buscado = int(input("Ingresa el ID de la tarea que deseas eliminar: "))
    encontrada = False

    for i, tarea in enumerate(tareas):
        if tarea["id"] == id_buscado:
            confirmacion = input("¿Seguro que deseas eliminar esta tarea? (si/no): ")
            if confirmacion.lower() == "si":
                tareas.pop(i)
                print("Tarea eliminada correctamente.")
            else:
                print("Eliminacion cancelada.")
            encontrada = True
            break 

    if not encontrada:
        print("No se encontro una tarea con ese ID.")

#agregar funcion al punto 8 (Busca tarea de manera eficiente)
def buscar_tarea():
    """
    Busca tareas por palabra clave en el título.

    Parámetros:
        Solicita al usuario una palabra clave (str).

    Retorno:
        Ninguno. Imprime las tareas que coinciden con la búsqueda.
    """
    if not tareas:
        print("No hay tareas registradas.")
        return
    palabra = input("Ingresa una palabra para buscar en el titulo: ").lower()
    encontradas = False

    for tarea in tareas:
        if palabra in tarea["titulo"].lower():
            print("ID:", tarea["id"])
            print("Titulo:", tarea["titulo"])
            print("Descripcion:", tarea["descripcion"])
            print("Prioridad:", tarea["prioridad"])
            print("Estado:", tarea["estado"])
            print("Fecha creacion:", tarea["fecha_creacion"])
            print("Fecha limite:", tarea["fecha_limite"])
            print()
            encontradas = True

    if not encontradas:
        print("No se encontraron tareas con esa palabra.")

#Ciclo para cada una de las funciones
    """
Ciclo principal del programa:
- Muestra el menú al usuario
- Recibe la opción seleccionada
- Ejecuta la función correspondiente
- Se repite hasta que el usuario elija salir
"""
while True: # Bucle infinito, se repite hasta que el usuario decida salir
    mostrar_menu()
    opcion = input("Selecciona una opcion: ")
    if opcion == "1":
        agregar_tarea() # Crear nueva tarea
    elif opcion == "2":
        ver_todas_tareas() # Mostrar todas las tareas
    elif opcion == "3":
        ver_tareas_pendientes() # Mostrar solo tareas pendientes
    elif opcion == "4":
        ver_tareas_completadas() # Mostrar solo tareas completadas
    elif opcion == "5":
        marcar_tarea_completada() # Cambiar estado de tarea a completada
    elif opcion == "6":
        editar_tarea()  # Editar una tarea existente
    elif opcion == "7":
        eliminar_tarea()  # Eliminar una tarea
    elif opcion == "8":
        buscar_tarea() # Buscar tarea por palabra clave
    elif opcion == "9":
        print("Saliendo del programa...")  # Mensaje de salida
        break  # Rompe el ciclo y termina el programa
    else:
        print("Opcion invalida.") # Mensaje si el usuario ingresa algo incorrecto


