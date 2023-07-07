from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "DB_Fruteria"

app.secret_key = 'mysecretkey'
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/consultar_frutas', methods=['POST', 'GET'])
def consultar_frutas():
    if request.method == 'POST':
        nombre = request.form['nombre']

        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM tbFrutas WHERE fruta LIKE %s', (f'%{nombre}%',))
        frutas = cur.fetchall()
        cur.close()

        return render_template('consultarFrutas.html', frutas=frutas)
    else:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM tbFrutas')
        frutas = cur.fetchall()
        cur.close()

        return render_template('consultarRegistros.html', frutas=frutas)


@app.route('/agregar_fruta', methods=['POST'])
def agregar_fruta():
    if request.method == 'POST':
        fruta = request.form['fruta']
        temporada = request.form['temporada']
        precio = request.form['precio']
        stock = request.form['stock']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO tbFrutas (fruta, temporada, precio, stock) VALUES (%s, %s, %s, %s)',
                    (fruta, temporada, precio, stock))
        mysql.connection.commit()
        cur.close()

        flash('Fruta agregada correctamente')
    return redirect(url_for('index'))

@app.route('/editar_fruta/<int:id>')
def editar_fruta(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tbFrutas WHERE id = %s', (id,))
    fruta = cur.fetchone()
    cur.close()

    return render_template('editarFrutas.html', fruta=fruta)

@app.route('/actualizar_fruta/<int:id>', methods=['POST'])
def actualizar_fruta(id):
    if request.method == 'POST':
        fruta = request.form['fruta']
        temporada = request.form['temporada']
        precio = request.form['precio']
        stock = request.form['stock']

        cur = mysql.connection.cursor()
        cur.execute('UPDATE tbFrutas SET fruta=%s, temporada=%s, precio=%s, stock=%s WHERE id=%s',
                    (fruta, temporada, precio, stock, id))
        mysql.connection.commit()
        cur.close()

        flash('Fruta actualizada en la base de datos')
    return redirect(url_for('index'))

@app.route('/eliminar_fruta/<int:id>')
def eliminar_fruta(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tbFrutas WHERE id = %s', (id,))
    fruta = cur.fetchone()
    cur.close()

    return render_template('eliminarFrutas.html', fruta=fruta)

@app.route('/borrar_fruta/<int:id>', methods=['POST'])
def borrar_fruta(id):
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM tbFrutas WHERE id = %s', (id,))
        mysql.connection.commit()
        cur.close()

        flash('Fruta eliminada correctamente')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)
