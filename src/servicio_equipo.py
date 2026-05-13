from src.servicio import Servicio
from src.excepciones import ReservaInvalidaError

class ServicioEquipo(Servicio):
    def __init__(self, id_entidad, nombre, precio_base, tipo_equipo):
        if not tipo_equipo:
            raise ReservaInvalidaError("El tipo de equipo no puede estar vacío.")
        super().__init__(id_entidad, nombre, precio_base)
        self.tipo_equipo = tipo_equipo

    def validar_parametros(self, dias):
        if dias <= 0:
            raise ReservaInvalidaError("El alquiler de equipo requiere al menos 1 día.")

    def calcular_costo(self, dias, seguro=True):
        self.validar_parametros(dias)
        costo = self._precio_base * dias
        if seguro: costo *= 1.10
        return costo

    def describir_servicio(self):
        return f"Alquiler de equipo tipo: {self.tipo_equipo}."

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Detalle: {self.describir_servicio()}")