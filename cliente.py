from excepciones import ClienteError

class Cliente:
    def __init__(self, nombre, documento):
        if not nombre:
            raise ClienteError("El nombre no puede estar vacío")

        if len(str(documento)) < 5:
            raise ClienteError("Documento inválido")

        self.__nombre = nombre
        self.__documento = documento

    def get_nombre(self):
        return self.__nombre

    def get_documento(self):
        return self.__documento

    def __str__(self):
        return f"{self.__nombre} - {self.__documento}"
