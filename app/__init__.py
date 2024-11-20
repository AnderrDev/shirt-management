from flask import Flask
from flasgger import Swagger
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint
from app.db import init_db
from app.utils.error_handlers import register_error_handlers
from app.routes import estampas_bp, camisetas_bp, clientes_bp
from app.routes.main import bp as main_bp  # Importar el nuevo blueprint
from flask_cors import CORS

def create_app():
    # Inicialización de la aplicación Flask
    app = Flask(__name__)
    # Habilitar CORS para todas las rutas
    CORS(app)

    # Configuración de la aplicación
    app.config['DEBUG'] = True
    app.config.from_object('app.config.Config')
    app.config['JWT_SECRET_KEY'] = 'tu_clave_secreta'

    # Configuración de JWT
    JWTManager(app)

    # Configuración de Swagger UI
    configure_swagger_ui(app)

    # Inicialización de la base de datos y manejo de errores
    init_db(app)
    register_error_handlers(app)

    # Registro de Blueprints
    register_blueprints(app)

    return app

def configure_swagger_ui(app):
    """Configura Swagger UI y la documentación de API."""
    SWAGGER_URL = '/docs'
    API_URL = '/apispec.json'

    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={'app_name': "Flask API"}
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec',
                "route": '/apispec.json',
                "rule_filter": lambda rule: True,  # Todas las rutas
                "model_filter": lambda tag: True,  # Todos los modelos
            }
        ],
        "swagger_ui": True,
        "specs_route": "/docs/",
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "JWT Authorization header using the Bearer scheme. Example: 'Bearer {token}'"
            }
        },
        "security": [{"Bearer": []}],  # Define que las rutas requieren seguridad por defecto
    }

    Swagger(app, config=swagger_config)

def register_blueprints(app):
    """Registra todos los Blueprints en la aplicación Flask."""
    app.register_blueprint(main_bp)  # Ruta raíz
    app.register_blueprint(estampas_bp)
    app.register_blueprint(camisetas_bp)
    app.register_blueprint(clientes_bp)
