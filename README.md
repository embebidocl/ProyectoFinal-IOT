Proyecto Final - Matias Rivera Devia - Alexis Zamora Bernal

## Requisitos

Para ejecutar este proyecto correctamente se requiere:

- Python 3.11+.
- PostgreSQL como base de datos.
- Conectar el circuito presentado (Arduino+sensores) en el informe por puerto serial.
- Tener compilado y cargado el programa arduino para la captura de datos y posterior envío por serial (presentado en el informe).
- Contenedor Docker en un servidor Ubuntu para gestionar la base de datos.

El contenedor Docker debe estar configurado con una imagen de PostgreSQL y expuesto al puerto correspondiente. El sistema Django se conecta externamente a esa base de datos mediante variables de entorno o configuración directa en "settings.py".


