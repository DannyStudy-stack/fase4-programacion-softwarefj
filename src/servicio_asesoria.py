from src.servicio import Servicio
from src.excepciones import ReservaInvalidaError

class ServicioAsesoria(Servicio):
    def __init__(self, id_entidad, nombre, precio_base, especialidad):
        if not especialidad:
            raise ReservaInvalidaError("La especialidad de la asesoría no puede estar vacía.")
        super().__init__(id_entidad, nombre, precio_base)
        self.especialidad = especialidad

    def validar_parametros(self, horas):
        if horas <= 0:
            raise ReservaInvalidaError("La asesoría debe durar al menos 1 hora.")

    def calcular_costo(self, horas, nivel="Estandar"):
        self.validar_parametros(horas)
        multiplicador = 1.5 if nivel == "Senior" else 1.0
        return (self._precio_base * horas) * multiplicador

    def describir_servicio(self):
        return f"Asesoría técnica en {self.especialidad}."

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Detalle: {self.describir_servicio()}")