from flask import Flask, render_template,redirect,session,flash,request
from usuarios_app import app
from usuarios_app.modelos.modelo_usuario import Usuario



@app.route('/' , methods=['GET'])
def raiz():
    return redirect('/users')

@app.route('/users' , methods=["GET"])
def leerDatos():
    listaUsuarios=Usuario.obtenerListaUsuario()
    return render_template("leer.html",usuario=listaUsuarios)

@app.route('/users/new' , methods=["GET"])
def datos():
    return render_template("crear.html")

@app.route('/users/create', methods=['POST'])
def creaDatos():
    nuevoUsuario={
        "first_name" : request.form[ "first_name" ],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    session["first_name"] = request.form["first_name"]
    session["last_name"] = request.form["last_name"]
    session["email"] = request.form["email"]
    resultados=Usuario.agregarUsuario(nuevoUsuario)
    return redirect(f'/users/show/{resultados}')

@app.route('/users/show/<int:id>', methods=['GET'])
def show(id):
    data={
        "id" : id
    }
    listaUsuarios1=Usuario.mostrarUno(data)
    print(listaUsuarios1)
    return render_template("show.html",usuario=listaUsuarios1)

@app.route('/users/edit/<int:id>', methods=['GET'])
def editar(id):
    dict={
        "id":id
    }
    editar1=Usuario.mostrarUno(dict)
    return render_template("edit.html",editar=editar1)

@app.route('/users/edit/<int:id>', methods=['POST'])
def actualizar(id):
    dict1={
       "first_name" : request.form[ "first_name" ],
       "last_name" : request.form["last_name"],
       "email" : request.form["email"],
       "id":id
    }
    Usuario.editarUsuario(dict1)

    session["first_name"] = request.form["first_name"]
    session["last_name"] = request.form["last_name"]
    session["email"] = request.form["email"]

    return redirect('/')



@app.route('/users/delete/<int:id>',methods=['GET'])
def delete(id):
    dic={
        "id":id
    }
    Usuario.eliminarUno(dic)
    return redirect('/users')