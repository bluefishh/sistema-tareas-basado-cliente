from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Inicializar la base de datos
def init_db():
    conn = sqlite3.connect('tareas.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tareas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Obtener todas las tareas
def listar_tareas():
    conn = sqlite3.connect('tareas.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tareas")
    tareas = cursor.fetchall()
    conn.close()
    return tareas

# Agregar tarea
def crear_tarea(description):
    conn = sqlite3.connect('tareas.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tareas (description) VALUES (?)", (description,))
    conn.commit()
    conn.close()

# Eliminar tarea
def eliminar_tarea(id_tarea):
    conn = sqlite3.connect('tareas.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tareas WHERE id = ?", (id_tarea,))
    conn.commit()
    conn.close()

# Actualizar tarea
def actualizar_tarea(id_tarea, nueva_descripcion):
    conn = sqlite3.connect('tareas.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE tareas SET description = ? WHERE id = ?", (nueva_descripcion, id_tarea))
    conn.commit()
    conn.close()

# Ruta principal (listar tareas)
@app.route('/')
def index():
    tareas = listar_tareas()
    return render_template('index.html', tareas=tareas)

# Ruta para agregar tarea
@app.route('/crear', methods=['POST'])
def crear():
    descripcion = request.form['descripcion']
    if descripcion:
        crear_tarea(descripcion)
    return redirect(url_for('index'))

# Ruta para eliminar tarea
@app.route('/eliminar/<int:id_tarea>')
def borrar(id_tarea):
    eliminar_tarea(id_tarea)
    return redirect(url_for('index'))

# Ruta para actualizar tarea
@app.route('/actualizar/<int:id_tarea>', methods=['POST'])
def actualizar(id_tarea):
    nueva_descripcion = request.form['nueva_descripcion']
    if nueva_descripcion:
        actualizar_tarea(id_tarea, nueva_descripcion)
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
