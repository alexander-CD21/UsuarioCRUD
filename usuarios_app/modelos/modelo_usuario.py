from usuarios_app.config.mysqlconnection import connectToMySQL

class Usuario:
    x = "Atributo de clase"

    def __init__(self, id,first_name , last_name,email,created_at,updated_at):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email= email
        self.created_at=created_at
        self.updated_at=updated_at

    def holaMundo():
        return "HOLA MUNDO"


    @classmethod
    def agregarUsuario(cls,nuevoUsuario):
        query = "INSERT INTO users(first_name, last_name, email,created_at,updated_at) VALUES( %(first_name)s, %(last_name)s, %(email)s,NOW(),NOW());"
        resultado = connectToMySQL( "users_db" ).query_db(query,nuevoUsuario)
        return resultado 

    @classmethod
    def obtenerListaUsuario(cls):
        query = "SELECT * FROM users;"
        resultado = connectToMySQL( "users_db" ).query_db( query )
        listaUsuarios = []
        for usua in resultado:
            listaUsuarios.append( Usuario(usua["id"],usua["first_name"],usua["last_name"], usua["email"], usua["created_at"], usua["updated_at"] ) )
        return listaUsuarios

    @classmethod
    def editarUsuario(cls,data):
        query="UPDATE users SET first_name = %(first_name)s,last_name = %(last_name)s,email = %(email)s, updated_at = NOW() WHERE id= %(id)s;"
        resultado=connectToMySQL("users_db").query_db(query,data)
        return resultado
        
    # QUIERO RETORNAR LISTA DE OBJETOS
    @classmethod
    def mostrarUno(cls,data):
        query="SELECT * FROM users WHERE id=%(id)s;"
        resultados1=connectToMySQL("users_db").query_db(query,data)
        listaUsuarios1=[]
        for usuario in resultados1:
            listaUsuarios1.append(Usuario(usuario["id"],usuario["first_name"],usuario["last_name"],usuario["email"],usuario["created_at"], usuario["updated_at"] ))
        return listaUsuarios1
    @classmethod
    def eliminarUno(cls,dic):
        query="DELETE FROM users WHERE id=%(id)s;"
        return connectToMySQL("users_db").query_db(query,dic)







    # QUIERO RETORNAR LISTA DE DICCIONARIOS
    #@classmethod
    #def mostrarUno(cls,data):
    #    query="SELECT * FROM users WHERE id=%(id)s;"
    #    return connectToMySQL("users_db").query_db(query,data)