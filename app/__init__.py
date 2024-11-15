from flask import Flask
from flasgger import Swagger
from flask_jwt_extended import JWTManager
from app.db import init_db
from app.utils.error_handlers import register_error_handlers
from app.routes import estampas_bp, camisetas_bp, clientes_bp
from app.routes.main import bp as main_bp  # Importar el nuevo blueprint
from flask_swagger_ui import get_swaggerui_blueprint

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True    
    app.config.from_object('app.config.Config')
    app.config['JWT_SECRET_KEY'] = 'tu_clave_secreta'
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
        }
    }
    
    JWTManager(app)
    Swagger(app, config=swagger_config)
    init_db(app)
    register_error_handlers(app)

    # Registro de Blueprints
    app.register_blueprint(main_bp)  # Registro de la ruta raíz
    app.register_blueprint(estampas_bp)
    app.register_blueprint(camisetas_bp)
    app.register_blueprint(clientes_bp)

    return app
