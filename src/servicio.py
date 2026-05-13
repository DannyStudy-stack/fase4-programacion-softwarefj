from abc import ABC, abstractmethod
from src.entidad import Entidad

class Servicio(Entidad, ABC):
    def __init__(self, id_entidad, nombre, precio_base):
        # Entidad recibe id_entidad y nombre según el diseño del equipo
        super().__init__(id_entidad, nombre)
        self._precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, **kwargs):
        pass

    @abstractmethod
    def describir_servicio(self):
        """Nombre de método solicitado para la Fase 4"""
        pass

    @abstractmethod
    def validar_parametros(self, **kwargs):
        """Método para validaciones estrictas antes de operar"""
        pass

    # Exigencia de la clase Entidad
    def mostrar_informacion(self):
        print(f"ID: {self.id_entidad} | Servicio: {self.nombre} | Precio Base: {self._precio_base}")