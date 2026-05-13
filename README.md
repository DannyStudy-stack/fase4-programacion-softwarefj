# Fase 4 - Prácticas simuladas: Software FJ

## Descripción
Sistema Integral de Gestión desarrollado en Python. Este proyecto implementa los principios de la Programación Orientada a Objetos (POO) para simular la gestión de clientes, reservas y un catálogo de servicios polimórficos. Cabe destacar que el sistema opera enteramente en memoria durante la simulación y no utiliza ninguna base de datos externa.

## Objetivo
Crear una aplicación académica en Python que aplique herencia, encapsulamiento, polimorfismo y manejo avanzado de excepciones, cumpliendo con los lineamientos del curso para la Fase 4.

## Tecnologías
- Python 3.x
- Módulo estándar logging
- Módulo estándar abc (Abstract Base Classes)

## Estructura del Proyecto
```text
fase4-programacion-softwarefj/
│
├── src/                        # Código fuente (Paquete)
│   ├── cliente.py              # Clase Cliente (Hereda de Entidad)
│   ├── entidad.py              # Clase abstracta base
│   ├── excepciones.py          # Excepciones personalizadas
│   ├── logger_config.py        # Configuración del sistema de registros
│   ├── reserva.py              # Gestión de reservas
│   ├── servicio.py             # Clase abstracta Servicio (Hereda de Entidad)
│   ├── servicio_asesoria.py    # Servicio derivado (Asesoría)
│   ├── servicio_equipo.py      # Servicio derivado (Alquiler de equipos)
│   └── servicio_sala.py        # Servicio derivado (Reserva de salas)
│
├── logs/                       # Historial de ejecución
│   └── sistema.log             # Eventos y errores del sistema
│
├── main.py                     # Punto de entrada y simulación
└── README.md                   # Documentación principal
```

## Ejecución
Para ejecutar la simulación completa del sistema, abra su terminal en el directorio raíz del proyecto y utilice el siguiente comando:

```bash
python main.py
```

## Funcionalidades Principales
- Gestión de entidades: Validación estricta de formatos para nombres y documentos.
- Catálogo de servicios: Cálculo de costos dinámico mediante polimorfismo según el tipo de servicio seleccionado.
- Reservas: Flujo de creación, procesamiento y cancelación con actualización de estados.

## Manejo de Errores y Logs
El sistema implementa clases de excepciones diseñadas de manera específica para este modelo de negocio (por ejemplo, DatoInvalidoError y ReservaInvalidaError). 

Adicionalmente, se configuró un sistema de trazabilidad. Todos los eventos exitosos y los errores controlados que ocurren durante la ejecución quedan registrados de manera automática y detallada en el archivo `logs/sistema.log`.

## Integrantes
- [Nombre y Apellido] - [Código o Rol]
- [Nombre y Apellido] - [Código o Rol]
- [Nombre y Apellido] - [Código o Rol]

## Estado del Proyecto
Finalizado y listo para la entrega académica.
