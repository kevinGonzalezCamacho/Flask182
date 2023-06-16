
from flask import Flask 


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
    return "Hola Mundo"

@app.route('/guardar')
def guardar():
    return "se guardo el album en la BD"

@app.route('/eliminar')
def eliminar():
    return "se elimino el album en la BD"

# Ejecucion de servidor 
if __name__==  '__main__':
        app.run(port= 5000,debug=True)