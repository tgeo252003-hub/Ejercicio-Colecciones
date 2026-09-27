# Ejercicio-colecciones
# --------------------------------------
# AGENDA DE CONTACTOS
# INGRESO, BUSQUEDA Y ELIMINACIÓN DE DATOS INGRESADOS.
# --------------------------------------

agenda = {}
def agregar_contacto(nombre, telefono):
    agenda[nombre] = telefono
    print(f"Contacto '{nombre}' agregado correctamente.\n")


def buscar_contacto(nombre):
    if nombre in agenda:
        print(f"{nombre}: {agenda[nombre]}.\n")
    else:
        print(f"El contacto '{nombre}' no existe en la agenda.\n")


def eliminar_contacto(nombre):
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto '{nombre}' eliminado.\n")
    else:
        print(f"No se encontró el contacto '{nombre}'.\n")


def mostrar_agenda():
    print("Lista de contactos:")

    if not agenda:
        print("La agenda está vacía.\n")
    else:
        for nombre, telefono in agenda.items():
            print(f"- {nombre}: {telefono}")
        print()

#-------------------------------------------------------------------

while True:
    print("\n--- Agregar contacto ---")
    nombre = input("Ingrese el nombre del contacto: ").strip()

    if nombre == "":
        print("Error: debe ingresar un nombre.")
        continue

    telefono = input("Ingrese el número de teléfono: ").strip()
    if not telefono.isdigit():
        print("Error: el número de teléfono debe contener solamente números.")   
        continue

    if len(telefono) != 10:
        print("Error: el número de teléfono debe tener 10 dígitos.")
        continue

    agregar_contacto(nombre, telefono)
    continuar = input("¿Desea agregar otro contacto? (s/n): ").lower()
    if continuar != "s":
        break

#-------------------------------------------------------------------

mostrar_agenda()

print("--- Búsqueda ---")
while True:
    nombre = input("Ingrese el nombre que desea buscar: ")
    if nombre == "":
        print("Error: debe ingresar un nombre.")
        continue
    if nombre in agenda:
        buscar_contacto(nombre)
        break
    else:
        print(f"El contacto '{nombre}' no existe en la agenda.")
        nuevamente = input("¿Desea intentar nuevamente? (s/n): ").lower()
        if nuevamente != "s":
            break

#------------------------------------------------------------------
        
print("\n--- Eliminación ---")
while True:
    nombre = input("Ingrese el nombre que desea eliminar: ")
    if nombre == "":
        print("Error: debe ingresar un nombre.")
        eliminar_contacto(nombre)
        break
    else:
        print(f"El contacto '{nombre}' no existe en la agenda.")
        nuevamente = input("¿Desea intentar nuevamente? (s/n): ").lower()
        if nuevamente != "s":
            break

mostrar_agenda()

