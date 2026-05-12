from src.entidad import Entidad
from src.excepciones import DatoInvalidoError
import re

class Cliente(Entidad):
    """
    Representa a un cliente del sistema.
    Hereda de Entidad para tener id y nombre por defecto.
    """
    def __init__(self, id_entidad, nombre, documento, correo, telefono):
        # Inicializamos lo básico que nos pide la clase padre
        super().__init__(id_entidad, nombre)
        
        # Revisamos que el documento sea puro número y tenga una longitud mínima razonable
        if not documento or not str(documento).isdigit() or len(str(documento)) < 5:
            raise DatoInvalidoError("El documento debe ser numérico y tener al menos 5 dígitos.")
        self._documento = str(documento)
        
        # Validación de correo con expresión regular sencilla
        if not correo or not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", str(correo)):
            raise DatoInvalidoError("El correo electrónico ingresado no tiene un formato válido.")
        self._correo = correo
        
        # El teléfono tiene que ser numérico y tener mínimo 7 dígitos
        if not telefono or not str(telefono).isdigit() or len(str(telefono)) < 7:
            raise DatoInvalidoError("El teléfono debe ser numérico y tener al menos 7 dígitos.")
        self._telefono = str(telefono)
        
        # Todo cliente nuevo arranca activo
        self._activo = True

    # Los getters para poder leer los datos protegidos sin cambiarlos desde afuera
    @property
    def documento(self):
        return self._documento

    @property
    def correo(self):
        return self._correo

    @property
    def telefono(self):
        return self._telefono

    @property
    def activo(self):
        return self._activo

    # Acciones simples para prender o apagar clientes
    def activar_cliente(self):
        """Vuelve a activar al cliente."""
        self._activo = True

    def desactivar_cliente(self):
        """Pone al cliente como inactivo."""
        self._activo = False

    # Armamos un string bonito para mostrar todos los datos de una vez
    def mostrar_informacion(self):
        estado = "Activo" if self._activo else "Inactivo"
        return (f"Cliente [ID: {self.id_entidad}] | Nombre: {self.nombre} | "
                f"Doc: {self.documento} | Correo: {self.correo} | "
                f"Tel: {self.telefono} | Estado: {estado}")
