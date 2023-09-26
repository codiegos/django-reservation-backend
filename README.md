# API REST de Agendamiento de Cabañas

Esta API REST se ha desarrollado utilizando Django y Django Rest Framework (DRF) para administrar y gestionar el agendamiento de cabañas. Utiliza el paquete Simple JWT para la autenticación basada en tokens JWT y Python-dotenv para la gestión de variables de entorno.

## Tecnologías Utilizadas

- **django:** Framework de desarrollo web de alto nivel y de código abierto.
- **djangorestframework (DRF):** Biblioteca para crear API REST en Django de manera sencilla y eficiente.
- **simple-jwt:** Paquete que proporciona autenticación basada en tokens JWT (JSON Web Tokens).
- **python-dotenv:** Herramienta para cargar variables de entorno desde un archivo `.env`.

## Requisitos de Instalación

- Python 3.x
- Pip (administrador de paquetes de Python)

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/codiegos/django-reservation-backend.git
   cd django-reservation-backend


2. Crea un entorno virtual (se recomienda):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate

4. Instala las dependencias:

   ```bash
    pip install -r requirements.txt
    Copia el archivo .env.example como .env y configura las variables de entorno necesarias.

5. Ejecuta las migraciones de la base de datos:

   ```bash
    python manage.py migrate

7. Crea un superusuario para acceder al panel de administración:

   ```bash
    python manage.py createsuperuser

8. Inicia el servidor de desarrollo:

   ```bash
    python manage.py runserver

La API estará disponible en http://localhost:8000/.

## Uso

Para obtener acceso a los endpoints de la API, debes autenticarte utilizando JWT. Puedes hacerlo obteniendo un token JWT válido mediante la ruta de autenticación.

Obtener Token JWT (Inicio de Sesión):

Envía una solicitud POST a la ruta api/token/ con las credenciales del superusuario que creaste durante la instalación. Deberías recibir un token JWT válido.

Ejemplo de solicitud:

    bash
    curl -X POST -d "username=tusuperusuario&password=tucontraseña" http://localhost:8000/api/token/
    Endpoints Principales:

Una vez que tengas un token JWT, puedes usarlo para autenticarte y acceder a los siguientes endpoints:

### /api/cabins/:
### /api/reservations/:
### /api/customers/:
### /api/settings/:
### /api/prepaids/:
### /api/users/:

Asegúrate de incluir el token JWT en la cabecera de tus solicitudes HTTP como Authorization: Bearer <tu-token-jwt>.


