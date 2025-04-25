# actualizar registros desde python a mysql

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

# ejecutar la sentencia update
cursor = personas_db.cursor() # Creo objeto cursor
sentencia_sql = 'UPDATE personas SET nombre=%s, apellido=%s, edad=%s WHERE id=%s'
valores = ('Victoria', 'Flores', 45, 8)
cursor.execute(sentencia_sql, valores)
personas_db.commit()  # guarda los cambios en la DB
print(f'Se ha actualizado un registro de la DB...')

cursor.close()
personas_db.close()