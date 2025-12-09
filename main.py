#Importar libreria de sql que contiene funciones de Base de datos en uso 
import sql 
from flask import Flask, render_template, url_for,request

app = Flask(__name__)
app.secret_key = "jamon"

@app.route("/")
def index():
    libros = sql.ListLibros()
    return render_template("index.html",libros=libros)

#Opciones Agregar un libro
@app.route("/addLibro", methods = ["Post"])
def addfront():
    if request.method == "Post":
        t = request.form["Titulo: "]
        au = request.form["Autor: "]
        g = request.form["Genero: "]
        an = request.form["Año del libro: "] 
        e = int(request.form["Estado (1. Leido / 2.No leido): "])
        sql.AddLibro(t, au, g,an, e)


#Actualizar un libro
@app.route("/updt", methods = ["Put"])
def updtfont():
    listar = sql.ListLibros()

    if not listar:
        print("\n No hay resultados.\n")
    else:
        print("\n===== LISTADO DE LIBROS =====")
        for l in listar:
            if not isinstance(l, dict):
                continue
            estado = l["Estado_Lectura"]
            if estado == 1:
                estado = "Leido"
            else:
                estado = "No leido"
            print(f"\nID: {l['id']}\nTítulo: {l['Titulo']}\nAutor: {l['Autor']}\nGénero: {l['Genero']}\nAño: {l['Ano']}\nEstado: {estado}\n")
                    
        try:
            id = input("Ingrese el ID del libro a actualizar (puede copiar y pegar el id): ")
        except:
            print("ID invalido.")

        t = input("Nuevo titulo: ")
        au = input("Nuevo autor: ")
        g = input("Nuevo genero: ")
        an = input("Nuevo año del libro: ") 
        es = input("Nuevo estado (1. Leido / 2.No leido): ")

        sql.UpdateLibro(id, t, au, g,an, es)

#Eliminar un libro
@app.route("/dlt", methods = ["Delete"])
def delfront():
    listar = sql.ListLibros()

    if not listar:
        print("\n No hay resultados.\n")
    else:
        print("\n===== LISTADO DE LIBROS =====")
        for l in listar:
            if not isinstance(l, dict):
                continue
            estado = l["Estado_Lectura"]
            if estado == 1:
                estado = "Leido"
            else:
                estado = "No leido"
                print(f"\nID: {l['id']}\nTítulo: {l['Titulo']}\nAutor: {l['Autor']}\nGénero: {l['Genero']}\nAño: {l['Ano']}\nEstado: {estado}\n")
                        
        try:
            id = input("Ingrese el ID del libro a eliminar: ") 
        except:
            print("ID invalido.")

    sql.DeleteLibro(id)

"""   #Listado de libros
@app.route("/addLiro", methods = ["Post"])
            listar = sql.ListLibros()
            if not listar:
                    print("\n No hay resultados.\n")
            else:
                print("\n===== LISTADO DE LIBROS =====")
                for l in listar:
                    if not isinstance(l, dict):
                        continue

                    estado = int(l["Estado_Lectura"])

                    if estado == 1:
                        estado = "Leido"
                    else:
                        estado = "No leido"
                    print(f"\nID: {l['id']}\nTítulo: {l['Titulo']}\nAutor: {l['Autor']}\nGénero: {l['Genero']}\nAño: {l['Ano']}\nEstado: {estado}\n")

        #Busqueda de libros    
@app.route("/addLiro", methods = ["Post"])
            print("\nBuscar por:")
            print("1. Título")
            print("2. Autor")
            print("3. Género")

            tipo = input("Seleccione opcion: ")
            campos = {"1": "Titulo", "2": "Autor", "3": "Genero"}

            if tipo not in campos:
                print("Opción inválida.")
                continue

            valor = input("Valor a buscar: ")
            resultados = sql.GetLibro(campos[tipo], valor)

            if not resultados:
                    print("\n No hay resultados.\n")
            else:
                print("\n===== LISTADO DE LIBROS =====")
                for l in resultados:
                    if not isinstance(l, dict):
                        continue
                    estado = int(l["Estado_Lectura"])
                    if estado == 1:
                        estado = "Leido"
                    else:
                        estado = "No leido"
                    print(f"\nID: {l['id']}\nTítulo: {l['Titulo']}\nAutor: {l['Autor']}\nGénero: {l['Genero']}\nAño: {l['Ano']}\nEstado: {estado}\n")
                         """

if __name__ == "__main__":
    app.run(debug = True)