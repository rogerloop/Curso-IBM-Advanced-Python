# insertar registros desde python a mysql

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

# ejecutar la sentencia insert
cursor = personas_db.cursor() # Creo objeto cursor
sentencia_sql = 'INSERT INTO personas(nombre, apellido, edad) VALUES(%s, %s, %s)'
valores = ('Victor', 'Ramos', 46)
cursor.execute(sentencia_sql, valores)
personas_db.commit()  # guarda los cambios en la DB
print(f'Se ha agregado el nuevo registro a la bd : {valores}')

cursor.close()
personas_db.close()
