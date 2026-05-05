from abc import ABC, abstractmethod

class Servicio(ABC):

    def __init__(self, nombre, tarifa):
        self.nombre = nombre
        self.tarifa = tarifa

    @abstractmethod
    def calcular_costo(self, horas):
        pass


class ReservaSala(Servicio):

    def calcular_costo(self, horas):
        return self.tarifa * horas


class AlquilerEquipo(Servicio):

    def calcular_costo(self, horas):
        return (self.tarifa * horas) + 20


class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, horas):
        return (self.tarifa * horas) * 1.15
