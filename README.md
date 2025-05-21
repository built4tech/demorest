# API REST de Gestión de Pacientes y Especialidades Médicas

Este proyecto implementa una API REST minimalista utilizando Flask para la gestión de pacientes, especialidades médicas e historias clínicas. La aplicación está diseñada para ejecutarse en un entorno Docker ligero y expone sus servicios en el puerto 8080.
La aplicación utiliza una BBDD sqlite3 (medical_records.db) que ya se encuentra poblada con datos de ejemplo. Si se borrara esta BBDD se puede recrear utilizando el script initdb.py, que genera información random en las tablas que conforman el proyecto de acuerdo con la información contenida en sample_data.py.

## Estructura del Proyecto

```
v2/
├── apirest.py             # Código principal de la API Flask, incluyendo los endpoints y el servidor Web
├── sample_data.py         # Datos de ejemplo: especialidades, pacientes e historias médicas
├── requirements.txt       # Dependencias Python necesarias para la API
├── Dockerfile             # Instrucciones para construir la imagen Docker
├── initdb.py              # Script para inicializar la base de datos SQLite, importa el archivo sample_data.py para de un modo random poblar la BBDD con información de muestra.
├── medical_records.db     # Base de datos SQLite con los datos médicos y las historias médicas
├── index.html             # Página principal de la aplicación web
├── introducir_datos.htm   # Página que permite la selección de un paciente por su identificador.
├── about.html             # Página de información sobre la aplicación, indicando el desarrollador de la misma
├── especialidad.html      # Plantilla HTML para visualizar especialidades
├── README.md              # Documentación del proyecto
└── templates/
    └── especialidad.html  # Plantilla HTML para especialidades (Plantilla html que es renderizada por el servicio Web en función de la especialidad elegida)
```

## Descripción de los Archivos

- **apirest.py**: Implementa los endpoints de la API REST y la lógica de la aplicación.
- **sample_data.py**: Contiene los datos de ejemplo que utiliza la API (especialidades, pacientes e historias médicas).
- **initdb.py**: Script para crear e inicializar la base de datos SQLite (`medical_records.db`), importa el archivo sample_data.py para de un modo random poblar la BBDD con información de muestra..
- **medical_records.db**: Base de datos SQLite con la información médica persistente.
- **index.html**: Página principal de la aplicación web, sirve como punto de entrada para los usuarios.
- **about.html**: Página con información sobre el autor de la aplicación.
- **especialidad.html**: Plantilla HTML para la visualización de especialidades médicas.
- **introducir_datos.html**: Página que permite la selección de un paciente por su identificador.
- **requirements.txt**: Lista las dependencias necesarias (por ejemplo, Flask).
- **Dockerfile**: Define una imagen ligera basada en Alpine Linux con Python 3.11.9.
- **README.md**: Documentación del proyecto.
- **templates/especialidad.html**: Plantilla HTML alternativa para especialidades si se utiliza el sistema de plantillas de Flask.

## Objetivo

El objetivo de esta aplicación es proporcionar una API REST sencilla para consultar y gestionar información de pacientes, especialidades médicas e historias clínicas, utilizando datos de ejemplo precargados y una base de datos SQLite. Además, incluye páginas HTML para la visualización web de la información.

## Puesta en Marcha

1. **Construir la imagen Docker**:
   ```sh
   docker build -t api-pacientes .
   ```

2. **Ejecutar el contenedor Docker**:
   ```sh
   docker run -p 8080:8080 api-pacientes
   ```

3. **Acceso a la API**:
   Accede a los endpoints de la API en `http://localhost:8080` usando tu navegador, `curl` o Postman.

4. **Interfaz Web**:
   Puedes acceder a las páginas HTML (`index.html`, `about.html`, `especialidad.html`, `introducir_datos.html` ) desde el navegador para visualizar la información de la aplicación.

## Dependencias

Las dependencias necesarias están especificadas en `requirements.txt`. La imagen Docker las instalará automáticamente al construir el contenedor.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.