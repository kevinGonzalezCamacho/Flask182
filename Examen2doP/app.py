from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "db_floreria"

app.secret_key = 'mysecretkey'
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('indexflor.html')


@app.route('/consultar_registros', methods=['POST', 'GET'])
def consultar_registros():
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM tbFlores')
        frutas = cur.fetchall()
        cur.close()

        return render_template('consultar_Registros.html', frutas=frutas)


@app.route('/agregar_fruta', methods=['POST'])
def agregar_fruta():
    if request.method == 'POST':
        ID = request.form['id']
        Nombre = request.form['nombre']
        Cantidad = request.form['cantidad']
        Precio = request.form['Precio']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO tbFlores (ID, Nombre, cantidad, Precio) VALUES (%s, %s, %s, %s)',
                    (ID, Nombre, Cantidad, Precio))
        mysql.connection.commit()
        cur.close()

        flash('Flor agregada correctamente')
    return redirect(url_for('indexFlor'))


@app.route('/eliminar_flor/<int:id>')
def eliminar_flor(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tbFlores WHERE id = %s', (id,))
    flor = cur.fetchone()
    cur.close()

    return render_template('eliminar_flor.html', flor=flor)

@app.route('/borrar_fruta/<int:id>', methods=['POST'])
def borrar_flor(id):
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM tbFlores WHERE id = %s', (id,))
        mysql.connection.commit()
        cur.close()

        flash('Flor eliminada correctamente')
    return redirect(url_for('indexFlor'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)