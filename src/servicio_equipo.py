from src.servicio import Servicio

class ServicioEquipo(Servicio):
    def __init__(self, id_entidad, nombre_servicio, precio_base, tipo_equipo):
        super().__init__(id_entidad, nombre_servicio, precio_base)
        self.tipo_equipo = tipo_equipo

    # Sobrecarga lógica mediante parámetros opcionales
    def calcular_costo(self, dias, seguro=True):
        costo = self._precio_base * dias
        if seguro:
            costo += (costo * 0.12) # 12% por cobertura de daños
        return costo

    def obtener_descripcion(self):
        return f"Equipo: {self._nombre_servicio} ({self.tipo_equipo})"