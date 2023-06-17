
from flask import Flask,render_template,request


#inicializacion del servido Flask 
app= Flask(__name__)

#configurarciones de conexion a BD
app.config['MYSQL_HOST']= "localhost"
app.config['MYSQL_USER']= "root"
app.config['MYSQL_PASSWORD']= "123456"
app.config['MYSQL_BD']= "bdflask"



#Declaracion de rutas


# ruta se compone del nombre y funcion

# Ruta Index http://localhost:5000
@app.route('/')
def index():
    return render_template ( 'index.html')

@app.route('/guardar',methods=['POST'])
def guardar():
    if request.method == 'POST':
        titulo = request.form['txtTitulo']
        artista = request.form['txtArtista']
        anio = request.form['txtAnio']
        print(titulo,artista,anio)
         

    return ("La inf del album llego a su ruta amigo ;")

@app.route('/eliminar')
def eliminar():
    return "se elimino el album en la BD"

# Ejecucion de servidor 
if __name__==  '__main__':
        app.run(port= 5000,debug=True)



