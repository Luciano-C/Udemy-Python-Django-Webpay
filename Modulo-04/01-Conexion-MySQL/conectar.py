import mysql.connector
from mysql.connector import errorcode
import os
from dotenv import load_dotenv

load_dotenv()

def conectar():
    try:
        return mysql.connector.connect(
            host = "localhost",
            port = 3306,
            user = os.getenv("DATABASE_USER"),
            password = os.getenv("DATABASE_PASSWORD"),
            database = "productos-udemy"
        )
    except mysql.connector.Error as e:
        print(f"Error de conecxión {e}")
        exit()

def get_datos(sql):
    cn = conectar()
    cursor = cn.cursor(buffered=True)
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    except mysql.connector.Error as e:
        print(f"Error con la consulta: {e}")
        exit()
    cn.close()

def get_dato(sql):
    cn = conectar()
    cursor = cn.cursor(buffered=True)
    try:
        cursor.execute(sql)
        return cursor.fetchone()
    except mysql.connector.Error as e:
        print(f"Error con la consulta: {e}")
        exit()
    cn.close()


def set_datos(sql):
    cn = conectar()
    cursor = cn.cursor(buffered=True)
    try:
        cursor.execute(sql)
        cn.commit()
    except mysql.connector.Error as e:
        print(f"Error con la consulta: {e}")
        exit()
    cn.close()