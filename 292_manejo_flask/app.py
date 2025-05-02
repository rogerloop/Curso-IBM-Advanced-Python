from flask import Flask, render_template

app = Flask(__name__)

titulo_app ='Zona Fit (GYM)'

@app.route('/')     # url: http://localhost:5000/ 
@app.route('/index.html')        # url: http://localhost:5000/index.html
def inicio():
    app.logger.debug('Entramos al path de inicio /')
    return render_template('index.html', titulo = titulo_app)

if __name__ == '__main__':
    app.run(debug=True)