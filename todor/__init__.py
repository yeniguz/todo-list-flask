from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy #importando las clases de la base de datos

db = SQLAlchemy()#creando una extendion de la base de datos

def create_app():

    app = Flask(__name__)
    
    #configuracion del proyecto
    app.config.from_mapping(
        DEBUG = False,
        SECRET_KEY = 'devtodo',
        SQLALCHEMY_DATABASE_URI = "sqlite:///todolist.db"#estableciendo conection con labase dedatos
    )
    
    db.init_app(app) #inicializamos la coneccion a la base de datos
    
    #Registrar Blueprint
    from . import todo
    app.register_blueprint(todo.bp)
    #---------------------------------
    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return render_template('index.html')
    with app.app_context():
        db.create_all()
    
    return app
