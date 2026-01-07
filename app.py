from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret_key_nexus'

def get_db_connection():
    # Conexión a tu archivo NEXUS.db
    conn = sqlite3.connect('NEXUS.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('indexx.html')

@app.route('/guardar_cliente', methods=['POST'])
def guardar_cliente():
    nombre = request.form['nombre']
    email = request.form['email']
    telefono = request.form['telefono']
    direccion = request.form['direccion']

    try:
        conn = get_db_connection()
        # Nota: Asegúrate que la tabla se llame CLIENTE sin espacios
        conn.execute('INSERT INTO CLIENTE (nombre, email, telefono, direccion) VALUES (?, ?, ?, ?)',
                     (nombre, email, telefono, direccion))
        conn.commit()
        conn.close()
        flash('Cliente guardado exitosamente')
    except Exception as e:
        flash(f'Error al guardar: {e}')
    
    return redirect(url_for('indexx'))

if __name__ == '__main__':
    app.run(debug=True)