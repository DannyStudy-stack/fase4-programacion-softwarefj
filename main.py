"""
Archivo principal del Sistema Integral de Gestión.
Desde aquí arrancamos todo el sistema y hacemos las pruebas.
"""
from src.logger_config import obtener_logger
from src.excepciones import DatoInvalidoError
from src.cliente import Cliente

# Preparamos el logger para ir guardando lo que pasa
logger = obtener_logger("main")

def main():
    logger.info("Arrancando el sistema...")
    print("---------------------------------------------------------")
    print(" ¡Bienvenido al Sistema Software FJ! ")
    print("---------------------------------------------------------")

    # Vamos a probar creando un cliente que sí tiene todos sus datos bien
    print("\n[ Prueba: Crear un cliente con todo en orden ]")
    try:
        cliente1 = Cliente(
            id_entidad="C001",
            nombre="Juan Pérez",
            documento="123456789",
            correo="juan.perez@email.com",
            telefono="3001234567"
        )
        logger.info(f"Se creó bien el cliente: {cliente1.nombre}")
        print("Todo OK ->", cliente1.mostrar_informacion())
    except DatoInvalidoError as e:
        logger.error(f"Se reventó algo creando el cliente bueno: {e}")

    # Ahora intentamos crear uno con datos malos a ver si falla como debería
    print("\n[ Prueba: Crear un cliente pasándole letras en el documento ]")
    try:
        logger.info("Tratando de meter un cliente con datos chuecos...")
        cliente_invalido = Cliente(
            id_entidad="C002",
            nombre="Maria Gomez",
            documento="123ABC",  # Acá es donde tiene que saltar el error
            correo="maria@email.com",
            telefono="3109876543"
        )
    except DatoInvalidoError as e:
        # Atrapamos el error para que el programa no se muera y lo anotamos en el log
        logger.error(f"Lo agarramos justo a tiempo: {e}")
        print(f"Error atajado correctamente -> {e}")

    print("\n---------------------------------------------------------")
    logger.info("Terminamos las pruebas, apagando todo.")

if __name__ == "__main__":
    main()
