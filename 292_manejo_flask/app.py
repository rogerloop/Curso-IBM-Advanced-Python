from flask import Flask, render_template
from cliente_dao import ClienteDAO
from cliente import Cliente  # Importing the Cliente class
from cliente_forma import ClienteForm

app = Flask(__name__)

titulo_app ='Zona Fit (GYM)'

@app.route('/')     # url: http://localhost:5000/ 
@app.route('/index.html')        # url: http://localhost:5000/index.html
def inicio():
    app.logger.debug('Entramos al path de inicio /')
    
    # Recuperamos clientes de la DB
    clientes_db = ClienteDAO.seleccionar()
    # Creamos un objeto de cliente form vacio
    cliente = Cliente()
    cliente_form = ClienteForm(obj=cliente)

    return render_template('index.html', titulo=titulo_app, clientes=clientes_db, form=cliente_form)

if __name__ == '__main__':
    app.run(debug=True)