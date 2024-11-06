from flask import Blueprint, request, jsonify
from flasgger import swag_from
from app.services.clientes_service import obtener_clientes, insertar_cliente, eliminar_cliente, actualizar_cliente

bp = Blueprint('clientes', __name__, url_prefix='/clientes')

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
def update_cliente(id):
    datos = request.form
    actualizar_cliente(id, datos)
    return jsonify({"message": "Cliente actualizado exitosamente"}), 200
