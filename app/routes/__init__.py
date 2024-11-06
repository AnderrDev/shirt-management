# Importa los Blueprints de cada módulo de rutas
from .estampas import bp as estampas_bp
from .camisetas import bp as camisetas_bp
from .clientes import bp as clientes_bp

# Exporta los Blueprints para que puedan ser registrados en la app principal
__all__ = ['estampas_bp', 'camisetas_bp', 'clientes_bp']
