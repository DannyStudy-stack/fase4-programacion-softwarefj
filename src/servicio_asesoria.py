from servicio import Servicio

class ServicioAsesoria(Servicio):
    def __init__(self, nombre_servicio, precio_base, especialidad):
        super().__init__(nombre_servicio, precio_base)
        self.especialidad = especialidad

    def calcular_costo(self, horas, nivel_urgencia="Normal"):
        # Polimorfismo: El costo varía según la complejidad de la asesoría [cite: 24]
        multiplicador = 1.5 if nivel_urgencia == "Alta" else 1.0
        return (self._precio_base * horas) * multiplicador

    def obtener_descripcion(self):
        return f"Asesoría en {self.especialidad} por profesionales de Software FJ."