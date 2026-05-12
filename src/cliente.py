from src.entidad import Entidad
from src.excepciones import DatoInvalidoError

class Cliente(Entidad):
    """
    Representa a un cliente del sistema.
    Hereda de Entidad para tener id y nombre por defecto.
    """
    def __init__(self, id_entidad, nombre, documento, correo, telefono):
        # Inicializamos lo básico que nos pide la clase padre
        super().__init__(id_entidad, nombre)
        
        # Revisamos que el documento sea puro número
        if not documento or not str(documento).isdigit():
            raise DatoInvalidoError("El documento no puede estar vacío y debe contener solo números.")
        self._documento = str(documento)
        
        # Un chequeo rapidito para ver si el correo tiene cara de correo real
        if not correo or "@" not in correo or "." not in correo:
            raise DatoInvalidoError("El correo electrónico ingresado no tiene un formato válido.")
        self._correo = correo
        
        # El teléfono también tiene que ser numérico
        if not telefono or not str(telefono).isdigit():
            raise DatoInvalidoError("El teléfono no puede estar vacío y debe contener solo números.")
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
    def activar(self):
        """Vuelve a activar al cliente."""
        self._activo = True

    def desactivar(self):
        """Pone al cliente como inactivo."""
        self._activo = False

    # Armamos un string bonito para mostrar todos los datos de una vez
    def mostrar_informacion(self):
        estado = "Activo" if self._activo else "Inactivo"
        return (f"Cliente [ID: {self.id_entidad}] | Nombre: {self.nombre} | "
                f"Doc: {self.documento} | Correo: {self.correo} | "
                f"Tel: {self.telefono} | Estado: {estado}")
