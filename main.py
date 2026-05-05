from cliente import Cliente
from servicio import ReservaSala
from reserva import Reserva

def registrar_log(error):
    with open("logs.txt", "a") as archivo:
        archivo.write(str(error) + "\n")

try:
    cliente1 = Cliente("Edy", "12345")
    servicio1 = ReservaSala("Sala VIP", 50)

    reserva1 = Reserva(cliente1, servicio1, 3)
    reserva1.confirmar()

    print("Cliente:", cliente1)
    print("Estado:", reserva1.estado)
    print("Costo total:", reserva1.procesar())

except Exception as e:
    registrar_log(e)
    print("Error:", e)

try:
    cliente2 = Cliente("", "12")
except Exception as e:
    registrar_log(e)
    print("Error controlado:", e)
  
