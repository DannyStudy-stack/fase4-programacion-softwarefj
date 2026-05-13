from src.logger_config import obtener_logger
from src.excepciones import ReservaInvalidaError, ParametroFaltanteError

logger = obtener_logger() # Ajustado a obtener_logger() 

class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"
        self.costo_total = 0

    def procesar_reserva(self):
        try:
            if not self.cliente or not self.servicio:
                raise ParametroFaltanteError("Cliente o Servicio no definidos.")
            
            # El cálculo ya incluye validar_parametros internamente
            self.costo_total = self.servicio.calcular_costo(self.duracion)
            self.estado = "Confirmada"
            logger.info(f"Reserva exitosa: {self.servicio.nombre} para {self.cliente.nombre}")

        except (ReservaInvalidaError, ParametroFaltanteError) as e:
            self.estado = "Fallida"
            logger.error(f"Error en validación: {str(e)}")
            
        except Exception as e:
            self.estado = "Error_Sistema"
            logger.critical(f"Falla crítica: {str(e)}")
            
        finally:
            print(f"Trámite finalizado. Resultado: {self.estado}")

    def cancelar(self):
        self.estado = "Cancelada"
        logger.info(f"Reserva cancelada para el cliente {self.cliente.id_entidad}")