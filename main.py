from cliente import Cliente
from servicio import ReservaSala
from reserva import Reserva

def registrar_log(error):
    with open("logs.txt", "a") as archivo:
        archivo.write(str(error) + "\n")

print("=== SISTEMA SOFTWARE FJ ===")

# OPERACIÓN 1: RESERVA VALIDA
try:
    nombre = input("Ingrese nombre del cliente: ")
    documento = input("Ingrese documento del cliente: ")

    cliente1 = Cliente(nombre, documento)

    servicio1 = ReservaSala("Sala VIP", 50)

    dias = int(input("Ingrese días de reserva: "))

    reserva1 = Reserva(cliente1, servicio1, dias)
    reserva1.confirmar()

    print("\n--- RESERVA EXITOSA ---")
    print("Cliente:", cliente1)
    print("Estado:", reserva1.estado)
    print("Costo total:", reserva1.procesar())

except Exception as e:
    registrar_log(e)
    print("Error:", e)

# OPERACIÓN 2: ERROR CONTROLADO (CLIENTE INVÁLIDO)
try:
    cliente2 = Cliente("", "12")
except Exception as e:
    registrar_log(e)
    print("Error controlado:", e)
