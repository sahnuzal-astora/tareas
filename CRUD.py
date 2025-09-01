
estudiantes = []

# CREATE
def crear_estudiante(nombre, edad):
    estudiante = {"nombre": nombre, "edad": edad}
    estudiantes.append(estudiante)
    print(f" Estudiante {nombre} agregado con éxito.")

# READ
def leer_estudiantes():
    if not estudiantes:
        print("⚠ No hay estudiantes registrados.")
    else:
        print("\n Lista de estudiantes:")
        for i, est in enumerate(estudiantes, start=1):
            print(f"{i}. {est['nombre']} - {est['edad']} años")

# UPDATE
def actualizar_estudiante(indice, nuevo_nombre=None, nueva_edad=None):
    if 0 <= indice < len(estudiantes):
        if nuevo_nombre:
            estudiantes[indice]["nombre"] = nuevo_nombre
        if nueva_edad:
            estudiantes[indice]["edad"] = nueva_edad
        print(" Estudiante actualizado con éxito.")
    else:
        print("⚠ Índice inválido.")

# DELETE
def eliminar_estudiante(indice):
    if 0 <= indice < len(estudiantes):
        eliminado = estudiantes.pop(indice)
        print(f" Estudiante {eliminado['nombre']} eliminado.")
    else:
        print("⚠ Índice inválido.")

# --- Menú interactivo ---
def menu():
    while True:
        print("\n=== MENÚ CRUD ESTUDIANTES ===")
        print("1. Crear estudiante")
        print("2. Leer estudiantes")
        print("3. Actualizar estudiante")
        print("4. Eliminar estudiante")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese nombre: ")
            edad = int(input("Ingrese edad: "))
            crear_estudiante(nombre, edad)
        elif opcion == "2":
            leer_estudiantes()
        elif opcion == "3":
            leer_estudiantes()
            indice = int(input("Ingrese número de estudiante a actualizar: ")) - 1
            nuevo_nombre = input("Nuevo nombre (deje vacío si no cambia): ")
            nueva_edad = input("Nueva edad (deje vacío si no cambia): ")
            nueva_edad = int(nueva_edad) if nueva_edad else None
            actualizar_estudiante(indice, nuevo_nombre or None, nueva_edad)
        elif opcion == "4":
            leer_estudiantes()
            indice = int(input("Ingrese número de estudiante a eliminar: ")) - 1
            eliminar_estudiante(indice)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("⚠ Opción no válida.")

menu()