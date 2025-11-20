import sqlite3 #Lo usaremos para almacenar: usuarios,roles,permisos
#empresas,codigos de accesos
import uuid #Sirve para generar los codigos de identificacion internos,largos
import secrets #Datos que se le muestran al usuario, mas cortos
import hashlib #Encriptar contraseñas
import os #Sirve para comprobar si los datos ya existen en la base de datos
from datetime import datetime #Ver cuando se creo un usuario
DB_PATH = "medirutas.sqlite3" # Este es el nombre del archivo donde voy a guardar mi base de datos de sqlite
def iniciobasededatos(db_path: str = DB_PATH): # db_path es un parametro del archivo db, str la clase de datos y si no
#se le asigna una ruta correra por DB_PATH por defecto 
 conexion = sqlite3.connect(db_path) # Si existe un archivo lo abre y si no lo crea en la base sqlite, haca guardare, se modificara y se cambiaran datos
 c = conexion.cursor() #manda las instrucciones a sql
#Haca vamos a crear el codigo de sqlite
 c.execute("""
CREATE TABLE IF NOT EXISTS empresas(
    id TEXT PRIMARY KEY --Esto es el codigo interno generado mediante uuid
    nombre TEXT NOT NULL
    codigo_empresa TEXT UNIQUE NOT NULL --Codigo maestro usado por admin lider 
    info_file_url TEXT
    ) 
    """)
 #CODIGOS DE ACCESO:
 c.execute("""
CREATE TABLE IF NOT EXISTS codigos_acceso(
    codigo TEXT PRIMARY KEY 
    empresa_id TEXT NOT NULL
    rol TEXT NOT NULL
    descripcion TEXT
    created_at TEXT
    FOREIGN KEY (empresa_id)REFERENCES empresas(id)       
    )          
    """)