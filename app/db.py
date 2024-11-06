import mysql.connector
from flask import current_app, g

def init_db(app):
    app.teardown_appcontext(close_db)

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            user=current_app.config['MYSQL_USER'],
            password=current_app.config['MYSQL_PASSWORD'],
            host=current_app.config['MYSQL_HOST'],
            database=current_app.config['MYSQL_DB'],
            port=current_app.config['MYSQL_PORT']
        )
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
