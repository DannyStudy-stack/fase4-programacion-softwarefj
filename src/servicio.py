from abc import ABC, abstractmethod
from src.entidad import Entidad

class Servicio(Entidad, ABC):
    def __init__(self, id_entidad, nombre, precio_base):
        if not nombre or precio_base <= 0:
            from src.excepciones import ReservaInvalidaError
            raise ReservaInvalidaError("El nombre no puede estar vacío y el precio debe ser mayor a cero.")
        
        super().__init__(id_entidad, nombre)
        self._precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, **kwargs):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    @abstractmethod
    def validar_parametros(self, **kwargs):
        pass

    def mostrar_informacion(self):
        print(f"ID: {self.id_entidad} | Servicio: {self.nombre} | Precio Base: {self._precio_base}")