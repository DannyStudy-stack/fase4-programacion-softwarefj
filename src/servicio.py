from abc import ABC, abstractmethod
from src.entidad import Entidad # Importación relativa para evitar fallos en el paquete

# Abstracción: Servicio hereda de Entidad 
class Servicio(Entidad, ABC):
    def __init__(self, id_entidad, nombre_servicio, precio_base):
        # Inicializa el ID en la clase padre Entidad 
        super().__init__(id_entidad)
        self._nombre_servicio = nombre_servicio # Encapsulamiento (protegido)
        self._precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, **kwargs):
        """Método abstracto para implementar polimorfismo"""
        pass

    @abstractmethod
    def obtener_descripcion(self):
        """Ficha técnica obligatoria para cada servicio"""
        pass

    @property
    def nombre(self):
        return self._nombre_servicio