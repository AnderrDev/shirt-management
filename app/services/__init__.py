# Importa los servicios de cada módulo
from .estampas_service import (
    obtener_estampas,
    obtener_estampa_por_id,
    insertar_estampa,
    actualizar_estampa,
    eliminar_estampa
)

from .camisetas_service import (
    obtener_camisetas,
    insertar_camiseta,
    eliminar_camiseta,
    actualizar_camiseta
)

from .clientes_service import (
    obtener_clientes,
    insertar_cliente,
    eliminar_cliente,
    actualizar_cliente
)

# Exporta todos los servicios para uso global
__all__ = [
    'obtener_estampas', 'obtener_estampa_por_id', 'insertar_estampa',
    'actualizar_estampa', 'eliminar_estampa', 
    'obtener_camisetas', 'insertar_camiseta', 'eliminar_camiseta', 'actualizar_camiseta',
    'obtener_clientes', 'insertar_cliente', 'eliminar_cliente', 'actualizar_cliente'
]
