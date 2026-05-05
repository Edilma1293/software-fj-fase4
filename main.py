from cliente import Cliente
from servicio import ReservaSala
from reserva import Reserva

def registrar_log(error):
    with open("logs.txt", "a") as archivo:
        archivo.write(str(error) + "\n")

print("=== SISTEMA SOFTWARE FJ ===")

operaciones = 0

while operaciones < 10:
    print("\n--- MENÚ ---")
    print("1. Crear reserva")
    print("2. Crear cliente inválido (prueba error)")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    # =========================
    # OPCIÓN 1: RESERVA NORMAL
    # =========================
    if opcion == "1":
        try:
            nombre = input("Igrese el nombre del cliente: ")
            documento = input("Igrese el Documento: ")
            dias = int(input("ingrese los días de reserva: "))

            cliente = Cliente(nombre, documento)
            servicio = ReservaSala("Sala VIP", 50)

            reserva = Reserva(cliente, servicio, dias)
            reserva.confirmar()

            print("\n✔ Reserva exitosa")
            print("Cliente:", cliente)
            print("Estado:", reserva.estado)
            print("Costo total:", reserva.procesar())

            operaciones += 1

        except Exception as e:
            registrar_log(e)
            print("✖ Error:", e)
            operaciones += 1

    # =========================
    # OPCIÓN 2: ERROR CONTROLADO
    # =========================
    elif opcion == "2":
        try:
            cliente = Cliente("", "12")  # error intencional
        except Exception as e:
            registrar_log(e)
            print("✖ Error controlado:", e)
            operaciones += 1

    # =========================
    # SALIR
    # =========================
    elif opcion == "3":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida")
