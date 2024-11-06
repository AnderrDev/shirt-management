import mysql.connector
from flask import current_app, g

def init_db(app):
    app.teardown_appcontext(close_db)

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host="mysql_container",  # Debe coincidir con el nombre del contenedor
            user="user",
            password="userpassword",
            database="base_camisetas",
            port=3306
        )
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
