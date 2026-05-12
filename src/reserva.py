from src.logger_config import registrar_error
from src.excepciones import ReservaInvalidaError, ParametroFaltanteError # Excepciones del doc 

class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente # Composición con objeto Cliente 
        self.servicio = servicio # Composición con objeto Servicio 
        self.duracion = duracion
        self.estado = "Pendiente"
        self.costo_total = 0

    def procesar_reserva(self):
        try: # Bloque try para capturar fallos 
            if not self.cliente or not self.servicio:
                raise ParametroFaltanteError("Faltan datos esenciales (Cliente/Servicio).") 
            
            if self.duracion <= 0:
                raise ReservaInvalidaError("La duración debe ser mayor a 0.") 
            
            # Cálculo dinámico (Polimorfismo)
            self.costo_total = self.servicio.calcular_costo(self.duracion)
            self.estado = "Confirmada"
            print(f"Reserva de {self.servicio.nombre} exitosa.")

        except (ReservaInvalidaError, ParametroFaltanteError) as e:
            self.estado = "Fallida"
            registrar_error(f"Error de Negocio: {str(e)}") # Registro en log 
            
        except Exception as e:
            self.estado = "Error_Critico"
            registrar_error(f"Falla inesperada en sistema: {str(e)}") 
            
        finally: # Garantiza que la aplicación siga activa aun tras errores 
            print(f"Finalizando trámite. Estado: {self.estado}")

    def cancelar(self):
        self.estado = "Cancelada"