import logging
import os

def obtener_logger(nombre):
    """
    Configura y retorna un logger para registrar eventos y errores en el sistema.
    Crea la carpeta 'logs' automáticamente si no existe.
    """
    # 1. Crear carpeta logs si no existe
    if not os.path.exists("logs"):
        os.makedirs("logs")

    # 2. Obtener el logger con el nombre solicitado
    logger = logging.getLogger(nombre)
    logger.setLevel(logging.DEBUG)

    # 3. Evitar que se dupliquen los mensajes si ya está configurado
    if not logger.handlers:
        # Formato de los mensajes
        formato = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Configurar para guardar en archivo
        manejador_archivo = logging.FileHandler("logs/sistema.log", encoding="utf-8")
        manejador_archivo.setLevel(logging.DEBUG)
        manejador_archivo.setFormatter(formato)

        # Configurar para mostrar en consola (opcional, ayuda al desarrollo)
        manejador_consola = logging.StreamHandler()
        manejador_consola.setLevel(logging.INFO)
        manejador_consola.setFormatter(formato)

        # Agregar los manejadores al logger
        logger.addHandler(manejador_archivo)
        logger.addHandler(manejador_consola)

    return logger
