
"""
*** SISTEMA DE LISTA DE TAREA PERSONAL ***
Estudiantes: Alex Yoza T y Vivian Moran M
El sistema utiliza una lista para almacenar tareas
y aplica operaciones CRUD (Crear, Leer, Actualizar, Eliminar).
"""

from datetime import datetime

tareas = []
siguiente_id = 1


def mostrar_menu():
    """
    Muestra el menú principal del gestor de tareas.

    Presenta en pantalla las opciones disponibles para que el
    usuario pueda interactuar con el sistema.

    :return: No retorna ningún valor.
    :rtype: None
    """
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
    Agrega una nueva tarea al sistema.

    Solicita al usuario el título, la descripción, la prioridad
    y la fecha límite. Luego crea una nueva tarea con estado
    inicial pendiente y la almacena en la lista.

    :return: No retorna ningún valor.
    :rtype: None
    """
    global siguiente_id

    print("\nAGREGAR NUEVA TAREA")
    titulo = input("Ingresa titulo de la tarea: ")
    descripcion = input("Ingresa una descripcion opcional: ")
    prioridad = input("Ingresa la prioridad (Alta/Media/Baja): ")
    fecha_limite = input("Ingresa la fecha limite (YYYY-MM-DD): ")

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
    """
    Muestra todas las tareas registradas en el sistema.

    Recorre la lista de tareas e imprime la información completa
    de cada una. Si no existen tareas, informa al usuario.

    :return: No retorna ningún valor.
    :rtype: None
    """
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
    """
    Muestra únicamente las tareas pendientes.

    Recorre la lista de tareas y presenta solo aquellas cuyo
    estado es "Pendiente". Si no encuentra ninguna, muestra
    un mensaje informativo.

    :return: No retorna ningún valor.
    :rtype: None
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


def ver_tareas_completadas():
    """
    Muestra únicamente las tareas completadas.

    Recorre la lista de tareas y presenta solo aquellas cuyo
    estado es "Completada". Si no existen tareas completadas,
    informa al usuario.

    :return: No retorna ningún valor.
    :rtype: None
    """
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
    """
    Cambia el estado de una tarea a completada.

    Solicita al usuario el ID de la tarea y, si existe en la lista,
    actualiza su estado a "Completada". Si no la encuentra,
    muestra un mensaje de aviso.

    :return: No retorna ningún valor.
    :rtype: None
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


def editar_tarea():
    """
    Edita los datos de una tarea existente.

    Solicita al usuario el ID de la tarea que desea modificar.
    Si la tarea existe, permite actualizar su titulo, descripcion,
    prioridad y fecha limite.

    :return: No retorna ningún valor.
    :rtype: None
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
            break

    if not encontrada:
        print("No se encontro una tarea con ese ID.")


def eliminar_tarea():
    """
    Elimina una tarea de la lista según su ID.

    Solicita al usuario el ID de la tarea y pide confirmación
    antes de eliminarla. Si la tarea no existe, muestra
    un mensaje informativo.

    :return: No retorna ningún valor.
    :rtype: None
    """
    if not tareas:
        print("No hay tareas registradas.")
        return

    id_buscado = int(input("Ingresa el ID de la tarea que deseas eliminar: "))
    encontrada = False

    for i, tarea in enumerate(tareas):
        if tarea["id"] == id_buscado:
            confirmacion = input("¿Seguro que deseas eliminar esta tarea? (s/n): ")
            if confirmacion.lower() == "s":
                tareas.pop(i)
                print("Tarea eliminada correctamente.")
            else:
                print("Eliminacion cancelada.")
            encontrada = True
            break

    if not encontrada:
        print("No se encontro una tarea con ese ID.")


def buscar_tarea():
    """
    Busca tareas por una palabra clave en el título.

    Solicita al usuario una palabra o texto de búsqueda y
    muestra las tareas cuyos titulos coinciden con el valor
    ingresado.

    :return: No retorna ningún valor.
    :rtype: None
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

def main():
    print("*** SISTEMA DE LISTA DE TAREA PERSONAL ***")
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

if __name__ == "__main__":
    main()