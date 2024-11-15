import bcrypt
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, create_access_token
from flasgger import swag_from
from app.services.clientes_service import obtener_clientes, insertar_cliente, eliminar_cliente, actualizar_cliente, obtener_cliente_por_usuario

bp = Blueprint('clientes', __name__, url_prefix='/clientes')


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
    if cliente and cliente['clave'] == clave:  # Comparación directa
        token = create_access_token(identity={'id': cliente['id'], 'usuario': cliente['usuario'], 'rol': cliente['rol']})
        return jsonify({"access_token": token}), 200

    return jsonify({"error": "Usuario o clave incorrectos"}), 401   


@bp.route('/', methods=['GET'])
@swag_from({
    'tags': ['Clientes'],  # Etiqueta para agrupar esta ruta
    'responses': {
        200: {
            'description': 'Lista de clientes',
            'examples': {
                'application/json': [{'id': 1, 'nombre': 'Juan', 'apellido': 'Pérez'}]
            }
        }
    }
})
@jwt_required()
def get_clientes():
    clientes = obtener_clientes()
    return jsonify(clientes)

@bp.route('/', methods=['POST'])
@swag_from({
    'tags': ['Clientes'],  # Etiqueta para agrupar esta ruta
    'parameters': [
        {'name': 'id', 'in': 'formData', 'type': 'string', 'required': True},
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
    insertar_cliente(datos)
    return jsonify({"message": "Cliente creado exitosamente"}), 201

@bp.route('/<int:id>', methods=['DELETE'])
@swag_from({
    'tags': ['Clientes'],  # Etiqueta para agrupar esta ruta
    'parameters': [
        {'name': 'id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'Cliente eliminado exitosamente'}
    }
})

@jwt_required()
def delete_cliente(id):
    eliminar_cliente(id)
    return jsonify({"message": "Cliente eliminado exitosamente"}), 200

@bp.route('/<int:id>', methods=['PUT'])
@swag_from({
    'tags': ['Clientes'],  # Etiqueta para agrupar esta ruta
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
        200: {'description': 'Cliente actualizado exitosamente'}
    }
})

@jwt_required()
def update_cliente(id):
    datos = request.form
    actualizar_cliente(id, datos)
    return jsonify({"message": "Cliente actualizado exitosamente"}), 200
