from abc import ABC, abstractmethod

# Aplicación de Abstracción: No se pueden crear instancias de esta clase directamente [cite: 11, 21]
class Servicio(ABC):
    def __init__(self, nombre_servicio, precio_base):
        self._nombre_servicio = nombre_servicio  # Atributo protegido (Encapsulamiento) 
        self._precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, **kwargs):
        """Método abstracto: obliga a las subclases a definir su propia lógica de cobro [cite: 24]"""
        pass

    @abstractmethod
    def obtener_descripcion(self):
        """Método abstracto para garantizar que cada servicio tenga una ficha técnica [cite: 24]"""
        pass

    @property # Getter para acceder al nombre cumpliendo con la encapsulación 
    def nombre(self):
        return self._nombre_servicio