from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from flasgger import swag_from
from app.services.camisetas_service import (
    obtener_camisetas,
    insertar_camiseta,
    eliminar_camiseta,
    actualizar_camiseta
)

bp = Blueprint('camisetas', __name__, url_prefix='/camisetas')

# Obtener lista de camisetas (No requiere token)
@bp.route('/', methods=['GET'])
@swag_from({
    'tags': ['Camisetas'],
    'responses': {
        200: {
            'description': 'Lista de camisetas',
            'examples': {
                'application/json': [{'id': 1, 'talla': 'M', 'color': 'Azul'}]
            }
        }
    }
})
def get_camisetas():
    camisetas = obtener_camisetas()
    return jsonify(camisetas)

# Crear una nueva camiseta (Requiere token)
@bp.route('/', methods=['POST'])
@jwt_required()
@swag_from({
    'tags': ['Camisetas'],
    'security': [{"Bearer": []}],
    'parameters': [
        {'name': 'id', 'in': 'formData', 'type': 'string', 'required': True},
        {'name': 'talla', 'in': 'formData', 'type': 'string', 'required': True},
        {'name': 'color', 'in': 'formData', 'type': 'string', 'required': True},
        {'name': 'material', 'in': 'formData', 'type': 'string', 'required': True},
        {'name': 'precio', 'in': 'formData', 'type': 'number', 'required': True}
    ],
    'responses': {
        201: {'description': 'Camiseta creada exitosamente'}
    }
})
def post_camiseta():
    datos = request.form
    insertar_camiseta(datos)
    return jsonify({"message": "Camiseta creada exitosamente"}), 201

# Eliminar una camiseta por ID (Requiere token)
@bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
@swag_from({
    'tags': ['Camisetas'],
    'security': [{"Bearer": []}],
    'parameters': [
        {'name': 'id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'Camiseta eliminada exitosamente'}
    }
})
def delete_camiseta(id):
    eliminar_camiseta(id)
    return jsonify({"message": "Camiseta eliminada exitosamente"}), 200

# Actualizar una camiseta por ID (Requiere token)
@bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
@swag_from({
    'tags': ['Camisetas'],
    'security': [{"Bearer": []}],
    'parameters': [
        {'name': 'id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'talla', 'in': 'formData', 'type': 'string', 'required': True},
        {'name': 'color', 'in': 'formData', 'type': 'string', 'required': True},
        {'name': 'material', 'in': 'formData', 'type': 'string', 'required': True},
        {'name': 'precio', 'in': 'formData', 'type': 'number', 'required': True}
    ],
    'responses': {
        200: {'description': 'Camiseta actualizada exitosamente'}
    }
})
def update_camiseta(id):
    datos = request.form
    actualizar_camiseta(id, datos)
    return jsonify({"message": "Camiseta actualizada exitosamente"}), 200
