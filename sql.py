#Importar biblioteca de PyMongoDB
import os
import redis 
import json 
from dotenv import load_dotenv

load_dotenv()

#Cadena de conexion de la bd
def conn():
    try:

        #metodo de conexion a keydb con variables de entorno 
        db = redis.Redis(
            host = os.getenv("HOST"),
            port = os.getenv("Puerto", 6505),
            decode_responses = True
        )
        db.ping() #verificador de conexion
        return db
    except Exception as e:
        print("Error al conectar con la base de datos:", e)
        raise
    
database = conn()

#Funciones para agregar, actualizar, eliminar, ver listado de libros y buscar libros 

def idnuevo():
    return database.incr("libro:id")


def AddLibro(Titulo,Autor,Genero,Ano,Estado): 
    try:
        id = idnuevo()
        key = f"libro:{id}"

        nuevo = {
        "id": id,
        "Titulo": Titulo,
        "Autor": Autor,
        "Genero": Genero,
        "Ano": int(Ano),
        "Estado_Lectura": int(Estado)  # 1 leido, 0 no leido
    }

        database.set(key,json.dumps(nuevo))

        print("Libro Agregado.")
    except Exception as e:
        print("Error al agregar el libro:", e)


def UpdateLibro(id1, Titulo, Autor, Genero, Ano, Estado):
    key = f"libro:{id1}"

    try:
        if database.exists(key):
            libro = json.loads(database.get(key))

            libro.update(
                {
                    "Titulo": Titulo,
                    "Autor": Autor,
                    "Genero": Genero,
                    "Ano": int(Ano),
                    "Estado_Lectura": int(Estado)
                }
            )
            database.set(key, json.dumps(libro))
            print("Se actualizo un libro")
        else:
            print("Libro no existe")
    except Exception as e:
        print("Error al actualizar libro:", e)


def DeleteLibro(id1):
    key = f"libro:{id1}"

    try:
        if not database.exists(key):
            print("Libro no existe")
        else:
            if database.delete(key):
                print("Libro eliminado")
            else:
                print("No se elimino ningun libro")
    except Exception as e:
        print("Error al eliminar libro:", e)


def ListLibros():
    try:
        resultado = []
        for key in database.scan_iter("libro:*"):
            libro = json.loads(database.get(key))
            if not isinstance(libro, dict):
                continue
            resultado.append(libro)

        return resultado
    
    except Exception as e:
        print("Error al ejecutar busqueda de libro: ",e)
        return []

def GetLibro(campo,id):
    try:
        resultado = []
        for key in database.scan_iter("libro:*"):
            libro = json.loads(database.get(key))
            if not isinstance(libro, dict):
                continue
            if id.lower() in str(libro[campo]).lower():
                resultado.append(libro)
        return resultado
    
    except Exception as e:
        print("Error al ejecutar busqueda de libro: ",e)
        return []