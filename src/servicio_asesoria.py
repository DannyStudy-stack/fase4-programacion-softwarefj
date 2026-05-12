from src.servicio import Servicio

class ServicioAsesoria(Servicio):
    def __init__(self, id_entidad, nombre_servicio, precio_base, especialidad):
        super().__init__(id_entidad, nombre_servicio, precio_base)
        self.especialidad = especialidad

    def calcular_costo(self, horas, nivel="Senior"):
        # Polimorfismo: El costo varía según el perfil del asesor
        multiplicador = 1.8 if nivel == "Senior" else 1.0
        return (self._precio_base * horas) * multiplicador

    def obtener_descripcion(self):
        return f"Asesoría Especializada en {self.especialidad} (FJ-Software)"