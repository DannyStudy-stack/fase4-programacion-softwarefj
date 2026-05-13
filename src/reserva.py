from src.logger_config import obtener_logger
from src.excepciones import ReservaInvalidaError, ParametroFaltanteError

# Logger específico para el módulo de reserva
logger = obtener_logger("reserva")

class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"
        self.costo_total = 0

    def confirmar(self):
        """Cambia el estado a confirmado tras validaciones externas"""
        if self.estado == "Pendiente":
            self.estado = "Confirmada"
            logger.info(f"Reserva {self.servicio.nombre} confirmada manualmente.")

    def procesar_reserva(self):
        try:
            if not self.cliente or not self.servicio:
                raise ParametroFaltanteError("Cliente o Servicio no definidos.")
            
            self.costo_total = self.servicio.calcular_costo(self.duracion)
            self.estado = "Procesada"
            logger.info(f"Reserva procesada exitosamente para {self.cliente.nombre}")

        except (ReservaInvalidaError, ParametroFaltanteError) as e:
            self.estado = "Fallida"
            logger.error(f"Fallo en procesamiento: {str(e)}")
            
        except Exception as e:
            self.estado = "Error_Sistema"
            logger.critical(f"Error inesperado: {str(e)}")
            
        finally:
            print(f"Operación finalizada. Estado actual: {self.estado}")

    def cancelar(self):
        self.estado = "Cancelada"
        logger.info(f"Reserva cancelada para el ID Cliente: {self.cliente.id_entidad}")