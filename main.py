#Importar libreria de sql que contiene funciones de Base de datos en uso 
import sql 
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "jamon"

@app.route("/")
def index():
    libros = sql.ListLibros()
    return render_template("index.html",libros=libros)

#Opciones Agregar un libro
@app.route("/addfront", methods = ["POST","GET"])
def addfront():
    if request.method == "POST":
        t = request.form["titulo"]
        au = request.form["autor"]
        g = request.form["genero"]
        an = request.form["ano"] 
        e = int(request.form["Estado_Lectura"])
        if e not in [1,2]:
            flash("Estado incorrecto","warning")
            return redirect(url_for("index")) #415 dato no soportado 
        
        sql.AddLibro(t, au, g,an, e)
        flash("Libro Agregado con exito","success")
        return redirect(url_for("index")), 200  #201 creado
    
    elif request.method == "GET":
        return render_template("libroadd.html")
    else:
        flash("Metodo no valido","warning")
        return redirect(url_for("index")),405
    
#Actualizar un libro
@app.route("/updtfont", methods = ["POST","GET"])
def updtfont():
    if request.method == "POST":
        id = request.form["id"]
        t = request.form["titulo"]
        au = request.form["autor"]
        g = request.form["genero"]
        an = request.form["ano"] 
        es = int(request.form["estado1"])

        if id == "":
            flash("Debe indicar el ID","warning")
            return redirect(url_for("index")) 
        if es not in [1,2]:
            flash("Estado incorrecto","warning")
            return redirect(url_for("index")) #415 dato no soportado 
        
        sql.UpdateLibro(id, t, au, g,an, es)
        flash("Libro Actualizado con exito","success")
        return redirect(url_for("index")), 200  #200 ok
    elif request.method == "GET":
        listar = sql.ListLibros()
        return render_template("updt.html", libros = listar)
    else:
        flash("Metodo no valido","warning")
        return redirect(url_for("index")),405
    
#Eliminar un libro
@app.route("/delfront", methods = ["DELETE","GET"])
def delfront():
    if request.method == "DELETE":
        try:
            sql.DeleteLibro(id)
            flash("Libro Eliminado con exito","success")
            return redirect(url_for("index")),200 #200 ok
        
        except Exception as e:
            flash("Error: No se pudo eliminar el libro.", "danger")
            return redirect(url_for("index")), 500
        
    elif request.method == "GET":
        listar = sql.ListLibros()
        return render_template("delibro.html",libros = listar)
    else:
        flash("Metodo no valido","warning")
        return redirect(url_for("index")),405
    
  #Listado de libros
@app.route("/listad", methods = ["GET"])
def listad():
    listar = sql.ListLibros()
    return render_template("listado.html", libros = listar)

#Busqueda de libros    
@app.route("/get/id", methods = ["GET"])
def getpor():

    valor = input("Valor a buscar: ")
    resultados = None
    #sql.GetLibro(campos[tipo], valor)
    return resultados



if __name__ == "__main__":
  app.run(debug = True)