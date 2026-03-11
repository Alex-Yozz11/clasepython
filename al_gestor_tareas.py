from datetime import datetime

print("""
*** SISTEMA DE LISTA DE TAREA PERSONAL ***
Estudiantes: Alex Yoza T y Vivian Moran M
El sistema utiliza una lista para almacenar tareas
y aplica operaciones CRUD (Crear, Leer, Actualizar, Eliminar).
""")

tareas = []
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

#Agregamos funciones al punto 1
def agregar_tarea():
    global siguiente_id

    print("\nAGREGAR NUEVA TAREA")
    titulo = input("Ingresa titulo de la tarea: ")
    descripcion = input("Ingresa una descripcion opcional: ")
    prioridad = input("Ingresa la prioridad (Alta/Media/Baja): ")
    fecha_limite = input("Ingresa la fecha limite (YYYY-MM-DD) o deja vacio: ")
    tarea = {
        "id": siguiente_id,
        "titulo": titulo,
        "descripcion": descripcion,
        "prioridad": prioridad,
        "estado": "Pendiente",
        "fecha_creacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "fecha_limite": fecha_limite
    }
    tareas.append(tarea)
    siguiente_id += 1
    print("Tarea agregada correctamente.")


def ver_todas_tareas():
    if not tareas:
        print("No hay tareas registradas.")
        return
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


def ver_tareas_pendientes():
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


def ver_tareas_completadas():
    if not tareas:
        print("No hay tareas registradas.")
        return
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


def marcar_tarea_completada():
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


def editar_tarea():
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
            break

    if not encontrada:
        print("No se encontro una tarea con ese ID.")


def eliminar_tarea():
    if not tareas:
        print("No hay tareas registradas.")
        return
    id_buscado = int(input("Ingresa el ID de la tarea que deseas eliminar: "))
    encontrada = False

    for i, tarea in enumerate(tareas):
        if tarea["id"] == id_buscado:
            confirmacion = input("¿Seguro que deseas eliminar esta tarea? (Si/No): ")
            if confirmacion.lower() == "si":
                tareas.pop(i)
                print("Tarea eliminada correctamente.")
            else:
                print("Eliminacion cancelada.")
            encontrada = True
            break

    if not encontrada:
        print("No se encontro una tarea con ese ID.")


def buscar_tarea():
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


while True:
    mostrar_menu()
    opcion = input("Selecciona una opcion: ")
    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        ver_todas_tareas()
    elif opcion == "3":
        ver_tareas_pendientes()
    elif opcion == "4":
        ver_tareas_completadas()
    elif opcion == "5":
        marcar_tarea_completada()
    elif opcion == "6":
        editar_tarea()
    elif opcion == "7":
        eliminar_tarea()
    elif opcion == "8":
        buscar_tarea()
    elif opcion == "9":
        print("Saliendo del programa...")
        break
    else:
        print("Opcion invalida.")