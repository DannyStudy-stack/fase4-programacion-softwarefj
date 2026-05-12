from src.servicio import Servicio

class ServicioSala(Servicio):
    def __init__(self, id_entidad, nombre_servicio, precio_base, capacidad):
        super().__init__(id_entidad, nombre_servicio, precio_base)
        self.capacidad = capacidad

    def calcular_costo(self, horas):
        # Polimorfismo: Cálculo basado en horas de uso 
        return self._precio_base * horas

    def obtener_descripcion(self):
        return f"Sala: {self._nombre_servicio} - Capacidad: {self.capacidad} personas"