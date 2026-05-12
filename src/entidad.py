from abc import ABC, abstractmethod
from src.excepciones import DatoInvalidoError

class Entidad(ABC):
    """
    Clase abstracta base para las entidades del sistema (Cliente, Servicio, etc.).
    """
    
    def __init__(self, id_entidad, nombre):
        """
        Constructor base. Valida que los datos obligatorios no estén vacíos.
        """
        if not id_entidad:
            raise DatoInvalidoError("El ID de la entidad no puede estar vacío.")
        if not nombre:
            raise DatoInvalidoError("El nombre de la entidad no puede estar vacío.")
            
        # Atributos protegidos (encapsulación)
        self._id_entidad = id_entidad
        self._nombre = nombre

    # Property para obtener el ID (solo lectura, no tiene setter)
    @property
    def id_entidad(self):
        return self._id_entidad

    # Property para obtener el nombre
    @property
    def nombre(self):
        return self._nombre

    # Setter para modificar el nombre con validación
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if not nuevo_nombre:
            raise DatoInvalidoError("El nuevo nombre no puede estar vacío.")
        self._nombre = nuevo_nombre

    @abstractmethod
    def mostrar_informacion(self):
        """
        Método abstracto. Obliga a las clases hijas a implementar
        cómo se debe mostrar su información.
        """
        pass
