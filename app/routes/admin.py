from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('admin', __name__)

@bp.route('/admin-endpoint', methods=['GET'])
@jwt_required()
def admin_endpoint():
    current_user = get_jwt_identity()
    if current_user['rol'] != 'Administrador':
        return jsonify({"error": "No autorizado"}), 403

    return jsonify({"message": "Acceso permitido solo a administradores"}), 200
