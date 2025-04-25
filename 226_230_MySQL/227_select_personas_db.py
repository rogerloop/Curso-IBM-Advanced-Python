# nos permite seleccionar los registros de una tabla de la DB
# import para variables de entorno seguras y protegidas
from dotenv import load_dotenv
import os

# Conectar a la Base de Datos
import mysql.connector

load_dotenv()  # Carga las variables de entorno del archivo .env

personas_db = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')
)

# ejecutar la sentencia select
cursor = personas_db.cursor() # Creo objeto cursor
cursor.execute('SELECT * FROM personas');
resultado = cursor.fetchall()
for persona in resultado:
    print(persona)


cursor.close()
personas_db.close()