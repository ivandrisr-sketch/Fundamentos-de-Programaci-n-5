# =====================================================
# FASE 5 - Evaluación Final POA
# Problema 1 - Evaluación de compromiso de clientes
# Autor: Ivan Salcedo
# =====================================================

# MATRIZ DE DATOS
# [ID Cliente, Duración(segundos), Clics]

sesiones = [
    ["CLI001", 250, 12],
    ["CLI002", 45, 2],
    ["CLI003", 120, 5],
    ["CLI004", 300, 15],
    ["CLI005", 80, 4]
]

# =====================================================
# FUNCIÓN PARA CLASIFICAR EL COMPROMISO
# =====================================================

def clasificar_compromiso(duracion, clics):

    if duracion > 180 and clics > 8:
        return "Alto"

    elif duracion < 60 or clics < 3:
        return "Bajo"

    else:
        return "Medio"


# =====================================================
# FUNCIÓN PARA MOSTRAR EL INFORME
# =====================================================

def mostrar_informe():

    print("\n====================================")
    print(" INFORME DE COMPROMISO DE CLIENTES ")
    print("====================================")

    # CICLO REPETITIVO
    for sesion in sesiones:

        id_cliente = sesion[0]
        duracion = sesion[1]
        clics = sesion[2]

        clasificacion = clasificar_compromiso(duracion, clics)

        print(f"\nCliente: {id_cliente}")
        print(f"Duración: {duracion} segundos")
        print(f"Clics: {clics}")
        print(f"Clasificación: {clasificacion}")

    print("====================================\n")


# =====================================================
# FUNCIÓN PARA AGREGAR NUEVA SESIÓN
# =====================================================

def agregar_sesion():

    print("\n====== AGREGAR NUEVA SESIÓN ======")

    id_cliente = input("Ingrese ID del cliente: ")
    duracion = int(input("Ingrese duración en segundos: "))
    clics = int(input("Ingrese cantidad de clics: "))

    sesiones.append([id_cliente, duracion, clics])

    print("Sesión agregada correctamente.\n")


# =====================================================
# MENÚ PRINCIPAL
# =====================================================

opcion = 0

# CICLO WHILE
while opcion != 3:

    print("====================================")
    print("      MENÚ PRINCIPAL")
    print("====================================")
    print("1. Mostrar informe")
    print("2. Agregar nueva sesión")
    print("3. Salir")
    print("====================================")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        mostrar_informe()

    elif opcion == 2:
        agregar_sesion()

    elif opcion == 3:
        print("\nPrograma finalizado correctamente.")

    else:
        print("\nOpción inválida.\n")


# Evita que la ventana se cierre sola
input("\nPresione ENTER para salir...")