# Aplicación de Datos de Vacunación con Flask, Gunicorn, Nginx y Celery

## Descripción del Proyecto
Esta aplicación web proporciona acceso a datos históricos sobre la vacunación contra el sarampión en Panamá. Utiliza Flask como framework web, Gunicorn como servidor WSGI, Nginx como servidor web frontal, y Celery para tareas asíncronas como el envío de correos electrónicos.

## Características Principales
- **Interfaz Web**: Interactúa con los datos a través de una interfaz web intuitiva.
- **Consulta de Datos**: Visualiza y filtra los datos de vacunación por año.
- **Envío Asíncrono de Correos**: Envía correos electrónicos de manera asíncrona utilizando Celery y Flask-Mail.

## Tecnologías Utilizadas
- **Flask**: Framework web para construir la aplicación.
- **Jinja2**: Motor de plantillas para renderizar vistas HTML.
- **Gunicorn**: Servidor WSGI para manejar solicitudes HTTP.
- **Nginx**: Servidor web para servir contenido estático y actuar como proxy inverso.
- **Celery**: Manejo de tareas asíncronas.
- **Flask-Mail**: Gestión del envío de correos electrónicos.

## Estructura del Proyecto
yourapp/ ├── app/ │ ├── init.py # Configura e inicializa la aplicación Flask con Celery y Flask-Mail │ ├── celery.py # Configuración de Celery │ ├── services.py # Servicios para interactuar con la API REST │ ├── routes.py # Rutas de la aplicación │ ├── templates/ # Plantillas Jinja2 para la interfaz de usuario │ └── static/ # Archivos estáticos (CSS, JS) ├── config/ │ ├── nginx/ # Configuración de Nginx │ └── systemd/ # Configuración del servicio systemd para Gunicorn ├── tests/ # Pruebas unitarias ├── requirements.txt # Dependencias ├── .gitignore # Archivos excluidos de Git └── README.md # Documentación del proyecto


## Instalación y Configuración

### Requisitos Previos
- Python 3.8+
- Redis (para Celery)
- Nginx
- Gunicorn

### Pasos de Instalación
1. **Clonar el Repositorio**:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd yourapp
   
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

celery -A app.celery worker

gunicorn --bind 0.0.0.0:8000 app:app
