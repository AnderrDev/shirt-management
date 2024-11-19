from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from flasgger import swag_from
from app.services.estampas_service import (
    obtener_estampas,
    obtener_estampa_por_id,
    insertar_estampa,
    actualizar_estampa,
    eliminar_estampa
)

bp = Blueprint('estampas', __name__, url_prefix='/estampas')

# Obtener todas las estampas (No requiere token)
@bp.route('/', methods=['GET'])
@swag_from({
    'tags': ['Estampas'],
    'responses': {
        200: {
            'description': 'Lista de todas las estampas',
            'examples': {
                'application/json': [{'id': 1, 'titulo': 'Estampa 1', 'color': 'Rojo'}]
            }
        }
    }
})
def get_estampas():
    estampas = obtener_estampas()
    return jsonify(estampas)

# Obtener una estampa por ID (No requiere token)
@bp.route('/<int:id>', methods=['GET'])
@swag_from({
    'tags': ['Estampas'],
    'parameters': [
        {'name': 'id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {
            'description': 'Estampa obtenida por ID',
            'examples': {
                'application/json': {'id': 1, 'titulo': 'Estampa 1', 'color': 'Rojo'}
            }
        },
        404: {'description': 'Estampa no encontrada'}
    }
})
def get_estampa_por_id(id):
    estampa = obtener_estampa_por_id(id)
    if estampa:
        return jsonify(estampa)
    return jsonify({"error": "Estampa no encontrada"}), 404

# Crear una nueva estampa (Requiere token)
@bp.route('/', methods=['POST'])
@jwt_required()
@swag_from({
    'tags': ['Estampas'],
    'security': [{"Bearer": []}],
    'parameters': [
        {'name': 'codigo', 'in': 'formData', 'type': 'string', 'required': True},
        {'name': 'titulo', 'in': 'formData', 'type': 'string', 'required': True},
        {'name': 'color', 'in': 'formData', 'type': 'string', 'required': True},
        {'name': 'clasificacion_id', 'in': 'formData', 'type': 'integer', 'required': True},
        {'name': 'categoria_id', 'in': 'formData', 'type': 'integer', 'required': True}
    ],
    'responses': {
        201: {'description': 'Estampa creada exitosamente'}
    }
})
def post_estampa():
    datos = request.form
    insertar_estampa(datos)
    return jsonify({"message": "Estampa creada exitosamente"}), 201

# Actualizar una estampa por ID (Requiere token)
@bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
@swag_from({
    'tags': ['Estampas'],
    'security': [{"Bearer": []}],
    'parameters': [
        {'name': 'id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'titulo', 'in': 'formData', 'type': 'string', 'required': True},
        {'name': 'color', 'in': 'formData', 'type': 'string', 'required': True},
        {'name': 'clasificacion_id', 'in': 'formData', 'type': 'integer', 'required': True},
        {'name': 'categoria_id', 'in': 'formData', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'Estampa actualizada exitosamente'},
        404: {'description': 'Estampa no encontrada'}
    }
})
def update_estampa(id):
    datos = request.form
    if actualizar_estampa(id, datos):
        return jsonify({"message": "Estampa actualizada exitosamente"}), 200
    return jsonify({"error": "Estampa no encontrada"}), 404

# Eliminar una estampa por ID (Requiere token)
@bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
@swag_from({
    'tags': ['Estampas'],
    'security': [{"Bearer": []}],
    'parameters': [
        {'name': 'id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'Estampa eliminada exitosamente'},
        404: {'description': 'Estampa no encontrada'}
    }
})
def delete_estampa(id):
    if eliminar_estampa(id):
        return jsonify({"message": "Estampa eliminada exitosamente"}), 200
    return jsonify({"error": "Estampa no encontrada"}), 404
