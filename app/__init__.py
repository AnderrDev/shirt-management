from flask import Flask
from flasgger import Swagger
from app.db import init_db
from app.utils.error_handlers import register_error_handlers
from app.routes import estampas_bp, camisetas_bp, clientes_bp
from app.routes.main import bp as main_bp  # Importar el nuevo blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    Swagger(app)
    init_db(app)
    register_error_handlers(app)

    # Registro de Blueprints
    app.register_blueprint(main_bp)  # Registro de la ruta raíz
    app.register_blueprint(estampas_bp)
    app.register_blueprint(camisetas_bp)
    app.register_blueprint(clientes_bp)

    return app
