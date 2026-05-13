from src.servicio import Servicio
from src.excepciones import ReservaInvalidaError

class ServicioSala(Servicio):
    def __init__(self, id_entidad, nombre, precio_base, capacidad):
        super().__init__(id_entidad, nombre, precio_base)
        self.capacidad = capacidad

    def validar_parametros(self, horas):
        if horas <= 0 or horas > 24:
            raise ReservaInvalidaError("Las horas de sala deben estar entre 1 y 24.")

    def calcular_costo(self, horas):
        self.validar_parametros(horas)
        return self._precio_base * horas

    def describir_servicio(self):
        return f"Reserva de Sala para {self.capacidad} personas."

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Detalle: {self.describir_servicio()}")