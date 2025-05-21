from flask import Flask, request, jsonify, send_file, render_template
import sqlite3

import sys, logging

# Creamos la aplicación Flask
app = Flask(__name__)

# Ruta al archivo de base de datos SQLite
DB_PATH = "medical_records.db"


# Configuración básica del logger
logging.basicConfig(
    level = logging.INFO,
    format = '[%(asctime)s] [%(levelname)s] %(message)s',
    datefmt = '%H:%M:%S'
)

# Endpoint para obtener todas las historias clinicas de una especialidad
@app.route('/hcd/especialidad/<string:especialidad>', methods=['GET'])
def get_historias_por_espacialidad(especialidad):
    """
    Devuelve todas las historias clínicas de una especialidad dada.
    """
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute("""
            SELECT pacientes.nombre, pacientes.apellidos, pacientes.dni, historias_medicas.especialidad, historias_medicas.fecha_apertura, historias_medicas.fecha_cierre, historias_medicas.estado, historias_medicas.descripcion
            FROM historias_medicas 
            JOIN pacientes ON historias_medicas.paciente_id = pacientes.id 
            WHERE historias_medicas.especialidad = ?
        """, (especialidad,))
        datos = cursor.fetchall()

    if not datos:
        return "No hay datos para mostrar", 404

    # Convertimos los datos a un formato JSON soportando caracteres especiales
    resultados = [{"nombre": nombre, "apellidos": apellidos, "dni": dni, "especialidad": especialidad, "fecha_apertura": fecha_apertura, "fecha_cierre": fecha_cierre, "estado": estado, "descripcion": descripcion} for nombre, apellidos, dni, especialidad, fecha_apertura, fecha_cierre, estado, descripcion in datos]
    return jsonify(resultados)

# Endpoint para obtener todas las historias clinicas de un paciente
@app.route('/hcd/paciente/<string:paciente_dni>', methods=['GET'])
def get_historias_por_paciente(paciente_dni):
    """
    Devuelve todas las historias clínicas de un paciente dado.
    """
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute("""
            SELECT pacientes.nombre, pacientes.apellidos, historias_medicas.especialidad, historias_medicas.fecha_apertura, historias_medicas.fecha_cierre, historias_medicas.estado, historias_medicas.descripcion
            FROM historias_medicas 
            JOIN pacientes ON historias_medicas.paciente_id = pacientes.id 
            WHERE pacientes.dni = ?
        """, (paciente_dni,))
        datos = cursor.fetchall()

    if not datos:
        return "No hay datos para mostrar", 404

    # Convertimos los datos a un formato JSON
    resultados = [{"nombre": nombre, "apellidos": apellidos, "especialidad": especialidad, "fecha_apertura": fecha_apertura, "fecha_cierre": fecha_cierre, "estado": estado, "descripcion": descripcion} for nombre, apellidos, especialidad, fecha_apertura, fecha_cierre, estado, descripcion in datos]
    return jsonify(resultados)

# Endpoint que muestra estadisticas sobre el numero de clientes, numero de historias totales y nmumero de historias por especialidad
@app.route('/hcd/estadisticas', methods=['GET'])
def get_estadisticas():
    """
    Devuelve estadísticas sobre el número de pacientes, historias clínicas totales y por especialidad.
    """
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute("SELECT COUNT(*) FROM pacientes")
        num_pacientes = cursor.fetchone()[0]

        cursor = conn.execute("SELECT COUNT(*) FROM historias_medicas")
        num_historias_totales = cursor.fetchone()[0]

        cursor = conn.execute("""
            SELECT especialidad, COUNT(*) FROM historias_medicas GROUP BY especialidad
        """)
        historias_por_especialidad = cursor.fetchall()

    # Convertimos los datos a un formato JSON
    resultados = {
        "num_pacientes": num_pacientes,
        "num_historias_totales": num_historias_totales,
        "historias_por_especialidad": {especialidad: count for especialidad, count in historias_por_especialidad}
    }
    return jsonify(resultados)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Implementación de los endpoints para cargar las páginas web
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# endpoint para cargar la pagina web de inicio (index.html)
@app.route('/') 
def index():
    """
    Devuelve la página de inicio.
    """
    try:
        return send_file('index.html')
    except Exception as e:
        logging.error(f"Error al cargar la página de inicio: {e}")
        return "Error al cargar la página de inicio", 500
# enpoint para cargar la pagina about (about.html)
@app.route('/about')
def about():
    """
    Devuelve la página de información.
    """
    try:
        return send_file('about.html')
    except Exception as e:
        logging.error(f"Error al cargar la página de información: {e}")
        return "Error al cargar la página de información", 500
    
# enpoint para cargar la pagina de introducción del DNI del paciente (introducir_datos.html)
@app.route('/introducir_datos') 
def introducir_datos():
    """
    Devuelve la página para introducir datos del paciente.
    """
    try:
        return send_file('introducir_datos.html')
    except Exception as e:
        logging.error(f"Error al cargar la página de introducción de datos: {e}")
        return "Error al cargar la página de introducción de datos", 500

# enpoint para cargar la pagina de especialidad (especialidad.html)
# esta pagina es la misma con independencia de la especialidad elegida
# La especialidad se pasa como argumento en la URL y la pagina enviada send_file
# debe inclurir el nomber de la especialidad como parametros de forma que el 
# codigo javascript pueda operar con el nombre de la especialidad
@app.route('/especialidad')
def especialidad():
    """
    Devuelve la página de especialidad.
    """
    try:
        especialidad = request.args.get('especialidad')
        #return send_file('especialidad.html')
        return render_template('especialidad.html', especialidad=especialidad)
    except Exception as e:
        logging.error(f"Error al cargar la página de especialidad: {e}")
        return "Error al cargar la página de especialidad", 500


if len(sys.argv) != 2:
    print(len(sys.argv))
    print("Uso: apirest puerto")
    print("puerto = número de puerto en el el que registrar el servidor")
    sys.exit()

if __name__ == '__main__':
    logging.info("Arrancando el servidor")
    app.run(host='0.0.0.0', port=int(sys.argv[1]))
