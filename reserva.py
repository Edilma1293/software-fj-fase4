from excepciones import ReservaError

class Reserva:

    def __init__(self, cliente, servicio, horas):
        if horas <= 0:
            raise ReservaError("Las horas deben ser mayores que cero")

        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar(self):
        return self.servicio.calcular_costo(self.horas)
