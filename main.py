#Importar libreria de sql que contiene funciones de Base de datos en uso 
import sql 
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "jamon"

@app.route("/")
def index():
    return render_template("index.html")

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
        return redirect(url_for("index"))  #201 creado
    
    elif request.method == "GET":
        return render_template("libroadd.html")
    else:
        flash("Metodo no valido","warning")
        return redirect(url_for("index"))
    
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
        return redirect(url_for("index"))  #200 ok
    
    elif request.method == "GET":
        listar = sql.ListLibros()
        return render_template("updt.html", libros = listar)
    
    else:
        flash("Metodo no valido","warning")
        return redirect(url_for("index"))
    
#Eliminar un libro
@app.route("/delfront", methods = ["POST","GET"])
def delfront():
    if request.method == "POST":
        try:
            id1 = request.form["id"]
            sql.DeleteLibro(id1)
            flash("Libro Eliminado con exito","success")
            return redirect(url_for("index")) #200 ok
        
        except Exception as e:
            flash("Error: No se pudo eliminar el libro.", "danger")
            return redirect(url_for("index"))
        
    elif request.method == "GET":
        listar = sql.ListLibros()
        return render_template("delibro.html",libros = listar)
    else:
        flash("Metodo no valido","warning")
        return redirect(url_for("index"))
    
  #Listado de libros
@app.route("/listad", methods = ["GET"])
def listad():
    listar = sql.ListLibros()
    return render_template("listado.html", libros = listar)

#Busqueda de libros    
@app.route("/listad/fil", methods = ["GET"])
def listad_fil():
    if request.method == "GET":
        campo = request.args.get("campo")
        valor = request.args.get("valor")
        resultados = []
        if campo and valor:
            
            resultados = sql.GetLibro(campo, valor)
        return render_template("listadfil.html", libros = resultados)
    else:
        flash("Metodo no valido","warning")
        return redirect(url_for("index"))


if __name__ == "__main__":
  app.run(debug = True)