"""
Módulo de excepciones personalizadas para el Sistema Integral de Gestión.
Define las excepciones específicas que pueden ocurrir durante la ejecución del programa.
"""

class SistemaError(Exception):
    """
    Excepción base para todos los errores del sistema.
    De esta clase heredarán las demás excepciones personalizadas.
    """
    pass

class DatoInvalidoError(SistemaError):
    """
    Excepción lanzada cuando se introduce un dato incorrecto o que no cumple las validaciones.
    Ejemplo: Un correo sin el formato correcto o un documento con letras.
    """
    pass

class ServicioNoDisponibleError(SistemaError):
    """
    Excepción lanzada cuando se intenta reservar un servicio que no está disponible.
    Ejemplo: Una sala de reuniones que ya está ocupada en el horario solicitado.
    """
    pass

class ReservaInvalidaError(SistemaError):
    """
    Excepción lanzada cuando hay un problema lógico en la creación o modificación de una reserva.
    Ejemplo: Intentar cancelar una reserva que ya fue completada o que no existe.
    """
    pass

class OperacionNoPermitidaError(SistemaError):
    """
    Excepción lanzada cuando se intenta realizar una acción prohibida por las reglas de negocio.
    Ejemplo: Un cliente inactivo intentando hacer una reserva.
    """
    pass

class CalculoCostoError(SistemaError):
    """
    Excepción lanzada cuando ocurre un error al calcular el costo total de un servicio o reserva.
    Ejemplo: Duración negativa o tarifas inconsistentes.
    """
    pass

class ParametroFaltanteError(SistemaError):
    """
    Excepción lanzada cuando falta un dato obligatorio para realizar una operación.
    Ejemplo: Crear un cliente sin documento o una reserva sin duración.
    """
    pass
