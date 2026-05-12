from logger_config import registrar_error 

class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente # Composición: Integra objeto Cliente [cite: 25]
        self.servicio = servicio # Composición: Integra objeto Servicio [cite: 25]
        self.duracion = duracion
        self.estado = "Pendiente"
        self.costo_total = 0

    def procesar_reserva(self):
        try: # Inicio de bloque para manejo avanzado de excepciones [cite: 17]
            if self.duracion <= 0:
                # Validación estricta: No se permiten duraciones negativas [cite: 19]
                raise ValueError("La duración debe ser mayor a cero.")
            
            # Aplicación de polimorfismo al llamar calcular_costo según el tipo de servicio
            self.costo_total = self.servicio.calcular_costo(self.duracion)
            self.estado = "Confirmada"

        except ValueError as e: # Captura de errores de datos inválidos [cite: 19]
            self.estado = "Fallida"
            registrar_error(f"Error de validación: {str(e)}") # Registro en log externo [cite: 18, 31]
            raise 
            
        except Exception as e: # Captura de errores inesperados para evitar que el sistema se detenga 
            self.estado = "Error de Sistema"
            registrar_error(f"Falla crítica: {str(e)}")
            
        finally: # Garantiza que se informe el estado final sin importar el error [cite: 17]
            print(f"Auditoría: Reserva de {self.servicio.nombre} finalizada con estado: {self.estado}")