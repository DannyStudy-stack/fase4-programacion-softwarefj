from servicio import Servicio

class ServicioEquipo(Servicio):
    def __init__(self, nombre_servicio, precio_base, tipo_equipo):
        super().__init__(nombre_servicio, precio_base)
        self.tipo_equipo = tipo_equipo

    def calcular_costo(self, dias, seguro=True):
        # Sobrecarga lógica: Manejo de parámetros opcionales (Seguro) [cite: 12, 26]
        costo = self._precio_base * dias
        if seguro:
            costo += (costo * 0.10) # 10% adicional por protección de equipos
        return costo

    def obtener_descripcion(self):
        return f"Alquiler de equipo: {self._nombre_servicio} ({self.tipo_equipo})."