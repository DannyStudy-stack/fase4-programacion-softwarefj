from servicio import Servicio

class ServicioSala(Servicio): # Herencia de la clase abstracta Servicio [cite: 24]
    def __init__(self, nombre_servicio, precio_base, capacidad):
        super().__init__(nombre_servicio, precio_base)
        self.capacidad = capacidad

    def calcular_costo(self, horas):
        # Polimorfismo: Cálculo específico por tiempo de uso de sala [cite: 24]
        return self._precio_base * horas

    def obtener_descripcion(self):
        return f"Reserva de sala: {self._nombre_servicio} para {self.capacidad} personas."