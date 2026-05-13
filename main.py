"""
Archivo principal del Sistema Integral de Gestión.
Simulación completa del sistema Software FJ: Clientes, Servicios y Reservas.
"""
from src.logger_config import obtener_logger
from src.excepciones import (
    SistemaError, DatoInvalidoError, ReservaInvalidaError, ParametroFaltanteError
)
from src.cliente import Cliente
from src.servicio_sala import ServicioSala
from src.servicio_equipo import ServicioEquipo
from src.servicio_asesoria import ServicioAsesoria
from src.reserva import Reserva

logger = obtener_logger("main")

def imprimir_separador(titulo):
    print(f"\n{'=' * 60}")
    print(f" {titulo} ".center(60, '='))
    print(f"{'=' * 60}")

def ejecutar_prueba(descripcion, funcion, *args, **kwargs):
    print(f"\n[ Prueba ] {descripcion}")
    try:
        resultado = funcion(*args, **kwargs)
    except SistemaError as e:
        logger.error(f"Fallo esperado en prueba '{descripcion}': {e}")
        print(f"[ERROR ESPERADO] {e}")
    except Exception as e:
        logger.critical(f"Fallo INESPERADO en prueba '{descripcion}': {e}")
        print(f"[ERROR CRITICO] {e}")
    else:
        logger.info(f"Éxito en prueba '{descripcion}'")
        print(f"[EXITO] Operación completada correctamente.")
        return resultado
    finally:
        print("-> Fin del bloque de prueba.")
    return None

def main():
    # 1. Iniciar el sistema y registrar el evento en logs
    logger.info("Iniciando simulación completa del sistema Software FJ...")
    imprimir_separador("INICIO DE SIMULACIÓN SOFTWARE FJ")

    # --- PRUEBAS DE CLIENTES ---
    imprimir_separador("1. GESTIÓN DE CLIENTES")

    # 2. Crear un cliente válido
    cliente_valido = ejecutar_prueba(
        "Crear un cliente válido",
        lambda: Cliente("C001", "Daniel Perez", "10203040", "daniel@correo.com", "3001234567")
    )
    if cliente_valido:
        print(f"  Detalle: {cliente_valido.mostrar_informacion()}")

    # 3. Intentar crear un cliente con nombre vacío
    ejecutar_prueba(
        "Fallo por nombre vacío",
        lambda: Cliente("C002", "", "10203040", "daniel@correo.com", "3001234567")
    )

    # 4. Intentar crear un cliente con documento inválido
    ejecutar_prueba(
        "Fallo por documento inválido (muy corto)",
        lambda: Cliente("C003", "Maria Gomez", "123", "maria@correo.com", "3001234567")
    )

    # 5. Intentar crear un cliente con correo inválido
    ejecutar_prueba(
        "Fallo por correo inválido",
        lambda: Cliente("C004", "Luis Torres", "98765432", "luis.torres.com", "3001234567")
    )

    # --- PRUEBAS DE SERVICIOS ---
    imprimir_separador("2. GESTIÓN DE SERVICIOS")

    # 6. Crear un servicio de reserva de sala válido
    sala_valida = ejecutar_prueba(
        "Crear servicio de Sala válido",
        lambda: ServicioSala("S01", "Sala de Juntas VIP", 50000, 10)
    )
    if sala_valida:
        sala_valida.mostrar_informacion()

    # 7. Intentar crear un servicio de sala con capacidad inválida
    ejecutar_prueba(
        "Fallo por capacidad inválida (negativa)",
        lambda: ServicioSala("S02", "Sala Pequeña", 20000, -5)
    )

    # 8. Crear un servicio de alquiler de equipo válido
    equipo_valido = ejecutar_prueba(
        "Crear servicio de Equipo válido",
        lambda: ServicioEquipo("EQ01", "Proyector Audiovisual", 15000, "Audiovisual")
    )
    if equipo_valido:
        equipo_valido.mostrar_informacion()

    # 9. Intentar crear un servicio de equipo con datos inválidos
    ejecutar_prueba(
        "Fallo por tipo de equipo vacío",
        lambda: ServicioEquipo("EQ02", "Portátil", 30000, "")
    )

    # 10. Crear un servicio de asesoría válido
    asesoria_valida = ejecutar_prueba(
        "Crear servicio de Asesoría válido",
        lambda: ServicioAsesoria("A01", "Consultoría TI", 100000, "Arquitectura de Software")
    )
    if asesoria_valida:
        asesoria_valida.mostrar_informacion()

    # 11. Intentar crear una asesoría con datos inválidos
    ejecutar_prueba(
        "Fallo por especialidad vacía",
        lambda: ServicioAsesoria("A02", "Soporte", 50000, "")
    )

    # --- PRUEBAS DE RESERVAS ---
    imprimir_separador("3. GESTIÓN DE RESERVAS")

    # 12. Crear una reserva exitosa
    print("\n[ Prueba ] Crear una reserva válida")
    reserva_valida = None
    if cliente_valido and sala_valida:
        reserva_valida = Reserva(cliente_valido, sala_valida, 4)
        print(f"[EXITO] Reserva creada en estado: {reserva_valida.estado}")
    
    if reserva_valida:
        # 13. Confirmar una reserva
        print("\n[ Prueba ] Confirmar la reserva")
        reserva_valida.confirmar()
        print(f"[EXITO] Estado actual: {reserva_valida.estado}")

        # 14. Procesar una reserva y calcular el costo
        print("\n[ Prueba ] Procesar la reserva (Cálculo de costo)")
        reserva_valida.procesar_reserva()
        print(f"[EXITO] Costo total calculado: ${reserva_valida.costo_total}")

        # 15. Cancelar una reserva
        print("\n[ Prueba ] Cancelar la reserva")
        reserva_valida.cancelar()
        print(f"[EXITO] Estado tras cancelación: {reserva_valida.estado}")

        # 16. Intentar cancelar una reserva ya cancelada
        print("\n[ Prueba ] Intentar cancelar una reserva ya cancelada")
        reserva_valida.cancelar()
        print(f"[INFO] La reserva sigue en estado: {reserva_valida.estado}")

    # 17. Intentar procesar una reserva con duración inválida
    print("\n[ Prueba ] Procesar reserva con duración inválida")
    if cliente_valido and equipo_valido:
        reserva_invalida = Reserva(cliente_valido, equipo_valido, -2)
        reserva_invalida.procesar_reserva()
        print(f"[RESULTADO ESPERADO] La reserva quedó en estado: {reserva_invalida.estado}")

    imprimir_separador("FIN DE SIMULACIÓN")
    logger.info("Simulación completa finalizada correctamente.")
    print("Todas las pruebas concluidas. Revisa logs/sistema.log para más detalles.\n")

if __name__ == "__main__":
    main()
