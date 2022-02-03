from flask import Flask
from usuarios_app import app
from usuarios_app.controladores import controladores_usuarios

if __name__ == "__main__":
    app.run( debug = True )