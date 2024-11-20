from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, create_access_token
from flasgger import swag_from
from app.services.clientes_service import (
    obtener_clientes, 
    insertar_cliente, 
    eliminar_cliente, 
    actualizar_cliente, 
    obtener_cliente_por_usuario
)
from app.services.role import role_required

bp = Blueprint('clientes', __name__, url_prefix='/clientes')

# Login para autenticación y generación de token JWT
@bp.route('/login', methods=['POST'])
@swag_from({
    'tags': ['Clientes'],
    'parameters': [
        {'name': 'usuario', 'in': 'formData', 'type': 'string', 'required': True},
        {'name': 'clave', 'in': 'formData', 'type': 'string', 'required': True}
    ],
    'responses': {
        200: {'description': 'Login exitoso', 'examples': {'application/json': {'access_token': 'token'}}},
        401: {'description': 'Usuario o clave incorrectos'}
    }
})
def login():
    datos = request.form
    usuario = datos.get('usuario')
    clave = datos.get('clave')

    if not usuario or not clave:
        return jsonify({"error": "Usuario y clave son obligatorios"}), 400

    cliente = obtener_cliente_por_usuario(usuario)
    if cliente and cliente['clave'] == clave:
        # Genera el token con la identidad del usuario
        token = create_access_token(identity={
            'id': cliente['id'],
            'usuario': cliente['usuario'],
            'rol': cliente['rol']
        })
        
        # Devuelve el token y la información del usuario
        return jsonify({
            "access_token": token,
            "usuario": {
                "id": cliente['id'],
                "usuario": cliente['usuario'],
                "rol": cliente['rol'],
                "nombre": cliente['nombre'],
                "apellido": cliente['apellido'],
                "correo": cliente['correo']
            }
        }), 200

    return jsonify({"error": "Usuario o clave incorrectos"}), 401


@bp.route('/admin-only', methods=['POST'])
@swag_from ({
    'tags': ['Clientes'],
    'security': [{"Bearer": []}],
    'responses': {
        200: {'description': 'Solo los administradores pueden acceder a esto'}
    }
})
@jwt_required()
@role_required('Administrador')
def admin_only():
    return jsonify({"message": "Solo los administradores pueden acceder a esto"}), 200

@bp.route('/cliente-endpoint', methods=['GET'])
@jwt_required()
@role_required('Cliente')
def cliente_endpoint():
    return jsonify({"message": "Solo los clientes pueden acceder a esto"}), 200


# Obtener lista de clientes (protegido con JWT)
@bp.route('/', methods=['GET'])
@swag_from({
    'tags': ['Clientes'],
    'security': [{"Bearer": []}],  # Indica que requiere token
    'responses': {
        200: {
            'description': 'Lista de clientes',
            'examples': {
                'application/json': [{'id': 1, 'nombre': 'Juan', 'apellido': 'Pérez'}]
            }
        },
        401: {'description': 'No autorizado'}
    }
})
def get_clientes():
    clientes = obtener_clientes()
    return jsonify(clientes)


# Crear un nuevo cliente (protegido con JWT)
@bp.route('/', methods=['POST'])
@swag_from({
    'tags': ['Clientes'],
    'security': [{"Bearer": []}],  # Indica que requiere token
    'parameters': [
        {'name': 'nombre', 'in': 'formData', 'type': 'string', 'required': True},
        {'name': 'apellido', 'in': 'formData', 'type': 'string', 'required': True},
        {'name': 'correo', 'in': 'formData', 'type': 'string', 'required': True},
        {'name': 'rol', 'in': 'formData', 'type': 'string', 'required': True},
        {'name': 'usuario', 'in': 'formData', 'type': 'string', 'required': True},
        {'name': 'clave', 'in': 'formData', 'type': 'string', 'required': True}
    ],
    'responses': {
        201: {'description': 'Cliente creado exitosamente'}
    }
})
def post_cliente():
    datos = request.form
    nuevo_id = insertar_cliente(datos)
    return jsonify({
        "message": "Cliente creado exitosamente",
        "id": nuevo_id  # Retorna el nuevo ID generado
    }), 201


# Eliminar un cliente por ID (protegido con JWT)
@bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
@swag_from({
    'tags': ['Clientes'],
    'parameters': [
        {'name': 'id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'Cliente eliminado exitosamente'},
        401: {'description': 'No autorizado'}
    }
})
def delete_cliente(id):
    eliminar_cliente(id)
    return jsonify({"message": "Cliente eliminado exitosamente"}), 200


# Actualizar un cliente por ID (protegido con JWT)
@bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
@swag_from({
    'tags': ['Clientes'],
    'parameters': [
        {'name': 'id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'nombre', 'in': 'formData', 'type': 'string', 'required': True},
        {'name': 'apellido', 'in': 'formData', 'type': 'string', 'required': True},
        {'name': 'correo', 'in': 'formData', 'type': 'string', 'required': True},
        {'name': 'rol', 'in': 'formData', 'type': 'string', 'required': True},
        {'name': 'usuario', 'in': 'formData', 'type': 'string', 'required': True},
        {'name': 'clave', 'in': 'formData', 'type': 'string', 'required': True}
    ],
    'responses': {
        200: {'description': 'Cliente actualizado exitosamente'},
        401: {'description': 'No autorizado'}
    }
})
def update_cliente(id):
    datos = request.form
    actualizar_cliente(id, datos)
    return jsonify({"message": "Cliente actualizado exitosamente"}), 200
