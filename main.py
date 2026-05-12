"""
Archivo principal del Sistema Integral de Gestión de Clientes, Servicios y Reservas.
Desde aquí se ejecutará el sistema y, más adelante, tendrá la simulación de operaciones.
"""
from src.logger_config import obtener_logger
from src.excepciones import DatoInvalidoError

# Inicializamos el logger
logger = obtener_logger("main")

def main():
    # Mensaje de inicio del sistema
    logger.info("Iniciando el Sistema Integral de Gestión - Software FJ...")
    print("---------------------------------------------------------")
    print(" ¡Bienvenido al Sistema Software FJ! ")
    print("---------------------------------------------------------")

    # Prueba sencilla de captura de excepción personalizada
    try:
        logger.info("Realizando prueba de validación de datos...")
        # Simulamos que alguien intentó crear una entidad con datos vacíos
        raise DatoInvalidoError("El nombre de la entidad no puede estar vacío.")
        
    except DatoInvalidoError as e:
        # Se captura el error esperado y se guarda en el log
        logger.error(f"Error de validación capturado correctamente: {e}")

    logger.info("Fin de la prueba inicial. El sistema se cerrará.")

if __name__ == "__main__":
    main()
