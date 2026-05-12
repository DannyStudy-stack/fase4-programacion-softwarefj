"""
Archivo principal del Sistema Integral de Gestión.
Desde aquí arrancamos todo el sistema y hacemos las pruebas iniciales.
"""
from src.logger_config import obtener_logger
from src.excepciones import DatoInvalidoError
from src.cliente import Cliente

logger = obtener_logger("main")

def probar_creacion_cliente(id_entidad, nombre, documento, correo, telefono, descripcion):
    print(f"\n[ Prueba: {descripcion} ]")
    try:
        cliente = Cliente(
            id_entidad=id_entidad,
            nombre=nombre,
            documento=documento,
            correo=correo,
            telefono=telefono
        )
    except DatoInvalidoError as e:
        logger.error(f"Error esperado al crear cliente ({descripcion}): {e}")
        print(f"[ERROR] Capturado: {e}")
    else:
        logger.info(f"Cliente creado exitosamente: {cliente.nombre}")
        print(f"[EXITO] -> {cliente.mostrar_informacion()}")
    finally:
        print("-> Fin de este bloque de prueba.")

def main():
    logger.info("Iniciando pruebas base del sistema...")
    print("=========================================================")
    print("    Pruebas Iniciales - Sistema Software FJ (Clientes)   ")
    print("=========================================================")

    # 1. Cliente válido (demuestra try/except/else/finally en la función)
    probar_creacion_cliente(
        "C001", "Juan Perez", "12345678", "juan@correo.com", "3001234567",
        "Crear un cliente con todos los datos correctos"
    )

    # 2. Cliente inválido: nombre vacío
    probar_creacion_cliente(
        "C002", "", "98765432", "maria@correo.com", "3109876543",
        "Fallo por nombre vacío"
    )

    # 3. Cliente inválido: documento muy corto
    probar_creacion_cliente(
        "C003", "Carlos Lopez", "123", "carlos@correo.com", "3201234567",
        "Fallo por documento corto"
    )

    # 4. Cliente inválido: correo sin formato
    probar_creacion_cliente(
        "C004", "Ana Torres", "11223344", "ana.torres.com", "3001122334",
        "Fallo por formato de correo inválido"
    )

    # 5. Cliente inválido: teléfono con letras
    probar_creacion_cliente(
        "C005", "Luis Ruiz", "55667788", "luis@correo.com", "300A",
        "Fallo por teléfono con letras"
    )

    print("\n=========================================================")
    logger.info("Pruebas base finalizadas.")
    print("Todas las pruebas concluidas. Revisa logs/sistema.log para más detalles.")

if __name__ == "__main__":
    main()
