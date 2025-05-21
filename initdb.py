import sqlite3
import logging
import random
from datetime import datetime, timedelta
import os

from sample_data import pacientes, especialidades, historias_medicas



# Configuración del logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(message)s',
    datefmt='%H:%M:%S'
)


def init_db():
    """
    Inicializa la base de datos y crea la tabla de muestras si no existe.
    """

    try:
        conn = sqlite3.connect("medical_records.db")
        logging.info("Validando conexión con la base de datos")

        # Crear un objeto cursor para ejecutar comandos SQL
        cursor = conn.cursor()

        # Crear la tabla pacientes si no existe
        """
        Aunque utilizamos un identificador de tipo entero auto-incrementado como clave primaria, 
        se realiza para conseguir una tabla más normalizada y rápida de consultar.
        el dni es único y no se repite, por lo que se podria tambien usar como clave primaria,
        pero su longitud es más larga, por lo que llegado el caso el rendimiento seria peor.
        
        El campo fecha_nacimiento es de tipo DATE, lo que permite almacenar fechas en un formato estándar.
        En este caso, se ha optado por almacenar la fecha de nacimiento como una cadena de texto en formato 'YYYY-MM-DD'.
        """
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pacientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                dni TEXT NOT NULL UNIQUE,
                nombre TEXT NOT NULL,
                apellidos TEXT NOT NULL,
                fecha_nacimiento DATE NOT NULL,
                email TEXT,
                telefono TEXT NOT NULL,
                direccion TEXT NOT NULL
            )
        """)

        # Crear la tabla de historias medicas si no existe
        """
        De nuevo utilizamos un identificador de tipo entero auto-incrementado como clave primaria.
        Utilizamos el Identificador del paciente como clave foránea para relacionar las historias médicas con los pacientes.
        
        Si el registro del paciente se elimina, se eliminarán automáticamente todas las historias médicas asociadas a él.
        Esto se logra mediante la cláusula ON DELETE CASCADE en la definición de la clave foránea.

        El campo estado es de tipo BOOLEAN, lo que permite almacenar valores verdaderos o falsos. 
        El valor 0 representa falso o historia cerrada y el valor 1 representa verdadero o historia abierta.

        El campo fecha_Apertura hace referencia a la fecha en la que se abrió la historia médica,tratándose de un campo de tipo DATE.
        El campo fecha_cierre es opcional y se utiliza para almacenar la fecha en la que se cerró la historia médica y que debe 
        correlarse con el campo estado, en este caso con el valor 0.
        """
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS historias_medicas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                paciente_id INTEGER NOT NULL,
                especialidad TEXT NOT NULL,
                estado BOOLEAN NOT NULL DEFAULT 1,
                fecha_apertura DATE NOT NULL,
                fecha_cierre DATE,
                descripcion TEXT NOT NULL,
                FOREIGN KEY (paciente_id) REFERENCES pacientes(id) ON DELETE CASCADE
            )
        """)
        conn.commit()
    except sqlite3.Error as e:
        logging.error(f"Error al inicializar la base de datos: {e}")
    finally:
        # Cerrar la conexión a la base de datos
        if conn:
            # Cerrar el cursor
            cursor.close()
            # Cerrar la conexión    
            conn.close()
            logging.info("Base de datos inicializada correctamente")

# Función para generar una fecha aleatoria
def random_date(start, end):
    return start + timedelta(days=random.randint(0, int((end - start).days)))

def load_data():
    """
    Carga de datos de ejemplo en la base de datos.
    """
    # Conectar a la base de datos SQLite
    conn = sqlite3.connect("medical_records.db")

    # Obtener un cursor para ejecutar comandos SQL
    cursor = conn.cursor()

    # Insertar datos de pacientes en la tabla
    # Utilizo el comando executemany para insertar múltiples filas a la vez
    # Esto es más eficiente que ejecutar un INSERT por cada fila
    cursor.executemany("""
        INSERT OR IGNORE INTO pacientes (dni, nombre, apellidos, fecha_nacimiento, email, telefono, direccion)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, pacientes)

    # Commit de la transacción
    cursor.execute("COMMIT")
    
    # Fechas de inicio y fin para generar fechas aleatorias
    start_date = datetime.strptime('2020-01-01', '%Y-%m-%d')
    end_date = datetime.strptime('2025-05-01', '%Y-%m-%d')


    for paciente in pacientes:
        dni = paciente[0]
        cursor.execute(""" SELECT id FROM pacientes WHERE dni = ? """, (dni,))
        paciente_id = cursor.fetchone()[0]
        
        # Generar un numero aleatorio de historias médicas para cada paciente
        num_historias = random.randint(1, 5)
        # Lista_especialidades es una lista para almacenar las especialidades que ya se han asignado a un paciente y evitar repeticiones de historias médicas
        # asociadas a la misma especialidad
        lista_especialidades = []

        # Generar historias médicas para cada paciente
        for _ in range(num_historias):
            
            # Obtener una especialidad aleatoria de la lista de especialidades asegurando que la especialidad no se repita  
            especialidad = random.choice(especialidades)
            # Si la especialidad ya está en la lista, elegir otra
            while especialidad in lista_especialidades:
                especialidad = random.choice(especialidades)
            # Agregar la especialidad a la lista           
            lista_especialidades.append(especialidad)

            # Obtener una historia médica aleatoria de la lista de historias médicas
            historia_medica = random.choice(historias_medicas[especialidad])

            # Generar una fecha aleatoria para la apertura de la historia médica
            fecha_apertura = random_date(start_date, end_date).strftime('%Y-%m-%d')
            
            # Generar un valor aletarorio 0, 1 para el estado de la historia médica
            estado = random.randint(0, 1)

            # Si el estado es 0 (historia cerrada), generar una fecha de cierre aleatoria
            if estado == 0:
                fecha_cierre = random_date(datetime.strptime(fecha_apertura, '%Y-%m-%d'), end_date).strftime('%Y-%m-%d')
            else:
                fecha_cierre = None


            # Insertar la historia médica en la tabla
            cursor.execute("""
                INSERT INTO historias_medicas (paciente_id, especialidad, estado, fecha_apertura, fecha_cierre, descripcion)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (paciente_id, especialidad, estado, fecha_apertura, fecha_cierre, historia_medica))   
        
        # Hacemos un commit de todas las inserciones de historias médicas
        cursor.execute("COMMIT")
    # Cerrar la conexión a la base de datos
    cursor.close()
    conn.close()

if __name__ == "__main__":
    # Si la BBDD existe, preguntamos is se quiere eliminar y volver a crear
    if os.path.exists("medical_records.db"):
        respuesta = input("La base de datos ya existe. ¿Desea eliminarla y volver a crearla? (s/n): ")
        if respuesta.lower() == 's':
            try:
                # Eliminar la base de datos existente
                os.remove("medical_records.db")
                logging.info("Base de datos eliminada. Creando una nueva con datos de ejemplo...")
            except OSError as e:
                logging.error(f"Error al eliminar la base de datos: {e}")
                exit()
            init_db()
            load_data()
            logging.info("Datos de ejemplo cargados correctamente")
        else:
            logging.info("No se eliminará la base de datos existente. Saliendo...")
            exit()
   
